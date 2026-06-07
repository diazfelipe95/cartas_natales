# Plan de Acción: Pipeline de Curación y Generación Sintética de Contenido

Este documento detalla la estrategia y el flujo técnico para homogeneizar toda la base de datos de interpretaciones astrológicas directamente desde la rama activa `feature/contenido-interpretaciones`.

El objetivo es unificar el tono basándose en el estándar de la astrología psicológica-evolutiva (estilo Howard Sasportas en `planetas_casas_sasportas.json`) resolviendo tres escenarios distintos mediante automatización con IA:

1. **Curación:** Limpiar y reestructurar JSONs con textos en bruto o problemáticos (`planetas_signos_goodman.json`, `aspectos_tompkins.json`).
2. **Expansión Controlada:** Conservar las ideas centrales de textos existentes, ampliándolas y homogeneizándolas al estilo Sasportas sin reemplazar completamente el contenido original.
3. **Generación Sintética:** Crear desde cero las interpretaciones faltantes para `angulos_signos.json` y `casas_signos.json` utilizando el conocimiento nativo de la IA, pero replicando exactamente la estructura y el tono psicológico definido.

---

# 1. El Estándar Editorial (Estilo Sasportas)

Todo el contenido final (tanto el curado como el expandido o generado desde cero) debe cumplir rigurosamente con los siguientes pilares:

* **Enfoque Psicológico y Evolutivo:** La interpretación debe plantearse como un escenario de vida, un área de aprendizaje y una dinámica interna de desarrollo. Se debe evitar el determinismo predictivo ("te va a pasar esto") o las descripciones estáticas ("eres una persona fría y punto").
* **Perspectiva del Lector Casual:** Diseñado para personas que no son astrólogas. Debe ser digerible, claro y directo.
* **Voz y Persona:** Escrito obligatoriamente en **segunda persona del singular** ("Tú tienes...", "Tu reto principal es...", "Te enfrentas a...").
* **Eliminación de Ruido:** Cero anécdotas editoriales, cero metáforas obsoletas, cero debates técnicos de astrólogos (como planetas aplicativos/separativos u orbes exactas) y cero menciones a autores externos.
* **Coherencia Estructural:** Todas las interpretaciones deben compartir una arquitectura narrativa similar para evitar diferencias de estilo entre autores de origen.
* **Compatibilidad con Generación Automática:** El resultado final debe poder ser insertado directamente en el PDF sin requerir edición manual posterior.

---

# 2. Flujo de Arquitectura del Pipeline

El script en Python procesará los archivos de la carpeta `datos/` de tres maneras según el archivo:

```text
[Escenario A: Curar JSON Existente] ───────> Leer texto bruto ────────────────┐
                                                                              │
[Escenario B: Expansión Controlada] ────> Leer texto base ────────────────────┼──> [Procesamiento IA] ──> Guardar en datos/
                                                                              │
[Escenario C: Generar Faltantes] ───────> Leer claves vacías ─────────────────┘
```

---

# 3. Estrategia por Fuente de Datos

No todos los archivos deben recibir el mismo tratamiento.

| Archivo                         | Estrategia Recomendada                           |
| ------------------------------- | ------------------------------------------------ |
| `planetas_casas_sasportas.json` | Utilizar como estándar editorial de referencia   |
| `planetas_signos_goodman.json`  | Expansión controlada                             |
| `aspectos_tompkins.json`        | Expansión controlada                             |
| `angulos_signos.json`           | Generación sintética                             |
| `casas_signos.json`             | Generación sintética                             |
| Futuros JSON incompletos        | Curación o expansión según calidad del contenido |

### Justificación

#### Goodman

Sus interpretaciones suelen contener ideas psicológicas valiosas pero utilizan un estilo más literario y simbólico. Conviene preservar el contenido conceptual mientras se adapta la redacción.

#### Tompkins

Posee interpretaciones psicológicas modernas que pueden enriquecerse y normalizarse sin eliminar el material original.

#### Casas y Ángulos

No existe una fuente base consolidada dentro del proyecto, por lo que resulta más eficiente construirlas directamente mediante generación sintética guiada por el estándar editorial.

---

# 4. Implementación del Script Automatizado (`scripts/curar_y_generar_contenido.py`)

## Modos de Operación

El sistema deberá soportar tres modos:

### Modo `curar`

Objetivo:

* Limpiar textos problemáticos.
* Corregir redacción.
* Eliminar ruido editorial.
* Adaptar al estilo Sasportas.

### Modo `expandir`

Objetivo:

* Conservar ideas centrales.
* Mantener la esencia del texto original.
* Aumentar profundidad psicológica.
* Homogeneizar estructura narrativa.

### Modo `generar`

Objetivo:

* Construir interpretaciones completamente nuevas.
* Utilizar únicamente el conocimiento astrológico del modelo.
* Replicar el estilo editorial establecido.

---

## Prompt del Sistema

```text
Actúas como un astrólogo psicológico moderno y un editor de contenido experto.

Tu meta es entregar textos interpretativos perfectamente pulidos para el reporte final de un cliente.

REGLAS ESTRICTAS DE ESTILO:

1. Tono empático, serio, profesional y enfocado al crecimiento personal, inspirado en Howard Sasportas.
2. Dirígete al usuario de forma directa en segunda persona del singular.
3. Estructura el resultado en:
   - Dinámica interna o esencia.
   - Retos o bloqueos habituales.
   - Potencial evolutivo y desarrollo personal.
4. No uses jergas técnicas complejas.
5. No menciones autores.
6. No utilices metáforas excesivas.
7. No introduzcas predicciones deterministas.
8. Devuelve únicamente la interpretación final.
```

---

## Prompt de Curación

```text
Toma el siguiente texto interpretativo en bruto y reescríbelo siguiendo las reglas editoriales establecidas.

Elimina:
- Metáforas anticuadas.
- Debates técnicos.
- Referencias al autor.
- Preguntas retóricas.

Texto:
{texto_bruto}
```

---

## Prompt de Expansión Controlada

```text
Toma el siguiente texto interpretativo.

Conserva sus ideas principales y su significado esencial.

No resumas ni sustituyas completamente el contenido.

Amplía la interpretación desarrollando:

- Motivaciones psicológicas.
- Conflictos internos.
- Patrones emocionales.
- Potencial de crecimiento.

Adapta todo al estilo editorial definido.

Texto:
{texto_bruto}
```

---

## Prompt de Generación Sintética

```text
Basándote en tus conocimientos astrológicos profundos, genera una interpretación completa para:

{contexto_clave}

La interpretación debe seguir exactamente el estándar editorial del proyecto.
```

---

# 5. Control de Calidad Automatizado

Antes de guardar una respuesta generada por la IA, el script debería validar:

* Que el texto no esté vacío.
* Que tenga una longitud mínima razonable.
* Que esté escrito en segunda persona.
* Que no contenga referencias bibliográficas.
* Que no incluya encabezados artificiales como:

  * "Aquí tienes la interpretación".
  * "Interpretación astrológica".
  * "Respuesta".

En caso de incumplimiento:

1. Reintentar automáticamente.
2. Registrar el error en un log.
3. Conservar el valor original si se supera el límite de reintentos.

---

# 6. Implementación del Script Automatizado

La implementación base presentada anteriormente continúa siendo válida.

Los cambios principales consisten en:

* Añadir el modo `expandir`.
* Incorporar validaciones automáticas.
* Registrar errores en archivos de log.
* Mantener estadísticas de procesamiento.
* Permitir reintentos automáticos ante respuestas inválidas.

Esto mejora significativamente la calidad de la base de datos final y reduce la necesidad de supervisión manual.

---

# 7. Flujo de Trabajo en la Rama de Git

## 1. Confirmar estado de la rama actual

```bash
git status
```

Debe mostrar:

```text
On branch feature/contenido-interpretaciones
```

---

## 2. Ejecutar pruebas en lote reducido

Añadir temporalmente:

```python
if i > 3:
    break
```

para validar formato y calidad de salida.

---

## 3. Ejecución completa

Eliminar el limitador y procesar todos los JSON definidos.

---

## 4. Validación, Reemplazo e Integración

* Revisar visualmente los archivos generados.
* Comparar muestras aleatorias con las fuentes originales.
* Verificar coherencia de tono.
* Reemplazar los JSON antiguos.
* Ejecutar `main.py`.
* Generar una carta natal completa de prueba.

---

## 5. Auditoría Editorial Recomendada

Antes de integrar definitivamente el contenido:

* Revisar entre el 5 % y el 10 % de las entradas generadas.
* Comparar Goodman y Tompkins frente a sus versiones expandidas.
* Confirmar que el estilo percibido sea uniforme.
* Verificar que las interpretaciones sintéticas de casas y ángulos no desentonen respecto a Sasportas.

---

## 6. Guardar Progreso en Git

```bash
git add datos/*.json scripts/curar_y_generar_contenido.py

git commit -m "feat: curación, expansión y generación sintética de interpretaciones estilo Sasportas"
```

---

# 8. Resultado Esperado

Al finalizar este pipeline, el proyecto contará con:

* Una base de datos completamente homogénea.
* Un único tono editorial.
* Interpretaciones psicológicas modernas.
* Compatibilidad total con el generador de PDFs.
* Escalabilidad para futuras incorporaciones de contenido.
* Un proceso reproducible que permitirá regenerar o mejorar la base de datos cuando se incorporen nuevas fuentes bibliográficas o modelos de IA.
