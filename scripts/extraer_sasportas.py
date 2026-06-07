"""Extrae interpretaciones de 'Las Doce Casas' de Howard Sasportas
y genera un JSON con claves {planeta}_en_casa_{n} para planetas_casas.json."""

import re
import json
import pymupdf

DOC_PATH = "docs/las-doce-casas-howard-sasportas.pdf"

# Mapeo de nombres de planetas en el PDF a claves JSON
MAP_PLANETA = {
    "sol": "sol", "luna": "luna", "mercurio": "mercurio",
    "venus": "venus", "marte": "marte", "júpiter": "jupiter",
    "saturno": "saturno", "urano": "urano", "neptuno": "neptuno",
    "plutón": "pluton", "quiron": "quiron", "quirón": "quiron",
}

# Mapeo de números de casa en español a número
MAP_CASA = {
    "primera": 1, "segunda": 2, "tercera": 3, "cuarta": 4,
    "quinta": 5, "sexta": 6, "séptima": 7, "septima": 7,
    "octava": 8, "novena": 9, "décima": 10, "decima": 10,
    "undécima": 11, "undecima": 11, "onceava": 11,
    "duodécima": 12, "duodecima": 12, "doceava": 12,
}

# Variantes de nombres de casa (incluyendo typos del PDF)
CASA_PATRONES = {}
for k, v in MAP_CASA.items():
    CASA_PATRONES[k] = v
# Typos conocidos del PDF
CASA_PATRONES['lndécima'] = 11  # "Marte en la Lndécima"
CASA_PATRONES['lndecima'] = 11

# Patrón amplio para detectar encabezados de sección
# Acepta: "El Sol en la Primera", "Marte en la Lndécima", "lúpiter en la Séptima"
PLANETAS_ALT = list(MAP_PLANETA.keys()) + ['lúpiter']  # typo
MAP_PLANETA_ALT = {**MAP_PLANETA, 'lúpiter': 'jupiter'}

RE_SECCION = re.compile(
    r'(?:(?:El|La)\s+)?(' + '|'.join(PLANETAS_ALT) + r')\s+en\s+la\s+(' + '|'.join(CASA_PATRONES.keys()) + r')',
    re.IGNORECASE
)

# "Nodo norte en la Tercera, nodo sur en la Novena" - pares de nodos
RE_NODO = re.compile(
    r'Nodo\s+(norte|sur)\s+en\s+la\s+(' + '|'.join(CASA_PATRONES.keys()) + r')',
    re.IGNORECASE
)

MAP_NODO = {'norte': 'nodo_norte', 'sur': 'nodo_sur'}

# Patrón para detectar cambio de casa en texto fluido:
# "En la casa Siete, Júpiter puede manifestarse..."
RE_CASA_FLUIDA = re.compile(
    r'en\s+la\s+casa\s+(' + '|'.join(CASA_PATRONES.keys()) + r')',
    re.IGNORECASE
)


def limpiar_texto(texto):
    """Limpia y normaliza el texto extraído."""
    texto = re.sub(r'\s*\n\s*', ' ', texto)
    texto = re.sub(r'\s+', ' ', texto).strip()
    texto = texto.replace(' .', '.').replace(' ,', ',').replace(' ;', ';')
    texto = texto.replace(' :', ':').replace(' !', '!').replace(' ?', '?')
    return texto


def extraer_secciones(ruta_pdf):
    doc = pymupdf.open(ruta_pdf)
    texto_completo = ""
    for i in range(len(doc)):
        texto_completo += doc[i].get_text() + "\n"

    lineas = texto_completo.split('\n')
    secciones = {}
    buffer = []
    key_actual = None

    def guardar_seccion():
        nonlocal buffer, key_actual
        if key_actual and buffer:
            txt = limpiar_texto(' '.join(buffer))
            if len(txt) > 50:
                if key_actual not in secciones:
                    secciones[key_actual] = txt
        buffer = []

    def es_encabezado_valido(linea):
        """Retorna (planeta, casa_num) si la línea es un encabezado de sección.
           Solo acepta líneas CORTAS donde el título es el contenido principal."""
        if len(linea) > 60:
            return None, None

        m = RE_SECCION.search(linea)
        if m:
            p_raw = m.group(1).lower()
            c_raw = m.group(2).lower()
            p = MAP_PLANETA_ALT.get(p_raw)
            c = CASA_PATRONES.get(c_raw)
            if p and c:
                return p, c
        m = RE_NODO.search(linea)
        if m:
            c = CASA_PATRONES.get(m.group(2).lower())
            return MAP_NODO.get(m.group(1).lower()), c
        return None, None

    for linea in lineas:
        linea_strip = linea.strip()
        if not linea_strip:
            continue

        p, c = es_encabezado_valido(linea_strip)
        if p and c:
            guardar_seccion()
            key_actual = f"{p}_en_casa_{c}"
            buffer = [linea_strip]
            continue

        if key_actual:
            buffer.append(linea_strip)

    guardar_seccion()
    doc.close()
    return secciones


def generar_json(secciones, ruta_salida=None):
    if ruta_salida:
        with open(ruta_salida, 'w', encoding='utf-8') as f:
            json.dump(secciones, f, ensure_ascii=False, indent=2)
        print(f"Guardado: {ruta_salida} ({len(secciones)} entradas)")
    # Mostrar cobertura
    cubiertas = set()
    for k in secciones:
        partes = k.split('_en_casa_')
        if len(partes) == 2:
            cubiertas.add(k)
    print(f"Total entradas extraídas: {len(secciones)}")
    return secciones


def comparar_con_actuales(extraidas):
    """Compara con planetas_casas.json actual y muestra estadísticas."""
    with open('datos/planetas_casas.json', 'r', encoding='utf-8') as f:
        actuales = json.load(f)
    coinciden = 0
    mas_largas = 0
    for k, v_extraido in extraidas.items():
        if k in actuales:
            coinciden += 1
            if len(v_extraido) > len(actuales[k]):
                mas_largas += 1
    print(f"Coinciden con claves existentes: {coinciden}")
    print(f"De ellas, más largas que el original: {mas_largas}")
    print(f"Longitud media extraída: {sum(len(v) for v in extraidas.values()) / len(extraidas):.0f} chars")
    print(f"Longitud media actual: {sum(len(v) for v in actuales.values()) / len(actuales):.0f} chars")


if __name__ == "__main__":
    secciones = extraer_secciones(DOC_PATH)
    generar_json(secciones, "datos/planetas_casas_sasportas.json")
    comparar_con_actuales(secciones)
