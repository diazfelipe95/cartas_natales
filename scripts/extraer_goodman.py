"""Extrae descripciones de signos solares de Linda Goodman
y genera contenido para planetas_signos.json (sol_en_{signo}) y angulos_signos.json."""

import re
import json
import pymupdf

DOC_PATH = "docs/Linda Goodman Signos solares.pdf"

# Orden de los signos en el libro
SIGNOS = [
    ("aries", "ARIES, EL CARNERO"),
    ("tauro", "TAURO, EL TORO"),
    ("geminis", "GÉMINIS, LOS GEMELOS"),
    ("cancer", "CÁNCER, EL CANGREJO"),
    ("leo", "LEO, EL LEÓN"),
    ("virgo", "VIRGO, LA VIRGEN"),
    ("libra", "LIBRA, LA BALANZA"),
    ("escorpio", "ESCORPIO, EL ESCORPIÓN, EL ÁGUILA"),
    ("sagitario", "SAGITARIO"),
    ("capricornio", "CAPRICORNIO, LA CABRA"),
    ("acuario", "ACUARIO, EL AGUADOR"),
    ("piscis", "PISCIS, EL PEZ"),
]

# Variantes de cada header (con/sin comas, acentos)
HEADER_VARIANTS = {}
for key, h in SIGNOS:
    variants = {h}
    # Sin acentos
    variants.add(h.translate(str.maketrans('ÉÁÓÍÚ', 'EAOIU', '')))
    # Sin comas
    variants.add(h.replace(',', ''))
    # Sin acentos ni comas
    variants.add(h.replace(',', '').translate(str.maketrans('ÉÁÓÍÚ', 'EAOIU', '')))
    # Solo primera palabra para signos sin subtítulo completo (SAGITARIO)
    first = h.split(',')[0].strip()
    if first != h:
        variants.add(first)
    HEADER_VARIANTS[key] = {v for v in variants if v and len(v) >= 5}


def extraer_texto_signo(doc, num_pagina_inicio, num_pagina_fin):
    """Extrae todo el texto de un capítulo de signo."""
    texto = ""
    for i in range(num_pagina_inicio, num_pagina_fin + 1):
        if i < len(doc):
            pagina = doc[i].get_text()
            texto += pagina + "\n"
    return texto


def encontrar_secciones_signo(doc):
    """Encuentra las páginas de inicio y fin de cada signo."""
    paginas_signo = {}

    # Saltar páginas de índice (primeras 5 páginas)
    for i in range(5, len(doc)):
        text = doc[i].get_text()
        lines = [l.strip() for l in text.split('\n') if l.strip()]
        for linea in lines[:8]:  # Solo primeras líneas (header está al inicio de página)
            for key, variants in HEADER_VARIANTS.items():
                if key in paginas_signo:
                    continue
                for v in variants:
                    if v in linea and len(linea) < 70:
                        paginas_signo[key] = i
                        break

    signos_orden = [s[0] for s in SIGNOS]
    secciones = {}
    for idx, key in enumerate(signos_orden):
        inicio = paginas_signo.get(key)
        if inicio is None:
            continue
        if idx + 1 < len(signos_orden):
            fin = paginas_signo.get(signos_orden[idx + 1], len(doc) - 1) - 1
        else:
            fin = len(doc) - 1
        secciones[key] = (inicio, fin)

    return secciones


def limpiar_texto(texto):
    """Limpia el texto extraído."""
    # Quitar encabezados de página (Linda Goodman / Los signos del zodíaco / número)
    texto = re.sub(r'Linda Goodman\s*\nLos signos del zodíaco\s*\n\d+\s*\n', '', texto)
    texto = re.sub(r'\s*\n\s*', ' ', texto)
    texto = re.sub(r'\s+', ' ', texto).strip()
    return texto


def extraer_descripcion_principal(texto_signo):
    """Extrae la primera sección descriptiva del signo (después de 'Como reconocer a')."""
    # Buscar "Como reconocer a" y extraer hasta la siguiente sección
    match = re.search(
        r'Como reconocer a\s+\w+(.*?)(?:El\s+hombre\s+\w+|La\s+mujer\s+\w+|El\s+niño\s+\w+|El\s+jefe\s+\w+|El\s+empleado\s+\w+)',
        texto_signo, re.DOTALL | re.IGNORECASE
    )
    if not match:
        # Alternativa: hasta que aparezca la primera línea de solo "El" o "La" en mayúscula
        match = re.search(
            r'Como reconocer a\s.*?\n\n(.*?)(?:\n\s*\nEl\s+|\n\s*\nLa\s+)',
            texto_signo, re.DOTALL | re.IGNORECASE
        )
    if match:
        txt = limpiar_texto(match.group(1))
        # Tomar primeros ~500 caracteres como descripción principal
        if len(txt) > 200:
            return txt
    return None


def extraer_goodman():
    doc = pymupdf.open(DOC_PATH)
    secciones = encontrar_secciones_signo(doc)

    resultados = {}
    for key, (inicio, fin) in secciones.items():
        texto = extraer_texto_signo(doc, inicio, fin)
        desc = extraer_descripcion_principal(texto)
        if desc:
            resultados[f"sol_en_{key}"] = desc
            resultados[f"ascendente_en_{key}"] = desc
            resultados[f"luna_en_{key}"] = desc

    doc.close()
    return resultados


def generar_json(resultados, ruta_salida="datos/planetas_signos_goodman.json"):
    with open(ruta_salida, 'w', encoding='utf-8') as f:
        json.dump(resultados, f, ensure_ascii=False, indent=2)
    print(f"Guardado: {ruta_salida} ({len(resultados)} entradas)")

    # Estadísticas
    print(f"  Cubre {len([k for k in resultados if k.startswith('sol_')])} signos solares")

    return resultados


def comparar_con_actuales(extraidas):
    with open('datos/planetas_signos.json', 'r', encoding='utf-8') as f:
        actuales = json.load(f)
    coinciden = 0
    mas_largas = 0
    for k, v in extraidas.items():
        if k in actuales:
            coinciden += 1
            if len(v) > len(actuales[k]):
                mas_largas += 1
    print(f"Coinciden con claves existentes: {coinciden}")
    print(f"De ellas, más largas que el original: {mas_largas}")


if __name__ == "__main__":
    # Debug: mostrar páginas encontradas
    doc = pymupdf.open(DOC_PATH)
    secciones = encontrar_secciones_signo(doc)
    print("Secciones encontradas:")
    for k, (i, f) in sorted(secciones.items(), key=lambda x: x[1][0]):
        print(f"  {k}: pp {i+1}-{f+1}")
    doc.close()

    resultados = extraer_goodman()
    generar_json(resultados)
    comparar_con_actuales(resultados)
