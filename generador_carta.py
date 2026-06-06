import json
import os
from flatlib import datetime, geopos, const, props
from flatlib.chart import Chart
import swisseph as swe  # <--- Importación directa del motor


def cargar_biblioteca_json():
    """Carga todos los archivos de configuración y textos de interpretación."""
    biblioteca = {}
    nombres_archivos = {
        'planetas_signos': 'datos/planetas_signos.json',
        'planetas_casas': 'datos/planetas_casas.json',
        'aspectos': 'datos/aspectos.json',
        'casas_signos': 'datos/casas_signos.json',
        'angulos_signos': 'datos/angulos_signos.json'
    }
    
    for clave, nombre in nombres_archivos.items():
        if os.path.exists(nombre):
            with open(nombre, 'r', encoding='utf-8') as archivo:
                # Cargamos el contenido directamente en la clave correspondiente
                datos = json.load(archivo)
                # Si el JSON tiene una raíz como "planetas_en_signos", la extraemos
                biblioteca[clave] = datos.get(f"planetas_en_{clave.split('_')[-1]}", datos)
        else:
            print(f"Advertencia: No se encontró el archivo {nombre}. Se saltará esta sección.")
            biblioteca[clave] = {}
            
    return biblioteca





def calcular_carta_natal(fecha_str, hora_str, latitud, longitud, zona_horaria):
    """
    Realiza el cálculo astronómico de las posiciones.
    fecha_str: 'AAAA/MM/DD'
    hora_str: 'HH:MM'
    """
    """
    Realiza el cálculo astronómico de las posiciones.
    """
   # 1. Configurar la ruta a tu carpeta 'efemerides'
    # Usamos la ruta absoluta del archivo para evitar errores de "no encontrado"
    ruta_base = os.path.dirname(os.path.abspath(__file__))
    ruta_efem = os.path.join(ruta_base, 'efemerides')
    
    if os.path.exists(ruta_efem):
        # Esta línea configura las efemérides para todo el entorno de Python
        swe.set_ephe_path(ruta_efem)
        # PRUEBA ESTO:
        print(f"✅ Motor configurado en: {ruta_efem}")
    else:
        print(f"❌ Alerta: No se encontró la carpeta de efemérides en: {ruta_efem}")


    # 2. Lógica de cálculo
    fecha_calculo = datetime.Datetime(fecha_str, hora_str, zona_horaria)
    posicion_geo = geopos.GeoPos(latitud, longitud)
    # Creamos la carta usando el sistema de casas Placidus (común en astrología moderna)
    carta = Chart(fecha_calculo, posicion_geo, hsys='Placidus')
    return carta








def obtener_nombre_aspecto(id_aspecto):
    """Traduce los IDs internos de flatlib a tus claves de JSON."""
    mapeo = {
        const.CONJUNCTION: 'conjuncion',
        const.OPPOSITION: 'oposicion',
        const.SQUARE: 'cuadratura',
        const.TRINE: 'trigono',
        const.SEXTILE: 'sextil'
    }
    return mapeo.get(id_aspecto, 'aspecto')




# --- CONFIGURACIÓN DE TRADUCCIÓN ---


# Diccionario para corregir los signos de inglés a español (sin tildes como tus JSON)
TRADUCCION_SIGNOS = {
    'aries': 'aries', 'taurus': 'tauro', 'gemini': 'geminis',
    'cancer': 'cancer', 'leo': 'leo', 'virgo': 'virgo',
    'libra': 'libra', 'scorpio': 'escorpio', 'sagittarius': 'sagitario',
    'capricorn': 'capricornio', 'aquarius': 'acuario', 'pisces': 'piscis'
}



TRADUCCION_PLANETAS = {
    'Sun': 'sol', 'Moon': 'luna', 'Mercury': 'mercurio', 
    'Venus': 'venus', 'Mars': 'marte', 'Jupiter': 'jupiter', 
    'Saturn': 'saturno', 'Uranus': 'urano', 'Neptune': 'neptuno',
    'Pluto': 'pluton', 'North Node': 'nodo_norte',
    'South Node': 'nodo_sur',
    'Chiron': 'quiron', 'Lilith': 'lilith',
    'Ceres': 'ceres', 'Pallas': 'pallas',
    'Juno': 'juno', 'Vesta': 'vesta'
}




def orbe_para_objeto(obj):
    pid = str(getattr(obj, 'id', ''))
    if pid in ('Sun', 'Moon'):
        return 8
    if pid in ('North Node', 'South Node'):
        return 4
    if pid in ('Chiron', 'Lilith', 'Ceres', 'Pallas', 'Juno', 'Vesta'):
        return 3
    return 6


def obtener_nombre_aspecto_manual(distancia, obj1, obj2):
    orb = max(orbe_para_objeto(obj1), orbe_para_objeto(obj2))
    if distancia < orb: return 'conjuncion'
    if abs(distancia - 180) < orb: return 'oposicion'
    if abs(distancia - 90) < orb: return 'cuadratura'
    if abs(distancia - 120) < orb: return 'trigono'
    if abs(distancia - 60) < orb: return 'sextil'
    return None


def longitud_entre(valor, inicio, fin):
    if inicio <= fin:
        return inicio <= valor < fin
    return valor >= inicio or valor < fin


def obtener_casa_planeta(planeta, carta):
    for i in range(1, 13):
        actual = carta.get(f'House{i}')
        siguiente = carta.get(f'House{1 if i == 12 else i + 1}')
        if longitud_entre(planeta.lon, actual.lon, siguiente.lon):
            return i
    return 12


def calcular_todos_los_planetas(carta):
    objetos_planetas = []
    jd = carta.date.jd

    listado = [
        (const.SUN, 0), (const.MOON, 1), (const.MERCURY, 2),
        (const.VENUS, 3), (const.MARS, 4), (const.JUPITER, 5),
        (const.SATURN, 6), (const.URANUS, 7), (const.NEPTUNE, 8),
        (const.PLUTO, 9), (const.NORTH_NODE, 10),
        ('Chiron', 17), ('Lilith', 15), ('Ceres', 18),
        ('Pallas', 19), ('Juno', 20), ('Vesta', 21)
    ]

    from flatlib.object import GenericObject
    nombres_signos = [
        'Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo',
        'Libra', 'Scorpio', 'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces'
    ]

    for p_id, swe_id in listado:
        p = None
        try:
            if swe_id in (0, 1, 2, 3, 4, 5, 6, 10):
                p = carta.get(p_id)

            if p is None:
                res = swe.calc_ut(jd, swe_id, 2)
                def extraer_primer_numero(dato):
                    if isinstance(dato, (tuple, list)):
                        return extraer_primer_numero(dato[0])
                    return dato
                lon_pura = float(extraer_primer_numero(res))
                p = GenericObject()
                p.id = str(p_id)
                p.lon = lon_pura
                p.sign = nombres_signos[int(lon_pura / 30)]
                p.signlon = lon_pura % 30

            if p:
                objetos_planetas.append(p)
        except Exception as e:
            print(f"Error calculando {p_id}: {e}")

    # South Node from North Node
    for p in objetos_planetas:
        if str(getattr(p, 'id', '')) == 'North Node':
            lon_sur = (p.lon + 180) % 360
            sn = GenericObject()
            sn.id = 'South Node'
            sn.lon = lon_sur
            sn.sign = nombres_signos[int(lon_sur / 30)]
            sn.signlon = lon_sur % 30
            objetos_planetas.append(sn)
            break

    return objetos_planetas


def clasificar_planetas(objetos):
    principales = []
    nodos = []
    asteroides = []
    for p in objetos:
        pid = str(getattr(p, 'id', ''))
        if pid in ('North Node', 'South Node'):
            nodos.append(p)
        elif pid in ('Chiron', 'Lilith', 'Ceres', 'Pallas', 'Juno', 'Vesta'):
            asteroides.append(p)
        else:
            principales.append(p)
    return principales, nodos, asteroides


def formatear_grados(decimal):
    grados = int(decimal)
    minutos = round((decimal - grados) * 60)
    if minutos >= 60:
        grados += 1
        minutos = 0
    return f"{grados}°{minutos:02d}'"


def elemento_signo(signo_en):
    elementos = {
        'aries': 'fuego', 'leo': 'fuego', 'sagittarius': 'fuego',
        'tauro': 'tierra', 'virgo': 'tierra', 'capricorn': 'tierra',
        'gemini': 'aire', 'libra': 'aire', 'aquarius': 'aire',
        'cancer': 'agua', 'scorpio': 'agua', 'pisces': 'agua'
    }
    return elementos.get(signo_en.lower(), '')


def modalidad_signo(signo_en):
    modalidades = {
        'aries': 'cardinal', 'cancer': 'cardinal', 'libra': 'cardinal', 'capricorn': 'cardinal',
        'tauro': 'fijo', 'leo': 'fijo', 'scorpio': 'fijo', 'aquarius': 'fijo',
        'gemini': 'mutable', 'virgo': 'mutable', 'sagittarius': 'mutable', 'pisces': 'mutable'
    }
    return modalidades.get(signo_en.lower(), '')


def generar_sintesis(objetos, carta):
    elementos = {'fuego': 0, 'tierra': 0, 'aire': 0, 'agua': 0}
    modalidades = {'cardinal': 0, 'fijo': 0, 'mutable': 0}
    casas = {i: 0 for i in range(1, 13)}
    casas_angulares = {1, 4, 7, 10}

    for p in objetos:
        elem = elemento_signo(p.sign)
        if elem:
            elementos[elem] += 1
        mod = modalidad_signo(p.sign)
        if mod:
            modalidades[mod] += 1
        casa = obtener_casa_planeta(p, carta)
        casas[casa] = casas.get(casa, 0) + 1

    elem_dominante = max(elementos, key=elementos.get) if any(elementos.values()) else ''
    mod_dominante = max(modalidades, key=modalidades.get) if any(modalidades.values()) else ''

    traducir_elems = {'fuego': 'Fuego', 'tierra': 'Tierra', 'aire': 'Aire', 'agua': 'Agua'}
    traducir_mods = {'cardinal': 'Cardinal', 'fijo': 'Fijo', 'mutable': 'Mutable'}

    partes = []
    elem_txt = traducir_elems.get(elem_dominante, elem_dominante)
    mod_txt = traducir_mods.get(mod_dominante, mod_dominante)
    if elem_txt:
        partes.append(f"predominio del elemento {elem_txt}")
    if mod_txt:
        partes.append(f"modalidad {mod_txt}")

    angulares = [c for c in casas_angulares if casas.get(c, 0) > 0]
    if angulares:
        casas_str = ', '.join(f'Casa {c}' for c in sorted(angulares))
        ang_count = sum(1 for c in angulares for _ in range(casas[c]))
        partes.append(f"{ang_count} planeta(s) angular(es) en {casas_str}")

    casa_max = max(casas, key=casas.get) if any(casas.values()) else 0
    if casa_max and casas[casa_max] > 1:
        partes.append(f"concentracion en Casa {casa_max} ({casas[casa_max]} planetas)")

    if partes:
        return "Sintesis: " + "; ".join(partes) + "."
    return ""


def generar_informe_final(carta, biblioteca, nombre="", fecha="", hora="", lat=0, lon=0, gmt=""):
    lineas = []

    # --- DATOS NATALES ---
    lineas.append("=== INFORME ASTROLOGICO PROFESIONAL ===")
    lineas.append("")
    lineas.append("--- DATOS NATALES ---")
    lineas.append(f"Nombre: {nombre}")
    lineas.append(f"Fecha: {fecha} a las {hora} (UTC {gmt})")
    lineas.append(f"Coordenadas: {lat}, {lon}")
    lineas.append("")

    objetos_planetas = calcular_todos_los_planetas(carta)
    principales, nodos, asteroides = clasificar_planetas(objetos_planetas)

    nombres_signos = [
        'Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo',
        'Libra', 'Scorpio', 'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces'
    ]

    # --- 1. ESTRUCTURA DE PERSONALIDAD (ANGULOS) ---
    lineas.append("--- ESTRUCTURA DE PERSONALIDAD ---")
    try:
        asc = carta.get(const.ASC)
        mc = carta.get(const.MC)
        asc_es = TRADUCCION_SIGNOS.get(asc.sign.lower(), asc.sign.lower())
        mc_es = TRADUCCION_SIGNOS.get(mc.sign.lower(), mc.sign.lower())
        txt_asc = biblioteca['angulos_signos'].get(
            f"ascendente_en_{asc_es}",
            biblioteca['casas_signos'].get(f"casa_1_{asc_es}", f"En {asc.sign}")
        )
        txt_mc = biblioteca['angulos_signos'].get(
            f"medio_cielo_en_{mc_es}",
            biblioteca['casas_signos'].get(f"casa_10_{mc_es}", f"En {mc.sign}")
        )
        lineas.append(f"ASCENDENTE EN {asc_es.upper()} ({formatear_grados(asc.signlon)})")
        lineas.append(f"  {txt_asc}")
        lineas.append("")
        lineas.append(f"MEDIO CIELO EN {mc_es.upper()} ({formatear_grados(mc.signlon)})")
        lineas.append(f"  {txt_mc}")
        lineas.append("")
    except Exception:
        lineas.append("(No se pudieron calcular los angulos)")
        lineas.append("")

    # --- 2. CASAS EN SIGNOS ---
    lineas.append("--- CASAS EN SIGNOS ---")
    for i in range(1, 13):
        try:
            casa_obj = carta.get(f'House{i}')
            signo_idx = int(casa_obj.lon / 30)
            sig_en = nombres_signos[signo_idx].lower()
            sig_es = TRADUCCION_SIGNOS.get(sig_en, sig_en)
            txt = biblioteca['casas_signos'].get(f"casa_{i}_{sig_es}", "")
            grado_txt = formatear_grados(casa_obj.signlon if hasattr(casa_obj, 'signlon') else casa_obj.lon % 30)
            lineas.append(f"CASA {i} EN {sig_es.upper()} ({grado_txt})")
            if txt:
                lineas.append(f"  {txt}")
            lineas.append("")
        except Exception:
            lineas.append(f"CASA {i}: (no disponible)")
            lineas.append("")

    # --- 3. PLANETAS EN SIGNOS ---
    lineas.append("--- PLANETAS EN SIGNOS ---")
    for p in principales:
        pid = str(getattr(p, 'id', ''))
        n_es = TRADUCCION_PLANETAS.get(pid, pid.lower())
        sig_es = TRADUCCION_SIGNOS.get(p.sign.lower(), p.sign.lower())
        txt = biblioteca['planetas_signos'].get(f"{n_es}_en_{sig_es}", "")
        grado = formatear_grados(p.signlon if hasattr(p, 'signlon') else p.lon % 30)
        lineas.append(f"{n_es.upper()} EN {sig_es.upper()} ({grado})")
        if txt:
            lineas.append(f"  {txt}")
        lineas.append("")

    # --- 4. PLANETAS EN CASAS ---
    lineas.append("--- PLANETAS EN CASAS ---")
    for p in principales:
        pid = str(getattr(p, 'id', ''))
        n_es = TRADUCCION_PLANETAS.get(pid, pid.lower())
        casa = str(obtener_casa_planeta(p, carta))
        txt = biblioteca['planetas_casas'].get(f"{n_es}_en_casa_{casa}", "")
        grado = formatear_grados(p.signlon if hasattr(p, 'signlon') else p.lon % 30)
        sig_es = TRADUCCION_SIGNOS.get(p.sign.lower(), p.sign.lower())
        lineas.append(f"{n_es.upper()} EN CASA {casa} — {sig_es.capitalize()} {grado}")
        if txt:
            lineas.append(f"  {txt}")
        lineas.append("")

    # --- 5. MISION EVOLUTIVA ---
    lineas.append("--- MISION EVOLUTIVA ---")
    for p in nodos:
        pid = str(getattr(p, 'id', ''))
        n_es = TRADUCCION_PLANETAS.get(pid, pid.lower())
        sig_es = TRADUCCION_SIGNOS.get(p.sign.lower(), p.sign.lower())
        casa = str(obtener_casa_planeta(p, carta))
        prefijo = "nodo_norte" if pid == 'North Node' else "nodo_sur"

        txt_sig = biblioteca['planetas_signos'].get(f"{prefijo}_en_{sig_es}", "")
        txt_casa = biblioteca['planetas_casas'].get(f"{prefijo}_en_casa_{casa}", "")

        label = "NODO NORTE" if pid == 'North Node' else "NODO SUR"
        grado = formatear_grados(p.signlon if hasattr(p, 'signlon') else p.lon % 30)
        lineas.append(f"### {label}")
        lineas.append(f"{label} EN {sig_es.upper()} ({grado})")
        if txt_sig:
            lineas.append(f"  Por signo: {txt_sig}")
        lineas.append(f"{label} EN CASA {casa}")
        if txt_casa:
            lineas.append(f"  Por casa: {txt_casa}")
        lineas.append("")

    # --- 6. ASTEROIDES Y PUNTOS KARMICOS ---
    lineas.append("--- ASTEROIDES Y PUNTOS KARMICOS ---")
    for p in asteroides:
        pid = str(getattr(p, 'id', ''))
        n_es = TRADUCCION_PLANETAS.get(pid, pid.lower())
        sig_es = TRADUCCION_SIGNOS.get(p.sign.lower(), p.sign.lower())
        casa = str(obtener_casa_planeta(p, carta))
        txt_sig = biblioteca['planetas_signos'].get(f"{n_es}_en_{sig_es}", "")
        txt_casa = biblioteca['planetas_casas'].get(f"{n_es}_en_casa_{casa}", "")
        grado = formatear_grados(p.signlon if hasattr(p, 'signlon') else p.lon % 30)
        lineas.append(f"{n_es.upper()} EN {sig_es.upper()} ({grado}) — Casa {casa}")
        if txt_sig:
            lineas.append(f"  Signo: {txt_sig}")
        if txt_casa:
            lineas.append(f"  Casa: {txt_casa}")
        lineas.append("")

    # --- 7. DINAMICAS INTERNAS (ASPECTOS) ---
    lineas.append("--- DINAMICAS INTERNAS (ASPECTOS) ---")
    for i in range(len(objetos_planetas)):
        for j in range(i + 1, len(objetos_planetas)):
            p1, p2 = objetos_planetas[i], objetos_planetas[j]
            dist = abs(p1.lon - p2.lon)
            if dist > 180:
                dist = 360 - dist
            tipo = obtener_nombre_aspecto_manual(dist, p1, p2)
            if tipo:
                id1 = str(getattr(p1, 'id', ''))
                id2 = str(getattr(p2, 'id', ''))
                nom1 = TRADUCCION_PLANETAS.get(id1, id1).capitalize()
                nom2 = TRADUCCION_PLANETAS.get(id2, id2).capitalize()
                clave = f"{nom1.lower()}_{tipo}_{nom2.lower()}"
                txt = biblioteca['aspectos'].get(clave, f"Relacion de {tipo} entre {nom1} y {nom2}.")
                lineas.append(f"- {nom1} en {tipo} a {nom2}: {txt}")

    # --- 8. SINTESIS FINAL ---
    sintesis = generar_sintesis(objetos_planetas, carta)
    if sintesis:
        lineas.append("")
        lineas.append("--- SINTESIS FINAL ---")
        lineas.append(f"  {sintesis}")

    return "\n".join(lineas)


def generar_informe_md(carta, biblioteca, nombre="", fecha="", hora="", lat=0, lon=0, gmt=""):
    lineas = []

    objetos_planetas = calcular_todos_los_planetas(carta)
    principales, nodos, asteroides = clasificar_planetas(objetos_planetas)

    nombres_signos = [
        'Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo',
        'Libra', 'Scorpio', 'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces'
    ]

    lineas.append("# Informe Astrologico Profesional\n")
    lineas.append("## Datos Natales")
    lineas.append(f"- **Nombre:** {nombre}")
    lineas.append(f"- **Fecha:** {fecha} a las {hora} (UTC {gmt})")
    lineas.append(f"- **Coordenadas:** {lat}, {lon}\n")

    lineas.append("---\n")

    lineas.append("## Estructura de Personalidad")
    try:
        asc = carta.get(const.ASC)
        mc = carta.get(const.MC)
        asc_es = TRADUCCION_SIGNOS.get(asc.sign.lower(), asc.sign.lower())
        mc_es = TRADUCCION_SIGNOS.get(mc.sign.lower(), mc.sign.lower())
        txt_asc = biblioteca['angulos_signos'].get(
            f"ascendente_en_{asc_es}",
            biblioteca['casas_signos'].get(f"casa_1_{asc_es}", f"En {asc.sign}")
        )
        txt_mc = biblioteca['angulos_signos'].get(
            f"medio_cielo_en_{mc_es}",
            biblioteca['casas_signos'].get(f"casa_10_{mc_es}", f"En {mc.sign}")
        )
        lineas.append(f"**Ascendente en {asc_es.capitalize()}** ({formatear_grados(asc.signlon)})")
        lineas.append(f"  {txt_asc}\n")
        lineas.append(f"**Medio Cielo en {mc_es.capitalize()}** ({formatear_grados(mc.signlon)})")
        lineas.append(f"  {txt_mc}\n")
    except Exception:
        lineas.append("(No se pudieron calcular los angulos)\n")

    lineas.append("---\n")

    lineas.append("## Casas en Signos\n")
    for i in range(1, 13):
        try:
            casa_obj = carta.get(f'House{i}')
            signo_idx = int(casa_obj.lon / 30)
            sig_en = nombres_signos[signo_idx].lower()
            sig_es = TRADUCCION_SIGNOS.get(sig_en, sig_en)
            txt = biblioteca['casas_signos'].get(f"casa_{i}_{sig_es}", "")
            grado = formatear_grados(casa_obj.signlon if hasattr(casa_obj, 'signlon') else casa_obj.lon % 30)
            lineas.append(f"**Casa {i} en {sig_es.capitalize()}** ({grado})")
            if txt:
                lineas.append(f"  {txt}")
            lineas.append("")
        except Exception:
            lineas.append(f"**Casa {i}:** (no disponible)\n")

    lineas.append("---\n")

    lineas.append("## Planetas en Signos\n")
    for p in principales:
        pid = str(getattr(p, 'id', ''))
        n_es = TRADUCCION_PLANETAS.get(pid, pid.lower())
        sig_es = TRADUCCION_SIGNOS.get(p.sign.lower(), p.sign.lower())
        txt = biblioteca['planetas_signos'].get(f"{n_es}_en_{sig_es}", "")
        grado = formatear_grados(p.signlon if hasattr(p, 'signlon') else p.lon % 30)
        lineas.append(f"**{n_es.upper()} en {sig_es.capitalize()}** ({grado})")
        if txt:
            lineas.append(f"  {txt}")
        lineas.append("")

    lineas.append("---\n")

    lineas.append("## Planetas en Casas\n")
    for p in principales:
        pid = str(getattr(p, 'id', ''))
        n_es = TRADUCCION_PLANETAS.get(pid, pid.lower())
        casa = str(obtener_casa_planeta(p, carta))
        txt = biblioteca['planetas_casas'].get(f"{n_es}_en_casa_{casa}", "")
        grado = formatear_grados(p.signlon if hasattr(p, 'signlon') else p.lon % 30)
        sig_es = TRADUCCION_SIGNOS.get(p.sign.lower(), p.sign.lower())
        lineas.append(f"**{n_es.upper()} en Casa {casa}** &mdash; {sig_es.capitalize()} {grado}")
        if txt:
            lineas.append(f"  {txt}")
        lineas.append("")

    lineas.append("---\n")

    lineas.append("## Mision Evolutiva\n")
    for p in nodos:
        pid = str(getattr(p, 'id', ''))
        n_es = TRADUCCION_PLANETAS.get(pid, pid.lower())
        sig_es = TRADUCCION_SIGNOS.get(p.sign.lower(), p.sign.lower())
        casa = str(obtener_casa_planeta(p, carta))
        prefijo = "nodo_norte" if pid == 'North Node' else "nodo_sur"
        txt_sig = biblioteca['planetas_signos'].get(f"{prefijo}_en_{sig_es}", "")
        txt_casa = biblioteca['planetas_casas'].get(f"{prefijo}_en_casa_{casa}", "")
        label = "Nodo Norte" if pid == 'North Node' else "Nodo Sur"
        grado = formatear_grados(p.signlon if hasattr(p, 'signlon') else p.lon % 30)
        lineas.append(f"### {label}")
        lineas.append(f"**{label.upper()} en {sig_es.capitalize()}** ({grado})")
        if txt_sig:
            lineas.append(f"  *Por signo:* {txt_sig}")
        lineas.append(f"**{label.upper()} en Casa {casa}**")
        if txt_casa:
            lineas.append(f"  *Por casa:* {txt_casa}")
        lineas.append("")

    lineas.append("---\n")

    lineas.append("## Asteroides y Puntos Karmicos\n")
    for p in asteroides:
        pid = str(getattr(p, 'id', ''))
        n_es = TRADUCCION_PLANETAS.get(pid, pid.lower())
        sig_es = TRADUCCION_SIGNOS.get(p.sign.lower(), p.sign.lower())
        casa = str(obtener_casa_planeta(p, carta))
        txt_sig = biblioteca['planetas_signos'].get(f"{n_es}_en_{sig_es}", "")
        txt_casa = biblioteca['planetas_casas'].get(f"{n_es}_en_casa_{casa}", "")
        grado = formatear_grados(p.signlon if hasattr(p, 'signlon') else p.lon % 30)
        lineas.append(f"**{n_es.upper()} en {sig_es.capitalize()}** ({grado}) &mdash; Casa {casa}")
        if txt_sig:
            lineas.append(f"  *Signo:* {txt_sig}")
        if txt_casa:
            lineas.append(f"  *Casa:* {txt_casa}")
        lineas.append("")

    lineas.append("---\n")

    lineas.append("## Dinamicas Internas (Aspectos)\n")
    for i in range(len(objetos_planetas)):
        for j in range(i + 1, len(objetos_planetas)):
            p1, p2 = objetos_planetas[i], objetos_planetas[j]
            dist = abs(p1.lon - p2.lon)
            if dist > 180:
                dist = 360 - dist
            tipo = obtener_nombre_aspecto_manual(dist, p1, p2)
            if tipo:
                id1 = str(getattr(p1, 'id', ''))
                id2 = str(getattr(p2, 'id', ''))
                nom1 = TRADUCCION_PLANETAS.get(id1, id1).capitalize()
                nom2 = TRADUCCION_PLANETAS.get(id2, id2).capitalize()
                clave = f"{nom1.lower()}_{tipo}_{nom2.lower()}"
                txt = biblioteca['aspectos'].get(clave, f"Relacion de {tipo} entre {nom1} y {nom2}.")
                lineas.append(f"- **{nom1}** en {tipo} a **{nom2}**: {txt}")

    sintesis = generar_sintesis(objetos_planetas, carta)
    if sintesis:
        lineas.append("")
        lineas.append("---\n")
        lineas.append("## Sintesis Final")
        lineas.append(f"  {sintesis}")

    return "\n".join(lineas)


def exportar_pdf(carta, biblioteca, nombre, fecha, hora, lat, lon, gmt, archivo_salida):
    from fpdf import FPDF

    txt = generar_informe_final(carta, biblioteca, nombre, fecha, hora, lat, lon, gmt)

    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)

    ruta_font = '/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf'
    ruta_bold = '/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf'
    pdf.add_font('LibSans', '', ruta_font, uni=True)
    pdf.add_font('LibSans', 'B', ruta_bold, uni=True)

    pdf.set_font('LibSans', 'B', 18)
    pdf.cell(0, 12, 'INFORME ASTROLOGICO PROFESIONAL', align='C')
    pdf.ln(8)
    pdf.set_font('LibSans', '', 10)
    pdf.cell(0, 6, f'{nombre}  |  {fecha} a las {hora} (UTC {gmt})', align='C')
    pdf.ln(12)

    pdf.set_font('LibSans', '', 10)
    for linea in txt.split('\n'):
        if linea.startswith('=== ') and linea.endswith(' ==='):
            continue
        if linea.startswith('--- ') and linea.endswith(' ---'):
            seccion = linea.replace('--- ', '').replace(' ---', '')
            pdf.ln(3)
            pdf.set_font('LibSans', 'B', 14)
            pdf.cell(0, 8, seccion)
            pdf.ln(7)
            pdf.set_font('LibSans', '', 10)
        elif linea.startswith('### '):
            pdf.ln(2)
            pdf.set_font('LibSans', 'B', 11)
            pdf.cell(0, 7, linea.replace('### ', ''))
            pdf.ln(6)
            pdf.set_font('LibSans', '', 10)
        elif linea.strip():
            pdf.multi_cell(0, 5.5, linea.strip())
            pdf.ln(1)
        else:
            pdf.ln(2)

    pdf.output(archivo_salida)


def iniciar_programa():
    # 1. Cargar la biblioteca de textos
    datos_interpretacion = cargar_biblioteca_json()
    
    print("""
            #####
        ######
     ########
   ########             *
  ########
 #########
 #########     *
#########
#########
#########                  *
 ########
  #########      *
   ########
    ########
      ########          *
         ######
             #####
""")
    
    # 2. Entrada de datos interactiva
    nombre_usuario = input("Introduce tu nombre: ")
    fecha = input("Fecha de nacimiento (AAAA/MM/DD): ")
    hora = input("Hora de nacimiento (HH:MM): ")
    
    print("\n--- Coordenadas Geográficas ---")
    print("Nota: Usa decimales (ej. Manizales es Lat: 5.06, Lon: -75.51)")
    lat = float(input("Introduce la Latitud: "))
    lon = float(input("Introduce la Longitud: "))
    
    print("\n--- Zona Horaria ---")
    print("Ejemplo: Colombia es -05:00, España es +01:00")
    gmt = input("Introduce tu zona horaria (UTC): ")
    
    try:
        # 3. Procesamiento astronómico
        print("\n[Calculando posiciones con las efemérides suizas...]")
        carta_calculada = calcular_carta_natal(fecha, hora, lat, lon, gmt)
        
        # 4. Formato de salida
        print("\n--- Formato de salida ---")
        print("1: TXT (texto plano)")
        print("2: Markdown")
        print("3: PDF")
        fmt = input("Elige el formato (1/2/3) [1]: ").strip() or "1"

        base = f"Carta_Natal_{nombre_usuario.replace(' ', '_')}"

        if fmt == "1":
            archivo = f"{base}.txt"
            print("[Generando TXT...]")
            contenido = generar_informe_final(carta_calculada, datos_interpretacion, nombre_usuario, fecha, hora, lat, lon, gmt)
            with open(archivo, "w", encoding="utf-8") as salida:
                salida.write(f"CARTA NATAL DE: {nombre_usuario}\n")
                salida.write(f"Datos: {fecha} a las {hora} (UTC {gmt})\n")
                salida.write("="*40 + "\n\n")
                salida.write(contenido)
            print(f"  ✅ {archivo}")

        elif fmt == "2":
            archivo = f"{base}.md"
            print("[Generando Markdown...]")
            contenido = generar_informe_md(carta_calculada, datos_interpretacion, nombre_usuario, fecha, hora, lat, lon, gmt)
            with open(archivo, "w", encoding="utf-8") as salida:
                salida.write(f"CARTA NATAL DE: {nombre_usuario}\n")
                salida.write(f"Datos: {fecha} a las {hora} (UTC {gmt})\n")
                salida.write("="*40 + "\n\n")
                salida.write(contenido)
            print(f"  ✅ {archivo}")

        elif fmt == "3":
            archivo = f"{base}.pdf"
            print("[Generando PDF...]")
            exportar_pdf(carta_calculada, datos_interpretacion, nombre_usuario, fecha, hora, lat, lon, gmt, archivo)
            print(f"  ✅ {archivo}")
        
    except Exception as error:
        print(f"\n❌ Ocurrió un error en el cálculo: {error}")
        print("Asegúrate de que el formato de fecha (AAAA/MM/DD) y hora (HH:MM) sea correcto.")

if __name__ == "__main__":
    iniciar_programa()