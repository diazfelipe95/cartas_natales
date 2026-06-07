import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src.core.calculador import (
    TRADUCCION_SIGNOS, TRADUCCION_PLANETAS, PLANETAS_CORE, NOMBRES_SIGNOS,
    longitud_entre, obtener_casa_planeta, formatear_grados,
    elemento_signo, modalidad_signo,
    calcular_carta_natal, calcular_todos_los_planetas, clasificar_planetas
)

from src.core.interprete import (
    cargar_biblioteca_json, orbe_para_objeto,
    obtener_nombre_aspecto_manual, generar_aspectos, generar_sintesis
)

from src.utils.renderers import (
    generar_informe_final, generar_informe_md, exportar_pdf
)

from main import iniciar_programa


if __name__ == "__main__":
    iniciar_programa()
