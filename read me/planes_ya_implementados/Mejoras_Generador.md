# Mejoras Propuestas para el Generador de Cartas Natales

## Objetivo General

Transformar el generador actual en un sistema más robusto, modular y cercano a los estándares utilizados por programas profesionales de astrología.

Los objetivos principales son:

* Corregir errores potenciales en el cálculo de casas.
* Incorporar completamente los planetas modernos.
* Separar claramente las distintas capas interpretativas.
* Mejorar la legibilidad del informe final.
* Facilitar futuras ampliaciones mediante archivos JSON.

---

# Problemas Detectados en la Versión Actual

## 1. Cálculo de casas vulnerable

Actualmente se utiliza una comparación directa:

```python
if c_actual.lon <= p.lon < c_siguiente.lon:
```

Este método puede fallar cuando una casa cruza los 0° de Aries.

Ejemplo:

* Casa 12: 350°
* Casa 1: 10°

Un planeta situado en 355° pertenece a esa zona, pero la condición anterior puede no detectarlo correctamente.

## Solución

Implementar:

```python
def longitud_entre(valor, inicio, fin):

    if inicio <= fin:
        return inicio <= valor < fin

    return valor >= inicio or valor < fin
```

y posteriormente:

```python
def obtener_casa_planeta(planeta, carta):

    for i in range(1, 13):

        actual = carta.get(f'House{i}')

        siguiente_num = 1 if i == 12 else i + 1

        siguiente = carta.get(f'House{siguiente_num}')

        if longitud_entre(
            planeta.lon,
            actual.lon,
            siguiente.lon
        ):
            return i

    return 12
```

---

# Inclusión de Planetas Modernos

Actualmente el sistema omite:

* Urano
* Neptuno
* Plutón

Deben añadirse:

```python
(const.URANUS, 7)
(const.NEPTUNE, 8)
(const.PLUTO, 9)
```

También actualizar:

```python
TRADUCCION_PLANETAS
```

agregando:

```python
'Uranus': 'urano'
'Neptune': 'neptuno'
'Pluto': 'pluton'
```

---

# Organización Recomendada del Informe

Actualmente se mezclan signo y casa en una misma interpretación.

Ejemplo actual:

SOL en Virgo (Casa 6)

Interpretación signo.
Interpretación casa.

Esto dificulta la lectura.

---

# Nueva Estructura Recomendada

## DATOS NATALES

Nombre

Fecha

Hora

Coordenadas

Zona Horaria

---

## ESTRUCTURA DE PERSONALIDAD

### Ascendente

ASCENDENTE EN ARIES

Interpretación del Ascendente.

### Medio Cielo

MEDIO CIELO EN CAPRICORNIO

Interpretación del Medio Cielo.

---

## CASAS EN SIGNOS

CASA 1 EN ARIES

Interpretación.

CASA 2 EN TAURO

Interpretación.

...

CASA 12 EN PISCIS

Interpretación.

---

## PLANETAS EN SIGNOS

SOL EN VIRGO

Interpretación del Sol en Virgo.

LUNA EN PISCIS

Interpretación de la Luna en Piscis.

MERCURIO EN LIBRA

Interpretación.

...

---

## PLANETAS EN CASAS

SOL EN CASA 6

Interpretación de Sol Casa 6.

LUNA EN CASA 1

Interpretación de Luna Casa 1.

...

---

## MISIÓN EVOLUTIVA

### Nodo Norte

NODO NORTE EN LIBRA

Interpretación por signo.

NODO NORTE EN CASA 7

Interpretación por casa.

### Nodo Sur

NODO SUR EN ARIES

Interpretación complementaria.

---

## ASTEROIDES Y PUNTOS KÁRMICOS

QUIRÓN

LILITH

CERES

PALLAS

JUNO

VESTA

Cada uno con:

* Signo
* Casa
* Interpretación del signo
* Interpretación de la casa

---

## DINÁMICAS INTERNAS (ASPECTOS)

Listado de aspectos.

Ejemplo:

* Sol oposición Luna
* Sol conjunción Venus
* Marte conjunción Nodo Norte

---

## SÍNTESIS FINAL

Sección automática de resumen.

Debe identificar:

* Elemento dominante.
* Modalidad dominante.
* Planetas angulares.
* Concentraciones por casas.
* Aspectos más importantes.

Ejemplo:

"La carta presenta un fuerte énfasis en Virgo y la Casa 6, indicando una personalidad orientada al servicio, la mejora continua y el trabajo práctico."

---

# Mejoras en la Biblioteca JSON

## Estructura Actual

Ya existen:

* planetas_signos.json
* planetas_casas.json
* aspectos.json
* casas_signos.json

---

## Recomendación

Agregar:

### angulos_signos.json

Ejemplo:

```json
{
  "ascendente_en_aries": "...",
  "ascendente_en_tauro": "...",
  "medio_cielo_en_capricornio": "..."
}
```

Esto permite interpretaciones específicas para:

* Ascendente.
* Medio Cielo.

Sin reutilizar textos genéricos de casas.

---

# Aspectos Astrológicos

Actualmente:

* Conjunción
* Oposición
* Cuadratura
* Trígono
* Sextil

---

## Futuras mejoras

Añadir:

* Quincuncio (150°)
* Semisextil (30°)
* Semicuadratura (45°)
* Sesquicuadratura (135°)

---

# Orbes

Actualmente todos los aspectos usan prácticamente el mismo margen.

Recomendación:

## Luminarias

Sol y Luna:

8°

## Planetas

6°

## Asteroides

3°

## Puntos sensibles

2°

Esto reducirá falsos aspectos.

---

# Nodo Sur

Actualmente se calcula mediante:

```python
num_casa_sur = int(num_casa) + 6
```

Esto es una simplificación.

En una futura versión debería calcularse:

1. Longitud exacta del Nodo Sur.
2. Determinar la casa real usando el algoritmo general.

---

# Mejoras Futuras

## Retrogradaciones

Mostrar:

* Mercurio Retrógrado
* Venus Retrógrado
* Marte Retrógrado
* etc.

---

## Grados Exactos

Mostrar:

Ejemplo:

```text
SOL
Virgo 15°23'
Casa 6
```

---

## Cúspides

Mostrar:

```text
Casa 1: Aries 6°12'
Casa 2: Tauro 11°44'
Casa 3: Géminis 18°10'
...
```

---

## Exportación Profesional

Generar:

* TXT
* Markdown
* PDF

con la misma estructura.

---

# Prioridad de Implementación

## Prioridad Alta

1. Corregir cálculo de casas.
2. Añadir Urano, Neptuno y Plutón.
3. Separar planetas en signos y planetas en casas.
4. Mostrar signo del Ascendente y Medio Cielo.

## Prioridad Media

5. Añadir sección Casas en Signos.
6. Nodo Norte por signo y por casa.
7. Síntesis Final.

## Prioridad Baja

8. Aspectos menores.
9. Retrogradaciones.
10. Generación PDF.
11. Cálculo preciso del Nodo Sur.
