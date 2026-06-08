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
        return 'conjunción'
    if abs(distancia - 180) < orb:
        return 'oposición'
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
                txt = biblioteca['aspectos'].get(clave, f"Relación de {tipo} entre {nom1} y {nom2}.")
                aspectos.append({
                    'cuerpo1': nom1,
                    'cuerpo2': nom2,
                    'tipo': tipo,
                    'texto': txt,
                    'clave': clave
                })
    return aspectos


def generar_sintesis(objetos, carta):
    from .calculador import TRADUCCION_PLANETAS, elemento_signo, modalidad_signo, obtener_casa_planeta

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
    desc_elems = {
        'fuego': 'la accion, la iniciativa y la capacidad de inspirar',
        'tierra': 'la solidez, la paciencia y la construcción concreta',
        'aire': 'la comunicación, las ideas y las relaciones sociales',
        'agua': 'la emoción, la intuición y la profundidad psicológica'
    }
    desc_mods = {
        'cardinal': 'iniciativa y capacidad de iniciar ciclos',
        'fijo': 'determinación, resistencia y profundidad',
        'mutable': 'adaptabilidad, versatilidad y capacidad de cambio'
    }
    desc_casa = {
        1: 'la identidad y la autoafirmación',
        2: 'los valores y la seguridad material',
        3: 'la comunicación y el entorno cercano',
        4: 'las raices y la vida emocional',
        5: 'la creatividad, el placer y el amor',
        6: 'el trabajo, la salud y el servicio',
        7: 'las relaciones y las asociaciones',
        8: 'la transformación y los recursos compartidos',
        9: 'la filosofia y la expansion',
        10: 'la vocación y la proyección pública',
        11: 'los grupos y los ideales',
        12: 'el inconsciente y la trascendencia'
    }

    partes = []
    elem_txt = traducir_elems.get(elem_dominante, elem_dominante)
    mod_txt = traducir_mods.get(mod_dominante, mod_dominante)
    elem_desc = desc_elems.get(elem_dominante, '')
    mod_desc = desc_mods.get(mod_dominante, '')

    # Paragraph 1: Elemental + modal makeup
    if elem_txt and mod_txt:
        par1 = (
            f"Esta carta revela un predominio del elemento {elem_txt}, lo que imprime una tendencia hacia "
            f"{elem_desc}. La modalidad {mod_txt} aporta {mod_desc}, sugiriendo que la persona procesa la "
            f"experiencia con {mod_desc}."
        )
        partes.append(par1)
    elif elem_txt:
        partes.append(f"El elemento {elem_txt} domina esta carta, orientando la personalidad hacia {elem_desc}.")

    # Paragraph 2: Angular emphasis
    angulares = [c for c in casas_angulares if casas.get(c, 0) > 0]
    if angulares:
        casas_str = ', '.join(f'Casa {c}' for c in sorted(angulares))
        ang_count = sum(casas[c] for c in angulares)
        ang_desc = ', '.join(desc_casa[c] for c in sorted(angulares))
        par2 = (
            f"La presencia de {ang_count} planeta(s) en casas angulares ({casas_str}) señala que las áreas "
            f"de {ang_desc} son ejes centrales en la vida del nativo. Estas casas representan los pilares "
            f"de la personalidad y la proyección pública, indicando que la persona está llamada a desarrollar "
            f"estos temas de manera consciente y visible."
        )
        partes.append(par2)

    # Paragraph 3: House concentration
    casa_max = max(casas, key=casas.get) if any(casas.values()) else 0
    if casa_max and casas[casa_max] > 1:
        focus_txt = desc_casa.get(casa_max, f'la Casa {casa_max}')
        par3 = (
            f"La Casa {casa_max} concentra {casas[casa_max]} planetas, convirtiéndola en el eje de mayor "
            f"densidad energética del tema astral. La vida del nativo gravita en torno a {focus_txt}, y es "
            f"en este terreno donde se juegan sus principales desafíos evolutivos y donde puede encontrar "
            f"su mayor fuente de realización. La integración consciente de esta concentración planetaria "
            f"es clave para el desarrollo personal."
        )
        partes.append(par3)

    # Paragraph 4: Closing integration
    if elem_txt and mod_txt:
        par4 = (
            f"En conjunto, esta configuración describe a una persona cuya naturaleza {elem_txt.lower()} "
            f"se expresa a través de la modalidad {mod_txt.lower()}, creando un perfil donde la {elem_desc} "
            f"se manifiesta con {mod_desc}. La clave evolutiva está en armonizar estas energías para que "
            f"trabajen en sinergia, permitiendo que el propósito de vida se despliegue con plenitud."
        )
        partes.append(par4)
    elif elem_txt:
        partes.append(
            f"La clave evolutiva de esta carta está en canalizar la energía del elemento {elem_txt.lower()} "
            f"de manera consciente, integrando sus luces y sombras para que el propósito de vida se "
            f"despliegue con plenitud."
        )

    if partes:
        return "\n\n".join(partes)
    return ""
