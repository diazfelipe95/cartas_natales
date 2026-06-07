from src.core.calculador import calcular_carta_natal
from src.core.interprete import cargar_biblioteca_json
from src.utils.renderers import generar_informe_final, generar_informe_md, exportar_pdf


def iniciar_programa():
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

    nombre_usuario = input("Introduce tu nombre: ")
    fecha = input("Fecha de nacimiento (AAAA/MM/DD): ")
    hora = input("Hora de nacimiento (HH:MM): ")

    print("\n--- Coordenadas Geograficas ---")
    print("Nota: Usa decimales (ej. Manizales es Lat: 5.06, Lon: -75.51)")
    lat = float(input("Introduce la Latitud: "))
    lon = float(input("Introduce la Longitud: "))

    print("\n--- Zona Horaria ---")
    print("Ejemplo: Colombia es -05:00, Espana es +01:00")
    gmt = input("Introduce tu zona horaria (UTC): ")

    try:
        print("\n[Calculando posiciones con las efemerides suizas...]")
        carta_calculada = calcular_carta_natal(fecha, hora, lat, lon, gmt)

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
            print(f"  {archivo}")

        elif fmt == "2":
            archivo = f"{base}.md"
            print("[Generando Markdown...]")
            contenido = generar_informe_md(carta_calculada, datos_interpretacion, nombre_usuario, fecha, hora, lat, lon, gmt)
            with open(archivo, "w", encoding="utf-8") as salida:
                salida.write(f"CARTA NATAL DE: {nombre_usuario}\n")
                salida.write(f"Datos: {fecha} a las {hora} (UTC {gmt})\n")
                salida.write("="*40 + "\n\n")
                salida.write(contenido)
            print(f"  {archivo}")

        elif fmt == "3":
            archivo = f"{base}.pdf"
            print("[Generando PDF...]")
            exportar_pdf(carta_calculada, datos_interpretacion, nombre_usuario, fecha, hora, lat, lon, gmt, archivo)
            print(f"  {archivo}")

    except Exception as error:
        print(f"\nOcurrio un error en el calculo: {error}")
        print("Asegurate de que el formato de fecha (AAAA/MM/DD) y hora (HH:MM) sea correcto.")


if __name__ == "__main__":
    iniciar_programa()
