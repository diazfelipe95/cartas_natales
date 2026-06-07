"""Importa contenido extraído de PDFs a los JSONs de datos/."""

import json
import os

RUTA_DATOS = "datos"


def importar_planetas_casas(extraido_path="datos/planetas_casas_sasportas.json"):
    """Reemplaza planetas_casas.json con el contenido extraído de Sasportas."""
    with open(extraido_path, 'r', encoding='utf-8') as f:
        extraido = json.load(f)

    ruta_destino = os.path.join(RUTA_DATOS, "planetas_casas.json")
    with open(ruta_destino, 'r', encoding='utf-8') as f:
        actual = json.load(f)

    # Reemplazar todas las claves que tienen nuevo contenido
    reemplazadas = 0
    conservadas = 0
    nuevas = 0
    for k, v in extraido.items():
        if k in actual:
            if len(v) > len(actual[k]):
                actual[k] = v
                reemplazadas += 1
            else:
                conservadas += 1
        else:
            actual[k] = v
            nuevas += 1

    with open(ruta_destino, 'w', encoding='utf-8') as f:
        json.dump(actual, f, ensure_ascii=False, indent=2)

    print(f"planetas_casas.json: {reemplazadas} reemplazadas, {conservadas} conservadas, {nuevas} nuevas")
    print(f"  Total: {len(actual)} entradas")

    # Estadísticas de longitud
    largos = sum(1 for v in actual.values() if len(v) > 100)
    print(f"  Textos largos (>100 chars): {largos}/{len(actual)}")

    return actual


def importar_planetas_signos(extraido_path="datos/planetas_signos_goodman.json"):
    """Importa contenido de Linda Goodman a planetas_signos.json y angulos_signos.json."""
    with open(extraido_path, 'r', encoding='utf-8') as f:
        extraido = json.load(f)

    # Importar a planetas_signos.json (claves: sol_en_*, luna_en_*)
    ruta_signos = os.path.join(RUTA_DATOS, "planetas_signos.json")
    with open(ruta_signos, 'r', encoding='utf-8') as f:
        actual_signos = json.load(f)

    signos_reemp = 0
    signos_nuevas = 0
    for k, v in extraido.items():
        if k.startswith(("sol_", "luna_")):
            if k in actual_signos:
                if len(v) > len(actual_signos[k]):
                    actual_signos[k] = v
                    signos_reemp += 1
            else:
                actual_signos[k] = v
                signos_nuevas += 1

    with open(ruta_signos, 'w', encoding='utf-8') as f:
        json.dump(actual_signos, f, ensure_ascii=False, indent=2)
    print(f"planetas_signos.json: {signos_reemp} reemplazadas, {signos_nuevas} nuevas")
    largos = sum(1 for v in actual_signos.values() if len(v) > 100)
    print(f"  Textos largos (>100 chars): {largos}/{len(actual_signos)}")

    # Importar a angulos_signos.json (claves: ascendente_en_*)
    ruta_angulos = os.path.join(RUTA_DATOS, "angulos_signos.json")
    with open(ruta_angulos, 'r', encoding='utf-8') as f:
        actual_angulos = json.load(f)

    angulos_reemp = 0
    angulos_nuevas = 0
    for k, v in extraido.items():
        if k.startswith("ascendente_"):
            if k in actual_angulos:
                if len(v) > len(actual_angulos[k]):
                    actual_angulos[k] = v
                    angulos_reemp += 1
            else:
                actual_angulos[k] = v
                angulos_nuevas += 1

    with open(ruta_angulos, 'w', encoding='utf-8') as f:
        json.dump(actual_angulos, f, ensure_ascii=False, indent=2)
    print(f"angulos_signos.json: {angulos_reemp} reemplazadas, {angulos_nuevas} nuevas")
    largos = sum(1 for v in actual_angulos.values() if len(v) > 100)
    print(f"  Textos largos (>100 chars): {largos}/{len(actual_angulos)}")

    return actual_signos, actual_angulos


def importar_aspectos(extraido_path="datos/aspectos_tompkins.json"):
    """Importa contenido de Sue Tompkins a aspectos.json."""
    with open(extraido_path, 'r', encoding='utf-8') as f:
        extraido = json.load(f)

    ruta_destino = os.path.join(RUTA_DATOS, "aspectos.json")
    with open(ruta_destino, 'r', encoding='utf-8') as f:
        actual = json.load(f)

    reemp = 0
    nuevas = 0
    for k, v in extraido.items():
        if k in actual:
            if len(v) > len(actual[k]):
                actual[k] = v
                reemp += 1
        else:
            actual[k] = v
            nuevas += 1

    with open(ruta_destino, 'w', encoding='utf-8') as f:
        json.dump(actual, f, ensure_ascii=False, indent=2)
    print(f"aspectos.json: {reemp} reemplazadas, {nuevas} nuevas")
    largos = sum(1 for v in actual.values() if len(v) > 100)
    print(f"  Textos largos (>100 chars): {largos}/{len(actual)}")

    return actual


if __name__ == "__main__":
    importar_planetas_casas()
    importar_planetas_signos()
    importar_aspectos()
