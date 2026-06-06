# Plan de Implementación — Refactor del Generador de Cartas Natales

Basado en el diagnóstico de `Mejoras_Generador.md` y el código actual.

---

## Fase 0 — Preparación (antes de tocar código)

- [x] Leer y entender el código base y los JSONs.
- [ ] Identificar TODOS los puntos del código donde se usan signos en inglés (`sign.lower()`) para centralizar la traducción.
- [ ] Revisar `planetas_signos.json` y `planetas_casas.json` -> faltan entradas para `urano`, `neptuno`, `pluton`.

---

## Fase 1 — Core Fixes (Prioridad Alta)

### 1.1 Corregir cálculo de casas (bug 0° Aries)

**Archivo:** `generador_carta.py`

- Reemplazar el bucle `for i in range(1,13)` inline (líneas 221-227) con una función `longitud_entre()` que maneje el cruce por 0°.
- Refactorizar la asignación de casa a una función `obtener_casa_planeta(planeta, carta)`.

### 1.2 Añadir Urano, Neptuno, Plutón

**Archivo:** `generador_carta.py`

- Agregar IDs: `(const.URANUS, 7)`, `(const.NEPTUNE, 8)`, `(const.PLUTO, 9)` al listado `planetas_a_calcular`.
- Agregar traducciones en `TRADUCCION_PLANETAS`.
- Agregar entradas faltantes en `datos/planetas_signos.json` y `datos/planetas_casas.json`.

### 1.3 Calcular Nodo Sur con longitud real (no simplificación)

**Archivo:** `generador_carta.py`

- Agregar `(const.SOUTH_NODE, 11)` al listado.
- Usar `obtener_casa_planeta()` para calcular su casa real.
- Eliminar la lógica `num_casa_sur = int(num_casa) + 6`.

---

## Fase 2 — Reestructura del Informe

Objetivo: pasar del informe lineal actual a la estructura propuesta.

### 2.1 Extraer cada sección a su propia función

- `generar_seccion_angulos()`
- `generar_seccion_planetas_signos()`
- `generar_seccion_planetas_casas()`
- `generar_seccion_casas_signos()`
- `generar_seccion_mision_evolutiva()`
- `generar_seccion_asteroides()`
- `generar_seccion_aspectos()`
- `generar_seccion_sintesis()`

### 2.2 Orden del informe

```
DATOS NATALES
ESTRUCTURA DE PERSONALIDAD
  - Ascendente
  - Medio Cielo
CASAS EN SIGNOS
PLANETAS EN SIGNOS
PLANETAS EN CASAS
MISIÓN EVOLUTIVA
  - Nodo Norte (signo + casa)
  - Nodo Sur (signo + casa)
ASTEROIDES Y PUNTOS KÁRMICOS
  - Quirón, Lilith, Ceres, Pallas, Juno, Vesta
DINÁMICAS INTERNAS (ASPECTOS)
SÍNTESIS FINAL
```

### 2.3 Datos del usuario

Agregar bloque al inicio con nombre, fecha, hora, coordenadas, zona horaria.

---

## Fase 3 — Ángulos (Ascendente / MC)

- [ ] Crear `datos/angulos_signos.json` con interpretaciones dedicadas.
- [ ] Reemplazar el lookup `casas_signos.json` (que reusa textos genéricos) por el nuevo archivo.

---

## Fase 4 — Síntesis Final

- [ ] Función que analice:
  - Elemento dominante (Fuego/Tierra/Aire/Agua) basado en planetas + ascendente.
  - Modalidad dominante (Cardinal/Fijo/Mutable).
  - Planetas angulares (en casa 1, 4, 7, 10).
  - Concentración por casas.
  - Aspectos más relevantes (conjunción, oposición, etc.).
- [ ] Generar párrafo automático de resumen.

---

## Fase 5 — Orbes Diferenciados

- Reemplazar `obtener_nombre_aspecto_manual()` con orbes:
  - Sol/Luna: ±8°
  - Planetas: ±6°
  - Asteroides: ±3°
  - Nodos: ±2°

---

## Fase 6 — Aspectos Menores (Prioridad Baja)

- Quincuncio (150°), Semisextil (30°), Semicuadratura (45°), Sesquicuadratura (135°)

---

## Fase 7 — Retrogradaciones

- Consultar estado de retrogradación via `swe.calc_ut()`.
- Mostrar "(R)" junto al planeta retrógrado.

---

## Fase 8 — Grados Exactos y Cúspides

- Mostrar posición exacta: `SOL en Virgo 15°23' Casa 6`.
- Agregar tabla de cúspides.

---

## Fase 9 — Múltiples Formatos de Exportación

- Refactorizar la generación del informe para que sea un objeto/diccionario de datos, no un string.
- Crear renderers: TXT, MD, PDF (reportlab / weasyprint).
- `generar_informe(datos: dict, formato: str) -> str | bytes`

---

## Notas Técnicas

- **flatlib** usa `lon` para longitud y `sign` para signo en inglés.
- Los ángulos (Asc, MC) se obtienen con `carta.get(const.ASC)` y `carta.get(const.MC)`.
- Los objetos `GenericObject` creados para asteroides necesitan `p.id`, `p.lon`, `p.sign`, `p.signlon`.
- Swiss Ephemeris IDs: Sol=0, Luna=1, Mercurio=2, Venus=3, Marte=4, Júpiter=5, Saturno=6, Urano=7, Neptuno=8, Plutón=9, NodoN=10, NodoS=11, Lilith=15, Quirón=17, Ceres=18, Pallas=19, Juno=20, Vesta=21.
