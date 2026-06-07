import os
from flatlib import datetime, geopos, const
from flatlib.chart import Chart
from flatlib.object import GenericObject
import swisseph as swe


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

PLANETAS_CORE = {'Sun', 'Moon', 'Mercury', 'Venus', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto'}

NOMBRES_SIGNOS = [
    'Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo',
    'Libra', 'Scorpio', 'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces'
]


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


def calcular_carta_natal(fecha_str, hora_str, latitud, longitud, zona_horaria):
    ruta_base = os.path.dirname(os.path.abspath(__file__))
    ruta_efem = os.path.join(os.path.dirname(ruta_base), '..', 'efemerides')
    ruta_efem = os.path.normpath(ruta_efem)

    if os.path.exists(ruta_efem):
        swe.set_ephe_path(ruta_efem)
        print(f"Motor configurado en: {ruta_efem}")
    else:
        print(f"Alerta: No se encontro la carpeta de efemerides en: {ruta_efem}")

    fecha_calculo = datetime.Datetime(fecha_str, hora_str, zona_horaria)
    posicion_geo = geopos.GeoPos(latitud, longitud)
    carta = Chart(fecha_calculo, posicion_geo, hsys='Placidus')
    return carta


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
                p.sign = NOMBRES_SIGNOS[int(lon_pura / 30)]
                p.signlon = lon_pura % 30

            if p:
                objetos_planetas.append(p)
        except Exception as e:
            print(f"Error calculando {p_id}: {e}")

    for p in objetos_planetas:
        if str(getattr(p, 'id', '')) == 'North Node':
            lon_sur = (p.lon + 180) % 360
            sn = GenericObject()
            sn.id = 'South Node'
            sn.lon = lon_sur
            sn.sign = NOMBRES_SIGNOS[int(lon_sur / 30)]
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
