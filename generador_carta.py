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
        'casas_signos': 'datos/casas_signos.json'
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
    'Saturn': 'saturno', 'North Node': 'nodo_norte',
    'Chiron': 'quiron', 'Lilith': 'lilith',
    'Ceres': 'ceres', 'Pallas': 'pallas',
    'Juno': 'juno', 'Vesta': 'vesta'
}

# Signos opuestos para calcular el Nodo Sur manualmente
OPUESTOS = {
    'aries': 'libra', 'taurus': 'scorpio', 'gemini': 'sagittarius',
    'cancer': 'capricorn', 'leo': 'aquarius', 'virgo': 'pisces',
    'libra': 'aries', 'scorpio': 'taurus', 'sagittarius': 'gemini',
    'capricorn': 'cancer', 'aquarius': 'leo', 'pisces': 'virgo'
}




def obtener_nombre_aspecto_manual(distancia):
    """Calcula aspectos por distancia en grados (con un margen de error/orbe)."""
    # Orbe de 8 grados para conjunción y oposición, 6 para el resto
    if distancia < 8: return 'conjuncion'
    if 172 < distancia < 188: return 'oposicion'
    if 84 < distancia < 96: return 'cuadratura'
    if 114 < distancia < 126: return 'trigono'
    if 56 < distancia < 64: return 'sextil'
    return None






def generar_informe_final(carta, biblioteca):
    lineas = []
    lineas.append("=== INFORME ASTROLÓGICO PROFESIONAL ===\n")

    # --- 1. ÁNGULOS ---
    lineas.append("--- ESTRUCTURA DE PERSONALIDAD (ÁNGULOS) ---")
    try:
        asc = carta.get(const.ASC)
        mc = carta.get(const.MC)
        clave_asc = f"casa_1_{asc.sign.lower()}"
        clave_mc = f"casa_10_{mc.sign.lower()}"
        lineas.append(f"ASCENDENTE: {biblioteca['casas_signos'].get(clave_asc, f'En {asc.sign}')}")
        lineas.append(f"MEDIO CIELO: {biblioteca['casas_signos'].get(clave_mc, f'En {mc.sign}')}\n")
    except Exception as e:
        lineas.append(f"Nota: Hubo un detalle calculando los ángulos principales.\n")

    # --- 2. PLANETAS Y CASAS ---
    lineas.append("--- POSICIONES DE LOS PLANETAS ---")
    
    # IDs numéricos de la Swiss Ephemeris:
    # 0:Sol, 1:Luna, 2:Mercurio, 3:Venus, 4:Marte, 5:Jupiter, 6:Saturno, 10:NodoN
    # 15:Lilith, 17:Quiron, 18:Ceres, 19:Pallas, 20:Juno, 21:Vesta
    planetas_a_calcular = [
        (const.SUN, 0), (const.MOON, 1), (const.MERCURY, 2), 
        (const.VENUS, 3), (const.MARS, 4), (const.JUPITER, 5), 
        (const.SATURN, 6), (const.NORTH_NODE, 10),
        ('Chiron', 17), ('Lilith', 15), ('Ceres', 18), 
        ('Pallas', 19), ('Juno', 20), ('Vesta', 21)
    ]
    
    objetos_planetas = []
    jd = carta.date.jd

    for p_id, swe_id in planetas_a_calcular:
        p = None
        try:
            # 1. Intentar obtener planetas ESTÁNDAR mediante flatlib
            if swe_id <= 10:
                p = carta.get(p_id)
            
            # 2. Si es un ASTEROIDE o flatlib falla, forzamos Swiss Ephemeris
            if p is None:
                # Calculamos posición
                res = swe.calc_ut(jd, swe_id, 2)
                
                # EXTRACCIÓN TOTAL (Recursiva)
                # Esta función busca el primer número dentro de cualquier estructura
                def extraer_primer_numero(dato):
                    if isinstance(dato, (tuple, list)):
                        return extraer_primer_numero(dato[0])
                    return dato

                try:
                    lon_pura = float(extraer_primer_numero(res))
                except Exception as e:
                    print(f"⚠️ Error fatal convirtiendo dato en {p_id}: {e}")
                    continue
                
                from flatlib.object import GenericObject
                nombres_signos = [
                    'Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo',
                    'Libra', 'Scorpio', 'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces'
                ]
                
                p = GenericObject()
                p.id = str(p_id)
                p.lon = lon_pura
                p.sign = nombres_signos[int(lon_pura / 30)]
                p.signlon = lon_pura % 30

            if p:
                objetos_planetas.append(p)
                
        except Exception as e:
            # Imprime el error exacto para saber si es falta de archivos .se1 o de código
            print(f"⚠️ Error en {p_id} (ID: {swe_id}): {e}")
            continue
            
      
        
        id_real = getattr(p, 'id', str(p_id))
        n_es = TRADUCCION_PLANETAS.get(id_real, str(id_real).lower())
        sig_en_libreria = p.sign.lower() 
        sig_es = TRADUCCION_SIGNOS.get(sig_en_libreria, sig_en_libreria)
        
        # CÁLCULO DE CASA
        num_casa = "1"
        for i in range(1, 13):
            c_actual = carta.get(f'House{i}')
            sig_idx = 1 if i == 12 else i + 1
            c_siguiente = carta.get(f'House{sig_idx}')
            if c_actual.lon <= p.lon < c_siguiente.lon:
                num_casa = str(i)
                break
        
        if id_real == 'North Node':
            lineas.append("--- EJE DEL DESTINO (MISIÓN DE VIDA) ---")
            txt_nn = biblioteca['planetas_signos'].get(f"nodo_norte_en_{sig_es}", f"Misión en {sig_es.capitalize()}.")
            lineas.append(f"* NODO NORTE en {sig_es.capitalize()} (Casa {num_casa})")
            lineas.append(f"  Camino de evolución: {txt_nn}")
            
            sig_sur = OPUESTOS.get(sig_es, sig_es)
            num_casa_sur = int(num_casa) + 6
            if num_casa_sur > 12: num_casa_sur -= 12
            
            lineas.append(f"* NODO SUR en {sig_sur.capitalize()} (Casa {num_casa_sur})")
            lineas.append(f"  Zona de confort y talentos innatos: Lo que ya dominas pero debes transformar.\n")
        else:
            txt_sig = biblioteca['planetas_signos'].get(f"{n_es}_en_{sig_es}", "")
            txt_casa = biblioteca['planetas_casas'].get(f"{n_es}_en_casa_{num_casa}", "")
            
            lineas.append(f"* {n_es.upper()} en {sig_es.capitalize()} (Casa {num_casa})")
            if txt_sig: 
                lineas.append(f"  {txt_sig}")
            if txt_casa and f"Influencia en la casa {num_casa}" not in txt_casa:
                lineas.append(f"  {txt_casa}")
            lineas.append("")

    # --- 3. ASPECTOS MANUALES ---
    lineas.append("--- DINÁMICAS INTERNAS (ASPECTOS) ---")
    for i in range(len(objetos_planetas)):
        for j in range(i + 1, len(objetos_planetas)):
            p1, p2 = objetos_planetas[i], objetos_planetas[j]
            dist = abs(p1.lon - p2.lon)
            if dist > 180: dist = 360 - dist
            
            tipo = obtener_nombre_aspecto_manual(dist)
            if tipo:
                id1 = str(getattr(p1, 'id', p1))
                id2 = str(getattr(p2, 'id', p2))
                nom1 = TRADUCCION_PLANETAS.get(id1, id1).capitalize()
                nom2 = TRADUCCION_PLANETAS.get(id2, id2).capitalize()
                clave = f"{nom1.lower()}_{tipo}_{nom2.lower()}"
                txt = biblioteca['aspectos'].get(clave, f"Relación de {tipo} entre {nom1} y {nom2}.")
                lineas.append(f"- {nom1} en {tipo} a {nom2}: {txt}")

    return "\n".join(lineas)







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
        
        # 4. Generación del informe cruzando con tus JSON
        print("[Redactando informe personalizado...]")
        resultado_texto = generar_informe_final(carta_calculada, datos_interpretacion)
        
        # 5. Guardar el archivo con el nombre del usuario
        nombre_archivo = f"Carta_Natal_{nombre_usuario.replace(' ', '_')}.txt"
        with open(nombre_archivo, "w", encoding="utf-8") as salida:
            salida.write(f"CARTA NATAL DE: {nombre_usuario}\n")
            salida.write(f"Datos: {fecha} a las {hora} (UTC {gmt})\n")
            salida.write("="*40 + "\n\n")
            salida.write(resultado_texto)
        
        print(f"\n✅ ¡Éxito! Tu carta natal se ha guardado en: {nombre_archivo}")
        
    except Exception as error:
        print(f"\n❌ Ocurrió un error en el cálculo: {error}")
        print("Asegúrate de que el formato de fecha (AAAA/MM/DD) y hora (HH:MM) sea correcto.")

if __name__ == "__main__":
    iniciar_programa()