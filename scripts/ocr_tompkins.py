"""OCR del libro "Los Aspectos en Astrología" de Sue Tompkins y
extracción de interpretaciones para aspectos.json.

Reutiliza OCR cache en /tmp/textos_tompkins.json si existe.
"""

import re
import json
import os
import sys
from pdf2image import convert_from_path
import tesserocr

DOC_PATH = "docs/Los-Aspectos-en-Astrologia-Sue-Tompkins.pdf"
TESSDATA = "/home/pipe/miniconda3/share/tessdata"
CACHE_PATH = "/tmp/textos_tompkins.json"

# Order of chapters in the book
CAPITULOS = [
    (138, 199, "sol"),        # Capítulo VI: ASPECTOS DEL SOL (pp139-199)
    (200, 245, "luna"),       # Capítulo VII: ASPECTOS DE LA LUNA (pp201-245)
    (246, 285, "mercurio"),   # Capítulo VIII: ASPECTOS DE MERCURIO
    (286, 320, "venus"),      # Capítulo IX: ASPECTOS DE VENUS
    (321, 350, "marte"),      # Capítulo X: ASPECTOS DE MARTE
    (351, 367, "jupiter"),    # Capítulo XI: ASPECTOS DE JÚPITER
    (368, 384, "saturno"),    # Capítulo XII: ASPECTOS DE SATURNO
    (385, 459, "transpersonales"),  # Capítulos XIII-XV: Urano, Neptuno, Plutón
]

# Regex for section headers like "Sol-Mercurio", "Luna-Marte"
RE_HDR = re.compile(r'^(Sol|Luna|Mercurio|Venus|Marte|Júpiter|Saturno|Urano|Neptuno|Plutón)[-\s]+(Sol|Luna|Mercurio|Venus|Marte|Júpiter|Saturno|Urano|Neptuno|Plutón)$')

NOMBRES = {
    "Sol": "sol", "Luna": "luna", "Mercurio": "mercurio",
    "Venus": "venus", "Marte": "marte", "Júpiter": "jupiter",
    "Saturno": "saturno", "Urano": "urano", "Neptuno": "neptuno",
    "Plutón": "pluton", "Pluton": "pluton"
}

ASPECTOS = ["conjuncion", "sextil", "cuadratura", "trino", "oposicion"]

# All expected planet-planet pairs (sol covers sol-luna through sol-pluton, etc.)
PAREJAS_ESPERADAS = set()
for i, p1 in enumerate(["sol", "luna", "mercurio", "venus", "marte", "jupiter", "saturno", "urano", "neptuno", "pluton"]):
    for p2 in ["sol", "luna", "mercurio", "venus", "marte", "jupiter", "saturno", "urano", "neptuno", "pluton"]:
        if p1 != p2 and f"{p2}_{p1}" not in PAREJAS_ESPERADAS:
            PAREJAS_ESPERADAS.add(f"{p1}_{p2}")

# Secciones no detectadas automáticamente (mapeo manual)
# (key, pagina_inicio, pagina_fin) - 0-indexed
MANUALES = [
    ("luna_saturno", 223, 228),      # Capítulo VII: después de Luna-Urano
    ("mercurio_jupiter", 254, 255),   # Capítulo VIII: después de Mercurio-Marte
    ("marte_neptuno", 337, 343),      # Capítulo X: dentro de Marte
    ("marte_pluton", 343, 351),       # Capítulo X: después de Marte-Neptuno
    ("jupiter_saturno", 354, 359),    # Capítulo XI: dentro de Júpiter
    ("urano_neptuno", 397, 401),      # Capítulo XIII: dentro de transpersonales
    ("urano_pluton", 397, 403),       # Capítulo XIII: dentro de transpersonales
    ("neptuno_pluton", 401, 405),     # Capítulo XIII: dentro de transpersonales
]

# Some OCR-common misspellings
CORRECCIONES = {
    "Plurón": "Plutón",
    "Pluton": "Plutón",
    "Júpíter": "Júpiter",
    "Mercuno": "Mercurio",
}


def ocr_paginas(desde=139, hasta=460, dpi=120):
    """OCR páginas del PDF, guarda y devuelve cache."""
    # Intentar cargar cache
    if os.path.exists(CACHE_PATH):
        with open(CACHE_PATH, 'r', encoding='utf-8') as f:
            cache = json.load(f)
        textos = list(cache.get("textos", []))
        if len(textos) >= hasta:
            print(f"Cargados {len(textos)} textos del caché ({CACHE_PATH})")
            return textos

    print(f"OCR páginas {desde}-{hasta}...")
    textos = []
    api = tesserocr.PyTessBaseAPI(lang='spa', path=TESSDATA)
    for p in range(1, hasta + 1):
        imgs = convert_from_path(DOC_PATH, first_page=p, last_page=p, dpi=dpi)
        api.SetImage(imgs[0])
        texto = api.GetUTF8Text()
        textos.append(texto)
        if p % 50 == 0:
            print(f"  OCR p{p}/{hasta}", flush=True)
    api.End()

    # Guardar cache
    with open(CACHE_PATH, 'w', encoding='utf-8') as f:
        json.dump({"textos": textos}, f, ensure_ascii=False)
    print(f"Cache guardado: {CACHE_PATH}")
    return textos


def encontrar_secciones(textos):
    """Encuentra secciones planeta-planeta en cada capítulo."""
    secciones = {}  # key: "sol_marte" -> (pag_inicio_idx, pag_fin_idx)

    for (inicio_pag, fin_pag, _) in CAPITULOS:
        for i in range(inicio_pag, min(fin_pag + 1, len(textos))):
            txt = textos[i]
            lines = [l.strip() for l in txt.split('\n') if l.strip()]
            for linea in lines:
                # Apply OCR corrections
                for wrong, correct in CORRECCIONES.items():
                    linea = linea.replace(wrong, correct)
                m = RE_HDR.match(linea)
                if m:
                    p1 = NOMBRES.get(m.group(1))
                    p2 = NOMBRES.get(m.group(2))
                    if p1 and p2:
                        key = f"{p1}_{p2}"
                        # Only keep if both planets are in core planet list
                        if key in PAREJAS_ESPERADAS and key not in secciones:
                            secciones[key] = i
                            break

    return secciones


ORDEN_PLANETAS = ["sol", "luna", "mercurio", "venus", "marte", "jupiter", "saturno", "urano", "neptuno", "pluton"]

def generar_claves_aspectos(p1, p2):
    """Genera las 5 claves de aspecto para un par de planetas.
    Usa el orden: Sol, Luna, Mercurio, Venus, Marte, Júpiter, Saturno, Urano, Neptuno, Plutón."""
    claves = []
    for asp in ASPECTOS:
        if ORDEN_PLANETAS.index(p1) < ORDEN_PLANETAS.index(p2):
            a, b = p1, p2
        else:
            a, b = p2, p1
        claves.append(f"{a}_{asp}_{b}")
    return claves


def extraer_texto_seccion(textos, inicio, fin):
    partes = []
    for i in range(inicio, fin + 1):
        if i < len(textos):
            partes.append(textos[i])
    return "\n".join(partes)


def limpiar_texto(texto):
    texto = re.sub(r'\n+', ' ', texto)
    texto = re.sub(r'\s+', ' ', texto).strip()
    return texto


def main():
    textos = ocr_paginas()

    print("\nBuscando secciones...")
    secciones = encontrar_secciones(textos)

    # Añadir secciones manuales
    for key, inicio, fin in MANUALES:
        if key not in secciones:
            secciones[key] = inicio

    print(f"Secciones encontradas: {len(secciones)}")
    for k, v in sorted(secciones.items(), key=lambda x: x[1]):
        p1, p2 = k.split("_")
        print(f"  {p1.title()}-{p2.title()}: p{v+1}")

    # Extraer textos y expandir a todas las combinaciones de aspecto
    resultados = {}
    secciones_ordenadas = sorted(secciones.items(), key=lambda x: x[1])

    # Build a lookup for manual section ends
    manual_fins = {k: f-1 for k, _, f in MANUALES}

    for idx, (key, inicio) in enumerate(secciones_ordenadas):
        # Fin: manual override, próxima sección, o fin
        if key in manual_fins:
            fin = manual_fins[key]
        elif idx + 1 < len(secciones_ordenadas):
            fin = secciones_ordenadas[idx + 1][1] - 1
        else:
            fin = len(textos) - 1

        # Ensure fin is within chapter bounds
        for (ch_inicio, ch_fin, _) in CAPITULOS:
            if ch_inicio <= inicio <= ch_fin and fin > ch_fin:
                fin = ch_fin
                break

        texto = extraer_texto_seccion(textos, inicio, fin)
        texto_limpio = limpiar_texto(texto)

        if len(texto_limpio) > 200:
            # Asignar a las 5 claves de aspecto
            p1, p2 = key.split("_")
            for clave in generar_claves_aspectos(p1, p2):
                resultados[clave] = texto_limpio

    # Guardar
    ruta = "datos/aspectos_tompkins.json"
    with open(ruta, 'w', encoding='utf-8') as f:
        json.dump(resultados, f, ensure_ascii=False, indent=2)
    print(f"\nGuardado: {ruta} ({len(resultados)} entradas)")

    # Estadísticas
    with open('datos/aspectos.json', 'r', encoding='utf-8') as f:
        actuales = json.load(f)
    coinciden = sum(1 for k in resultados if k in actuales)
    mas_largas = sum(1 for k, v in resultados.items() if k in actuales and len(v) > len(actuales[k]))
    print(f"  Coinciden con aspectos.json: {coinciden}/{len(resultados)}")
    print(f"  Más largas que original: {mas_largas}")

    # Mostrar faltantes
    faltantes = set(actuales.keys()) - set(resultados.keys())
    if faltantes:
        print(f"  Aspectos NO cubiertos: {len(faltantes)}")
        for k in sorted(faltantes)[:10]:
            print(f"    - {k}")


if __name__ == "__main__":
    main()
