#!/usr/bin/env python3
"""Pipeline de curacion, expansion y generacion sintetica de contenido astrologico.

Modos:
  - expandir: Conserva ideas centrales y expande con profundidad psicologica
  - generar: Crea desde cero usando conocimiento astrologico del modelo

Uso:
  export GROQ_API_KEY="gsk_..."
  python scripts/curar_y_generar_contenido.py --batch=3
  python scripts/curar_y_generar_contenido.py
"""

import json
import os
import re
import shutil
import time
import argparse
import logging
from pathlib import Path
from datetime import datetime

from groq import Groq

# ─── Configuracion ───────────────────────────────────────────────────────────

MODEL_NAME = "llama-3.3-70b-versatile"

# Prompts (extraidos de read me/curado_DB.md)
SYSTEM_PROMPT = """Actuas como un astrologo psicologico moderno y un editor de contenido experto.

Tu meta es entregar textos interpretativos perfectamente pulidos para el reporte final de un cliente.

REGLAS ESTRICTAS DE ESTILO:
1. Tono empatico, serio, profesional y enfocado al crecimiento personal, inspirado en Howard Sasportas.
2. Dirigete al usuario de forma directa en segunda persona del singular.
3. Estructura el resultado en:
   - Dinamica interna o esencia.
   - Retos o bloqueos habituales.
   - Potencial evolutivo y desarrollo personal.
4. No uses jergas tecnicas complejas.
5. No menciones autores.
6. No utilices metaforas excesivas.
7. No introduzcas predicciones deterministas.
8. Devuelve unicamente la interpretacion final, sin prefacios ni encabezados."""

PROMPT_EXPANDIR = """Toma el siguiente texto interpretativo para {clave}.

Conserva sus ideas principales y su significado esencial.
No resumas ni sustituyas completamente el contenido.

Amplia la interpretacion desarrollando:
- Motivaciones psicologicas.
- Conflictos internos.
- Patrones emocionales.
- Potencial de crecimiento.

Adapta todo al estilo editorial definido.

Texto original:
{texto}"""

PROMPT_GENERAR = """Basandote en tus conocimientos astrologicos profundos, genera una interpretacion completa y original para:

{contexto}

La interpretacion debe seguir exactamente el estandar editorial del proyecto (segunda persona, estilo Sasportas, enfoque psicologico-evolutivo)."""

# (clave, ruta, modo, filtro_opcional)
# Si filtro es None, se procesan todas las entradas
FILES_CONFIG = [
    ("goodman", "datos/planetas_signos_goodman.json", "expandir", None),
    ("tompkins", "datos/aspectos_tompkins.json", "expandir", None),
    ("angulos", "datos/angulos_signos.json", "generar", None),
    ("casas", "datos/casas_signos.json", "generar", None),
    ("planetas_signos", "datos/planetas_signos.json", "generar",
     lambda k, v: len(v) < 200),
    ("planetas_casas", "datos/planetas_casas.json", "generar",
     lambda k, v: len(v) < 200),
]

FORBIDDEN_HEADERS = [
    "aqui tienes", "aqui esta", "interpretacion astrologica",
    "respuesta:", "resultado:", "texto generado", "**interpretacion",
]


# ─── Helpers ─────────────────────────────────────────────────────────────────

def cargar_env(path=".env"):
    if not Path(path).exists():
        return
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if "=" in line:
                k, v = line.split("=", 1)
                os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))


def clave_a_contexto(clave, archivo_key):
    """Convierte clave JSON en contexto humanamente legible."""
    if archivo_key in ("casas",):
        m = re.match(r"casa_(\d+)_(.+)", clave)
        if m:
            return f"Interpretacion astrologica de Casa {m.group(1)} con {m.group(2).title()} en la cuspide"
        return f"Interpretacion astrologica de {clave.replace('_', ' ').title()}"
    elif archivo_key in ("planetas_signos", "goodman"):
        if re.match(r"(sol|luna|mercurio|venus|marte|jupiter|saturno|urano|neptuno|pluton|ceres|palas|juno|vesta|quiron|lilith|nodo_norte|nodo_sur|ascendente)_en_(.+)", clave):
            m = re.match(r"(.+)_en_(.+)", clave)
            return f"{m.group(1).title()} en {m.group(2).title()}"
        return f"Interpretacion astrologica de {clave.replace('_', ' ').title()}"
    elif archivo_key in ("planetas_casas",):
        m = re.match(r"(.+)_en_casa_(\d+)", clave)
        if m:
            return f"{m.group(1).title()} en Casa {m.group(2)}"
        return f"Interpretacion astrologica de {clave.replace('_', ' ').title()}"
    elif archivo_key in ("tompkins",):
        m = re.match(r"(.+)_(conjuncion|sextil|cuadratura|trino|oposicion)_(.+)", clave)
        if m:
            return f"{m.group(1).title()} en {m.group(2)} con {m.group(3).title()}"
        return f"Aspecto astrologico de {clave.replace('_', ' ').title()}"
    elif archivo_key in ("angulos",):
        if clave.startswith("ascendente_en_"):
            return f"Ascendente en {clave.replace('ascendente_en_', '').title()}"
        return f"Angulo astrologico de {clave.replace('_', ' ').title()}"
    return clave.replace("_", " ").title()


def validate_text(text):
    """Valida calidad del texto generado. Retorna (valido, razones)."""
    reasons = []
    if not text or not text.strip():
        reasons.append("vacio")
    elif len(text) < 100:
        reasons.append(f"muy_corto ({len(text)} chars)")

    text_lower = text.lower()
    for h in FORBIDDEN_HEADERS:
        if h in text_lower:
            reasons.append(f"encabezado: '{h}'")

    # Segunda persona
    if not any(p in text_lower for p in ["tu", "te ", "ti", "contigo", "tuyo", "tuya", " eres ", "tienes", "puedes", "debes", "necesitas"]):
        reasons.append("no_segunda_persona")

    return len(reasons) == 0, reasons


def setup_logger():
    Path("logs").mkdir(exist_ok=True)
    logger = logging.getLogger("curador")
    logger.setLevel(logging.DEBUG)

    fh = logging.FileHandler(
        f"logs/curacion_{datetime.now():%Y%m%d_%H%M%S}.log",
        encoding="utf-8",
    )
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(logging.Formatter("%(asctime)s | %(levelname)s | %(message)s"))
    logger.addHandler(fh)

    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    ch.setFormatter(logging.Formatter("%(message)s"))
    logger.addHandler(ch)

    return logger


def groq_generate(client, system, user_prompt, max_retries=3):
    """Llama a Groq con reintentos y backoff."""
    for attempt in range(max_retries):
        try:
            response = client.chat.completions.create(
                model=MODEL_NAME,
                messages=[
                    {"role": "system", "content": system},
                    {"role": "user", "content": user_prompt},
                ],
                temperature=0.7,
                max_tokens=2048,
            )
            text = response.choices[0].message.content.strip()
            return text, None
        except Exception as e:
            err = str(e)
            # Rate limit: esperar y reintentar
            if "429" in err or "rate_limit" in err.lower():
                wait = 5 * (attempt + 1)
                time.sleep(wait)
            elif attempt < max_retries - 1:
                time.sleep(3)
            else:
                return None, err
    return None, "max_retries_exceeded"


# ─── Procesamiento ───────────────────────────────────────────────────────────

def process_file(client, config, batch, logger):
    key, path, mode, filtro = config
    logger.info(f"\n{'='*60}")
    logger.info(f"[{key}] modo={mode} archivo={path}")
    logger.info(f"{'='*60}")

    if not Path(path).exists():
        logger.error(f"  ! Archivo no encontrado: {path}")
        return 0, 0

    with open(path, encoding="utf-8") as f:
        data = json.load(f)

    entries = list(data.items())
    if filtro:
        entries = [(k, v) for k, v in entries if filtro(k, v)]
        logger.info(f"  Filtrados: {len(entries)}/{len(data)} entradas a procesar")

    if batch:
        entries = entries[:batch]
        logger.info(f"  Modo batch: {len(entries)} entradas")

    if not entries:
        logger.info("  Sin entradas para procesar.")
        return 0, 0

    resultados = dict(data.items())  # copia, preserva no-procesadas
    total = len(entries)
    ok = 0
    errors = 0
    retries = 0

    for idx, (clave, valor_original) in enumerate(entries, 1):
        logger.info(f"  [{idx}/{total}] {clave} ... ")

        # Construir prompt
        if mode == "generar":
            ctx = clave_a_contexto(clave, key)
            user_prompt = PROMPT_GENERAR.format(contexto=ctx)
        else:
            user_prompt = PROMPT_EXPANDIR.format(clave=clave, texto=valor_original)

        texto_final = None
        for attempt in range(3):
            text, error = groq_generate(client, SYSTEM_PROMPT, user_prompt)
            if text:
                valido, razones = validate_text(text)
                if valido:
                    texto_final = text
                    break
                else:
                    logger.warning(f"    intento {attempt+1}: {', '.join(razones)}")
                    retries += 1
                    time.sleep(1.5)
            else:
                logger.warning(f"    intento {attempt+1}: {error}")
                retries += 1
                time.sleep(3)

        if texto_final:
            resultados[clave] = texto_final
            ok += 1
            logger.info(f"    OK ({len(texto_final)} chars)")
        else:
            logger.error(f"    FALLIDO - conservado original")
            errors += 1

        # Rate limiting: ~20 req/min (free tier: 30 rpm)
        time.sleep(3)

    # Guardar
    with open(path, "w", encoding="utf-8") as f:
        json.dump(resultados, f, ensure_ascii=False, indent=2)

    logger.info(f"  -> Guardado: {path}")
    logger.info(f"  -> Resultados: {ok} OK, {errors} errores, {retries} reintentos")

    return ok, errors


def main():
    parser = argparse.ArgumentParser(
        description="Pipeline de curacion y generacion de contenido astrologico"
    )
    parser.add_argument("--batch", type=int, default=0,
                        help="Procesar solo N entradas por archivo (prueba)")
    parser.add_argument("--files", nargs="*",
                        help="Archivos a procesar: goodman, tompkins, angulos, casas, planetas_signos, planetas_casas")
    parser.add_argument("--no-backup", action="store_true",
                        help="Omitir backup de archivos originales")
    args = parser.parse_args()

    cargar_env()
    api_key = os.environ.get("GROQ_API_KEY")
    if not api_key or api_key == "AQUI_TU_API_KEY":
        print("ERROR: GROQ_API_KEY no configurada.")
        print("  Edita .env y pon tu API key de https://console.groq.com/")
        return

    client = Groq(api_key=api_key)
    print(f"Modelo: {MODEL_NAME}\n")

    logger = setup_logger()

    # Backup
    if not args.no_backup:
        backup_dir = f"datos/backup_pre_curacion_{datetime.now():%Y%m%d_%H%M%S}"
        Path(backup_dir).mkdir(parents=True, exist_ok=True)
        for _, path, _, _ in FILES_CONFIG:
            if Path(path).exists():
                shutil.copy2(path, f"{backup_dir}/{Path(path).name}")
                logger.info(f"Backup: {path} -> {backup_dir}/")

    total_ok = total_errors = 0
    for config in FILES_CONFIG:
        key = config[0]
        if args.files and key not in args.files:
            logger.info(f"  [SKIP] {key} (no incluido en --files)")
            continue
        ok, err = process_file(client, config, args.batch, logger)
        total_ok += ok
        total_errors += err

    logger.info(f"\n{'='*60}")
    logger.info(f"  RESUMEN FINAL: {total_ok} OK, {total_errors} errores")
    logger.info(f"  Log: logs/curacion_*.log")
    logger.info(f"{'='*60}")


if __name__ == "__main__":
    main()
