# Proyecto Cartas Natales

## Stack
- Python 3, efemerides suizas (swisseph), JSON
- No frameworks externos; procesamiento directo
- `main.py`: CLI interactiva para generar cartas (TXT/MD/PDF)

## Archivos Clave

| Archivo | Entradas | Propósito |
|---------|----------|-----------|
| `datos/planetas_signos.json` | 216 | Interpretación de planetas en signos (estándar de calidad) |
| `datos/planetas_casas.json` | 216 | Planetas en casas + asteroides + nodos |
| `datos/casas_signos.json` | 144 | Casas en signos |
| `datos/angulos_signos.json` | 24 | Ascendente y MC en signos |
| `datos/aspectos.json` | 225 | Aspectos planetarios |
| `src/utils/renderers.py` | — | Renderiza los 5 JSONs a formato legible |
| `src/core/interprete.py` | — | Carga y gestiona los 5 JSONs |
| `src/core/calculador.py` | — | Cálculos astronómicos con swisseph |

## Estado Actual (Jun 2026)

- Los 5 JSONs están completos, válidos y cargan sin errores.
- ~700 entradas en total, caracteres variables (1500-3500 según archivo).
- **Ningún placeholder, texto OCR ni autocabecera duplicada sobrevive.**

## Reglas de Estilo (Sasportas)

1. **Narrativa 3ª persona** — "La persona", "quien posee esta posición", "el nativo".
2. **Profundidad psicológica** — describir dinámica interna (luz + sombra), no predecir eventos.
3. **Metáforas e imágenes** — "como el fénix que renace de sus cenizas", "la mente es una balanza".
4. **Estructura por párrafos**: (a) descripción del talento/dinámica, (b) imagen externa, (c) conflicto interno/sombra, (d) potencial evolutivo.
5. **Sin marcadores explícitos de sección tipo "Lado positivo:"** — fluye como texto continuo.
6. **Sin emojis ni asteriscos decorativos internos.**
7. **Sin comillas** salvo para citas textuales.

## Historial de Correcciones

### Corrección masiva de tildes (scripts/corregir_tildes.py)
- **Script automatizado** que corrige ~2300+ tildes faltantes en los 5 JSONs.
- Correcciones 100% seguras: terminaciones -ción/-sión, esdrújulas, verbos condicionales/imperfectos.
- No toca diacríticos ambiguos (tu/tú, el/él, esta/está, mas/más, solo/sólo).
- **planetas_casas.json**: 0 correcciones (ya tenía tildes correctas).
- **Fuente Python**: se corrigieron también ~30 tildes en `interprete.py` (síntesis, nombres de aspectos) y `renderers.py` (título de sección).

### Últimas (esta sesión)
- **Script de corrección de tildes**: ~2300 correcciones en JSONs + ~30 en código fuente.
- **interprete.py**: tildes corregidas en sintaxis de síntesis y nombres de aspectos.
- **renderers.py**: "Mision Evolutiva" → "Misión Evolutiva".
- Carta de prueba regenerada sin errores de acentuación.

### Sesiones anteriores (resumen)
- 120 entradas de planetas_casas reescritas (10 planetas × 12 casas).
- Variación de transiciones vía pools de 25 variantes.
- Eliminación de autocabeceras duplicadas en todos los JSONs.
- Corrección de ~50+ transiciones "Frankenstein" en casas_signos.
- 225 entradas de aspectos reescritas (OCR reemplazado).
- 24 entradas de angulos_signos generadas.
- 144 entradas de casas_signos generadas.
- 216 entradas de planetas_signos generadas.
- Renderers modificado (4 cambios de formato).
- Síntesis expandida a 3-4 párrafos.

## Decisiones Clave

1. **No usar APIs externas** por cuotas/rate limits; generación directa del asistente.
2. **Preferir subagentes** para correcciones cuando las transiciones varían sutilmente.
3. **No modificar renderers.py** — regla rota cuando fue necesario; ahora modificado.
4. **Aperturas truncadas eliminadas completamente**, no reemplazadas — el cuerpo funciona como inicio natural.
5. **Pools de 25 variantes** para transiciones (imagen, conflicto, positiva, sombra).
6. **Corrección de tildes vía script** no subagentes — más rápido y determinista.

## Pendiente / No Inmediato
- Revisión de estilo consistente en asteroides (Ceres, Juno, Lilith, Pallas, Vesta — signo OK, casa puede variar).
- Si se agregan nuevas entradas, mantener el estilo Sasportas y la estructura de párrafos documentada arriba.
