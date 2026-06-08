#!/usr/bin/env python3
"""Corrige tildes faltantes en los 5 JSONs de interpretación astrológica.

Enfoque: reemplazos seguros y no ambiguos.
- Terminaciones -cion → -ción, -sion → -sión (100% seguras)
- Palabras específicas con corrección inequívoca (esdrújulas, graves con hiato)
- No toca diacríticos ambiguos (tu/tú, el/él, esta/está, mas/más)
"""

import json
import re
import os
import sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILES = [
    "datos/angulos_signos.json",
    "datos/casas_signos.json",
    "datos/planetas_signos.json",
    "datos/planetas_casas.json",
    "datos/aspectos.json",
]

# Palabras completas que requieren tilde (con bordes de palabra)
# Solo incluye casos NO AMBIGUOS en contexto astrológico
REEMPLAZOS = {
    # Graves terminadas en vocal con hiato (tilde en i débil)
    r'\bdesafio\b': 'desafío',
    r'\bdesafios\b': 'desafíos',
    r'\bexito\b': 'éxito',
    r'\bexitos\b': 'éxitos',
    r'\bmaestria\b': 'maestría',
    r'\bmaestrias\b': 'maestrías',
    r'\bvalentia\b': 'valentía',
    r'\balegria\b': 'alegría',
    r'\benergia\b': 'energía',
    r'\benergias\b': 'energías',
    # 'arquitectura' correcta sin tilde (grave terminada en vocal)
    r'\barmonia\b': 'armonía',
    r'\bsabiduria\b': 'sabiduría',
    r'\bfantasia\b': 'fantasía',
    r'\bintuicion\b': 'intuición',

    # Esdrújulas
    r'\banalisis\b': 'análisis',
    r'\bfacil\b': 'fácil',
    r'\bfaciles\b': 'fáciles',
    r'\bdificil\b': 'difícil',
    r'\bdificiles\b': 'difíciles',
    r'\bunico\b': 'único',
    r'\bunica\b': 'única',
    r'\bunicos\b': 'únicos',
    r'\bunicas\b': 'únicas',
    r'\bintimo\b': 'íntimo',
    r'\bintima\b': 'íntima',
    r'\bintimos\b': 'íntimos',
    r'\bintimas\b': 'íntimas',
    r'\bcomodo\b': 'cómodo',
    r'\bcomoda\b': 'cómoda',
    r'\bcomodos\b': 'cómodos',
    r'\bcomodas\b': 'cómodas',
    r'\brapido\b': 'rápido',
    r'\brapida\b': 'rápida',
    r'\brapidos\b': 'rápidos',
    r'\brapidas\b': 'rápidas',
    r'\bexotico\b': 'exótico',
    r'\bexotica\b': 'exótica',
    r'\bproximo\b': 'próximo',
    r'\bproxima\b': 'próxima',
    r'\bproximos\b': 'próximos',
    r'\bproximas\b': 'próximas',
    r'\bultimo\b': 'último',
    r'\bultima\b': 'última',
    r'\bultimos\b': 'últimos',
    r'\bultimas\b': 'últimas',
    r'\bsimbolo\b': 'símbolo',
    r'\bsimbolos\b': 'símbolos',
    r'\bpractico\b': 'práctico',
    r'\bpractica\b': 'práctica',
    r'\bpracticos\b': 'prácticos',
    r'\bpracticas\b': 'prácticas',
    r'\bpublico\b': 'público',
    r'\bpublica\b': 'pública',
    r'\bpublicos\b': 'públicos',
    r'\bpublicas\b': 'públicas',
    r'\btipico\b': 'típico',
    r'\btipica\b': 'típica',
    r'\btipicos\b': 'típicos',
    r'\btipicas\b': 'típicas',
    r'\bcaracter\b': 'carácter',
    r'\bcientifico\b': 'científico',
    r'\bcientifica\b': 'científica',
    r'\bpractico\b': 'práctico',
    r'\bautomatico\b': 'automático',
    r'\bautomatica\b': 'automática',
    r'\bdomestico\b': 'doméstico',
    r'\bdomestica\b': 'doméstica',
    r'\bsintesis\b': 'síntesis',
    r'\bhipotesis\b': 'hipótesis',
    r'\bparalisis\b': 'parálisis',
    r'\bcrisis\b': 'crisis',
    r'\bdiabetes\b': 'diabetes',

    # Sobresdrújulas
    r'\bdigamelo\b': 'dígamelo',

    # Verbos condicionales (-ía) y otros que requieren tilde
    r'\bpodria\b': 'podría',
    r'\bpodrias\b': 'podrías',
    r'\bpodrian\b': 'podrían',
    r'\bpodriamos\b': 'podríamos',
    r'\bdeberia\b': 'debería',
    r'\bdeberias\b': 'deberías',
    r'\bdeberian\b': 'deberían',
    r'\btendria\b': 'tendría',
    r'\btendrias\b': 'tendrías',
    r'\btendrian\b': 'tendrían',
    r'\btendriamos\b': 'tendríamos',
    r'\bhabria\b': 'habría',
    r'\bhabrias\b': 'habrías',
    r'\bhabrian\b': 'habrían',
    r'\bqueria\b': 'quería',
    r'\bquerias\b': 'querías',
    r'\bquerian\b': 'querían',
    r'\bvenia\b': 'venía',
    r'\bvenian\b': 'venían',
    r'\btenia\b': 'tenía',
    r'\btenian\b': 'tenían',
    # 'hacia' omitido: ambiguo (preposición sin tilde vs verbo con tilde)
    r'\bdecia\b': 'decía',
    r'\bdecian\b': 'decían',
    r'\bsentia\b': 'sentía',
    r'\bsentian\b': 'sentían',
    r'\bvia\b': 'vía',
    r'\bvian\b': 'vían',
    r'\beconomia\b': 'economía',
    r'\bconocia\b': 'conocía',
    r'\bconocian\b': 'conocían',
    r'\brecibia\b': 'recibía',
    r'\brecibian\b': 'recibían',
    r'\bseguia\b': 'seguía',
    r'\bseguian\b': 'seguían',
    r'\bhibrido\b': 'híbrido',
    r'\bhibrida\b': 'híbrida',
    r'\bperiodo\b': 'período',
    r'\bpatetico\b': 'patético',
    r'\bpatetica\b': 'patética',
    r'\bexcentrico\b': 'excéntrico',
    r'\bexcentrica\b': 'excéntrica',
    r'\bpesimo\b': 'pésimo',
    r'\bpesima\b': 'pésima',
    r'\boptimo\b': 'óptimo',
    r'\boptima\b': 'óptima',
    r'\bmaximo\b': 'máximo',
    r'\bmaxima\b': 'máxima',
    r'\bminimo\b': 'mínimo',
    r'\bminima\b': 'mínima',
    r'\btorax\b': 'tórax',
    r'\btoracico\b': 'torácico',
    r'\btoracica\b': 'torácica',
    r'\bmusculo\b': 'músculo',
    r'\bmusculos\b': 'músculos',
    r'\bproposito\b': 'propósito',
    r'\bpropositos\b': 'propósitos',
    r'\bfenomeno\b': 'fenómeno',
    r'\bfenomenos\b': 'fenómenos',
    r'\bregimen\b': 'régimen',
    r'\bregimenes\b': 'regímenes',
    r'\bdinamico\b': 'dinámico',
    r'\bdinamica\b': 'dinámica',
    r'\bdinamicos\b': 'dinámicos',
    r'\bdinamicas\b': 'dinámicas',
    r'\beclectico\b': 'ecléctico',
    r'\beclectica\b': 'ecléctica',
    r'\bautentico\b': 'auténtico',
    r'\bautentica\b': 'auténtica',
    r'\bautenticos\b': 'auténticos',
    r'\bautenticas\b': 'auténticas',
    r'\bestimulo\b': 'estímulo',
    r'\bestimulos\b': 'estímulos',
    r'\bvocacion\b': 'vocación',
    r'\bvocacional\b': 'vocacional',

    # Agudas terminadas en -n que requieren tilde
    r'\btambien\b': 'también',
    r'\balguien\b': 'alguien',
}

# Compilamos las expresiones regulares
PAREJAS = [(re.compile(patron, re.IGNORECASE), reemplazo)
           for patron, reemplazo in REEMPLAZOS.items()]


def corregir_terminaciones_cion_sion(texto):
    """Corrige -cion → -ción y -sion → -sión al final de palabra."""
    patrones = [
        (re.compile(r'\b(\w+)cion\b'), r'\1ción'),
        (re.compile(r'\b(\w+)sion\b'), r'\1sión'),
    ]
    for patron, reemplazo in patrones:
        texto = patron.sub(reemplazo, texto)
    return texto


def corregir_palabras(texto):
    """Aplica reemplazos de palabras completas."""
    for patron, reemplazo in PAREJAS:
        # Solo reemplaza si la palabra sin tilde no es ya la palabra con tilde
        texto = patron.sub(reemplazo, texto)
    return texto


def procesar_valor(valor):
    """Corrige tildes en un valor string."""
    valor = corregir_terminaciones_cion_sion(valor)
    valor = corregir_palabras(valor)
    return valor


def recorrer_y_corregir(obj):
    """Recorre recursivamente un JSON y corrige tildes en strings."""
    if isinstance(obj, str):
        return procesar_valor(obj)
    elif isinstance(obj, dict):
        return {k: recorrer_y_corregir(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [recorrer_y_corregir(v) for v in obj]
    return obj


def main():
    total_reemplazos = 0
    for ruta_rel in FILES:
        ruta = os.path.join(BASE, ruta_rel)
        if not os.path.exists(ruta):
            print(f"⚠  No encontrado: {ruta_rel}")
            continue

        with open(ruta, 'r', encoding='utf-8') as f:
            contenido = f.read()

        # Contar ocurrencias de palabras sin tilde ANTES
        conteo_antes = 0
        for patron_str in REEMPLAZOS:
            conteo_antes += len(re.findall(patron_str, contenido, re.IGNORECASE))
        # También -cion/-sion
        conteo_antes += len(re.findall(r'\b\w+cion\b', contenido))
        conteo_antes += len(re.findall(r'\b\w+sion\b', contenido))

        datos = json.loads(contenido)
        datos_corregidos = recorrer_y_corregir(datos)

        with open(ruta, 'w', encoding='utf-8') as f:
            json.dump(datos_corregidos, f, ensure_ascii=False, indent=2)

        # Contar ocurrencias DESPUÉS
        contenido_nuevo = json.dumps(datos_corregidos, ensure_ascii=False, indent=2)
        conteo_despues = 0
        for patron_str in REEMPLAZOS:
            conteo_despues += len(re.findall(patron_str, contenido_nuevo, re.IGNORECASE))
        conteo_despues += len(re.findall(r'\b\w+cion\b', contenido_nuevo))
        conteo_despues += len(re.findall(r'\b\w+sion\b', contenido_nuevo))

        corregidos = conteo_antes - conteo_despues
        total_reemplazos += corregidos
        print(f"  {ruta_rel:35s} {corregidos:4d} correcciones aplicadas")

    print(f"\n✓ Total: {total_reemplazos} correcciones en {len(FILES)} archivos")


if __name__ == '__main__':
    main()
