from flatlib import const as flatlib_const

from src.core.calculador import (
    TRADUCCION_PLANETAS, TRADUCCION_SIGNOS, NOMBRES_SIGNOS,
    formatear_grados, obtener_casa_planeta,
    calcular_todos_los_planetas, clasificar_planetas
)
from src.core.interprete import (
    obtener_nombre_aspecto_manual, generar_aspectos, generar_sintesis
)


def generar_informe_final(carta, biblioteca, nombre="", fecha="", hora="", lat=0, lon=0, gmt=""):
    lineas = []

    lineas.append("=== INFORME ASTROLOGICO PROFESIONAL ===")
    lineas.append("")
    lineas.append("--- DATOS NATALES ---")
    lineas.append(f"Nombre: {nombre}")
    lineas.append(f"Fecha: {fecha} a las {hora} (UTC {gmt})")
    lineas.append(f"Coordenadas: {lat}, {lon}")
    lineas.append("")

    objetos_planetas = calcular_todos_los_planetas(carta)
    principales, nodos, asteroides = clasificar_planetas(objetos_planetas)

    lineas.append("--- ESTRUCTURA DE PERSONALIDAD ---")
    try:
        asc = carta.get(flatlib_const.ASC)
        mc = carta.get(flatlib_const.MC)
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

    lineas.append("--- CASAS EN SIGNOS ---")
    for i in range(1, 13):
        try:
            casa_obj = carta.get(f'House{i}')
            signo_idx = int(casa_obj.lon / 30)
            sig_en = NOMBRES_SIGNOS[signo_idx].lower()
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

    lineas.append("--- DINAMICAS INTERNAS (ASPECTOS) ---")
    aspectos = generar_aspectos(objetos_planetas, biblioteca)
    for asp in aspectos:
        lineas.append(f"- {asp['cuerpo1']} en {asp['tipo']} a {asp['cuerpo2']}: {asp['texto']}")

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

    lineas.append("# Informe Astrologico Profesional\n")
    lineas.append("## Datos Natales")
    lineas.append(f"- **Nombre:** {nombre}")
    lineas.append(f"- **Fecha:** {fecha} a las {hora} (UTC {gmt})")
    lineas.append(f"- **Coordenadas:** {lat}, {lon}\n")

    lineas.append("---\n")

    lineas.append("## Estructura de Personalidad")
    try:
        asc = carta.get(flatlib_const.ASC)
        mc = carta.get(flatlib_const.MC)
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
            sig_en = NOMBRES_SIGNOS[signo_idx].lower()
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
    aspectos = generar_aspectos(objetos_planetas, biblioteca)
    for asp in aspectos:
        lineas.append(f"- **{asp['cuerpo1']}** en {asp['tipo']} a **{asp['cuerpo2']}**: {asp['texto']}")

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
