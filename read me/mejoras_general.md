# Plan de Evolución del Proyecto: Generador de Cartas Natales

Este documento analiza el estado actual del script `generador_carta.py` y establece la ruta estratégica para transformarlo en una plataforma web comercializable (SaaS), optimizada para usuarios no astrólogos y con pasarelas de pago automatizadas.

---

# 📌 Análisis Técnico del Estado Actual

## Lo que está funcionando excelente 🚀

### Precisión Astronómica
La integración directa de **swisseph (Swiss Ephemeris)** junto con **flatlib** garantiza cálculos exactos y profesionales. Es el núcleo más complejo de resolver y ya está listo.

### Manejo de Efemérides
La estructura local de archivos `.se1` dentro de `/efemerides` hace que el sistema sea independiente de APIs externas de cálculo, lo que reduce costos fijos a cero.

### Estructura de Datos Clara
El uso de archivos JSON divididos por categorías (`planetas_signos`, `planetas_casas`, etc.) es ideal para acoplar la base de datos de interpretaciones más adelante.

---

## Críticas Constructivas y Oportunidades de Mejora 🛠️

### Monolito de Código
Actualmente, `generador_carta.py` se encarga de todo:

- Cálculo astronómico
- Traducción de strings
- Cruce con JSON
- Formateo de texto
- Renderizado de archivos (TXT, MD, PDF)

Para llevarlo a la web, es obligatorio separar la lógica de negocio (cálculo) de la lógica de presentación (generación de PDF o HTML).

### Limitaciones de Estética en el PDF (FPDF)
Construir un reporte visualmente atractivo (con la imagen del mandala al inicio, tipografías elegantes y fondos geométricos) usando la librería FPDF requiere cientos de líneas de código basadas en coordenadas rígidas (X, Y).

Cambiar el diseño a futuro con este enfoque es un dolor de cabeza.

### Abstracción del Tecnicismo
Como el reporte está dirigido a personas que no saben astrología, listar aspectos crudos como:

- "Saturno en cuadratura a Pallas"
- "Urano en sextil a Plutón"

sin una traducción amigable puede abrumar al usuario.

El informe debe centrarse en la narrativa psicológica.

---

# 🗺️ Hoja de Ruta (Roadmap) de Desarrollo

```text
Fase 1: Refactorización
        ↓
Fase 2: Motor de Textos (Git)
        ↓
Fase 3: Rediseño Visual
        ↓
Fase 4: Migración Web
        ↓
Fase 5: Monetización
```

---

# 🟩 Fase 1: Modularización y API Interna (Corto Plazo)

El objetivo es preparar el código actual para que pueda recibir peticiones desde la web en lugar de la terminal.

## [ ] Dividir el script monolítico en módulos

### `src/core/calculador.py`
Exclusivo para interactuar con `flatlib` y `swisseph`, retornando las posiciones astronómicas crudas.

### `src/core/interprete.py`
Clase que toma el output del calculador y busca las coincidencias textuales en los JSON.

### `src/utils/pdf_builder.py`
Código encargado únicamente de armar el documento de salida.

### `main.py`
Script principal que coordina los módulos.

---

## [ ] Estandarizar el intercambio de datos

Haz que el módulo `interprete.py` retorne un único diccionario de Python estructurado (o un JSON masivo) con toda la información ya procesada y traducida.

Tu sistema web usará este JSON para:

- Enviarlo a la interfaz de usuario.
- Alimentar el generador de PDF.
- Exponer información vía API.

---

# 🟨 Fase 2: Alimentación de la Base de Datos (Trabajo en Paralelo)

Nutrir el contenido utilizando la carpeta `docs/` como fuente bibliográfica mediante control de versiones.

## [ ] Aislar el trabajo en Git

Crear una rama independiente para el contenido de los libros para no congelar los avances del código:

```bash
git checkout -b feature/contenido-interpretaciones
```

---

## [ ] Estrategia de extracción (Sasportas / Tompkins / Goodman)

### Lineamientos editoriales

- Enfocar la redacción en lenguaje descriptivo.
- Priorizar el enfoque psicológico.
- Promover el autoconocimiento.
- Eliminar términos excesivamente esotéricos.

### Prioridad de llenado de JSON

1. Sol y Luna
2. Ascendente y Medio Cielo
3. Planetas personales en signos
4. Planetas en casas
5. Aspectos mayores:
   - Conjunción
   - Oposición
   - Cuadratura
   - Trígono
   - Sextil

---

## [ ] Mecanismo de Tolerancia a Fallos (Fallback)

Modificar la función que lee los JSON para que, si un aspecto menor (por ejemplo, **Quirón en conjunción a Lilith**) no tiene texto aún en la base de datos:

- El programa continúe normalmente.
- No se rompa la ejecución.
- No se impriman secciones vacías en el PDF final.

---

# 🟦 Fase 3: Identidad Visual y Rediseño Estético (Mediano Plazo)

El objetivo es lograr que el PDF luzca como el de un servicio premium automatizado.

## [ ] Generación Automática del Mandala (Gráfico Astral)

Evita programar la rueda zodiacal desde cero con coordenadas matemáticas.

Integra **Kerykeion**:

```bash
pip install kerykeion
```

Ventajas:

- Basada en Swiss Ephemeris.
- Genera SVG.
- Genera imágenes listas para usar.
- Produce cartas visualmente similares a las profesionales.

---

## [ ] Migrar el motor de PDF a HTML + WeasyPrint

### Sustituir FPDF

En lugar de usar FPDF:

- Diseña la plantilla en HTML.
- Aplica estilos mediante CSS.
- Usa Google Fonts.
- Crea portadas elegantes.
- Mantén tablas limpias.
- Utiliza márgenes profesionales.

### Inyección de datos

Usar **Jinja2** para insertar:

- Interpretaciones del JSON.
- Imagen del mandala.
- Datos del usuario.

### Generación final

Compilar el HTML directamente a PDF usando:

```bash
pip install weasyprint
```

Beneficio principal:

> El diseño visual puede modificarse en minutos editando únicamente archivos HTML y CSS.

---

# 🟧 Fase 4: Migración a Entorno Web (Backend & Frontend)

Llevar el programa desde la consola local hacia Internet.

## [ ] Construir el Backend con FastAPI

Utilizar FastAPI por:

- Excelente rendimiento.
- Integración natural con Python.
- Soporte para tareas en segundo plano.

### Endpoint principal

```http
POST /api/v1/carta-natal
```

Datos esperados:

```json
{
  "nombre": "",
  "fecha": "",
  "hora": "",
  "latitud": "",
  "longitud": "",
  "zona_horaria": ""
}
```

---

## [ ] Construir el Frontend

### Landing Page

Puede desarrollarse con:

- HTML/CSS/JS puro.
- React.
- Vue.

### Requisitos mínimos

- Formulario amigable.
- Validación de fecha.
- Validación de hora.
- Diseño responsive.

### Geolocalización automática

Consumir APIs como:

- Nominatim
- Google Places

para obtener automáticamente:

- Ciudad de nacimiento.
- Latitud.
- Longitud.

sin que el usuario tenga que buscarlas manualmente.

---

# 🟥 Fase 5: Monetización, Automatización y Despliegue (Largo Plazo)

Implementar cobros automatizados y distribución del producto.

## [ ] Pasarela de Pagos Nacional (Colombia)

Integrar:

- Wompi
- ePayco

Ventajas:

- Soporte para Nequi.
- Soporte para Daviplata.
- Soporte para PSE.
- APIs sencillas para Python.

---

## [ ] Pasarela de Pagos Internacional

Integrar:

- PayPal
- Stripe

para pagos con tarjeta de crédito desde cualquier país.

---

## [ ] Flujo de Entrega Automatizado (Webhooks)

### Flujo completo

1. El cliente llena el formulario natal.
2. Es redirigido a la pasarela de pago.
3. El pago es aprobado.
4. La pasarela envía un webhook a FastAPI.
5. FastAPI valida la transacción.
6. Se ejecuta el motor de generación.
7. Se genera el PDF final.
8. El PDF es entregado al cliente.

Entrega mediante:

- Correo electrónico (`emails`, `smtplib`, etc.).
- Enlace temporal de descarga.

---

## [ ] Despliegue (Hosting)

Alojar la aplicación en plataformas compatibles con Python y Swiss Ephemeris.

### Opciones recomendadas

- Render
- Railway
- VPS en DigitalOcean

Idealmente ejecutando Ubuntu, para mantener coherencia con el entorno actual de desarrollo.

---

# 📈 Recomendación de Prioridad Inmediata

**No intentes construir la página web todavía.**

El orden recomendado para los próximos commits es:

1. Refactorizar el script actual en módulos limpios.
2. Integrar Kerykeion para generar el mandala automáticamente.
3. Reemplazar FPDF por Jinja2 + WeasyPrint.
4. Crear una plantilla HTML profesional.
5. Automatizar la generación de PDFs.

Cuando dispongas de un script local capaz de:

- Recibir los datos natales.
- Generar el mandala.
- Crear un PDF atractivo y profesional.

entonces la migración a FastAPI y a una plataforma web será principalmente una tarea de integración y despliegue.