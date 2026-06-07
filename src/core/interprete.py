import os
import json


def cargar_biblioteca_json(ruta_base=None):
    if ruta_base is None:
        ruta_base = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'datos')
    else:
        ruta_base = os.path.join(ruta_base, 'datos')

    biblioteca = {}
    nombres_archivos = {
        'planetas_signos': 'planetas_signos.json',
        'planetas_casas': 'planetas_casas.json',
        'aspectos': 'aspectos.json',
        'casas_signos': 'casas_signos.json',
        'angulos_signos': 'angulos_signos.json'
    }

    for clave, nombre in nombres_archivos.items():
        ruta = os.path.join(ruta_base, nombre)
        if os.path.exists(ruta):
            with open(ruta, 'r', encoding='utf-8') as archivo:
                datos = json.load(archivo)
                biblioteca[clave] = datos.get(f"planetas_en_{clave.split('_')[-1]}", datos)
        else:
            print(f"Advertencia: No se encontro {ruta}. Se saltara esta seccion.")
            biblioteca[clave] = {}

    return biblioteca


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
    if distancia < orb:
        return 'conjuncion'
    if abs(distancia - 180) < orb:
        return 'oposicion'
    if abs(distancia - 90) < orb:
        return 'cuadratura'
    if abs(distancia - 120) < orb:
        return 'trino'
    if abs(distancia - 60) < orb:
        return 'sextil'
    return None


def generar_aspectos(objetos_planetas, biblioteca):
    from .calculador import TRADUCCION_PLANETAS, PLANETAS_CORE
    aspectos = []
    for i in range(len(objetos_planetas)):
        for j in range(i + 1, len(objetos_planetas)):
            p1, p2 = objetos_planetas[i], objetos_planetas[j]
            id1 = str(getattr(p1, 'id', ''))
            id2 = str(getattr(p2, 'id', ''))
            if id1 not in PLANETAS_CORE or id2 not in PLANETAS_CORE:
                continue
            dist = abs(p1.lon - p2.lon)
            if dist > 180:
                dist = 360 - dist
            tipo = obtener_nombre_aspecto_manual(dist, p1, p2)
            if tipo:
                nom1 = TRADUCCION_PLANETAS.get(id1, id1).capitalize()
                nom2 = TRADUCCION_PLANETAS.get(id2, id2).capitalize()
                clave = f"{nom1.lower()}_{tipo}_{nom2.lower()}"
                txt = biblioteca['aspectos'].get(clave, f"Relacion de {tipo} entre {nom1} y {nom2}.")
                aspectos.append({
                    'cuerpo1': nom1,
                    'cuerpo2': nom2,
                    'tipo': tipo,
                    'texto': txt,
                    'clave': clave
                })
    return aspectos


def generar_sintesis(objetos, carta):
    from .calculador import elemento_signo, modalidad_signo, obtener_casa_planeta

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
