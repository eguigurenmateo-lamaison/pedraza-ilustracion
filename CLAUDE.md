# Memoria del proyecto — Plan Pedraza Ilustración

Reglas permanentes para TODOS los entregables de este repo (documentos, páginas HTML, README, plantillas). Aplican a cualquier sesión y a cualquier subagente.

## Reglas de comunicación (obligatorias)

1. **Visual primero.** Usar gráficos y elementos visuales donde sea posible: la gran mayoría de las personas entiende mejor una idea viéndola que leyéndola.
   - En páginas HTML: gráficos con SVG/CSS inline (sin librerías externas), diagramas de embudo, barras de progreso, líneas de tiempo, calendarios visuales, tarjetas comparativas, íconos.
   - En documentos Markdown: diagramas Mermaid (GitHub los renderiza), tablas simples y visuales, emojis como señalética (🟢🟡🔴).
   - Regla práctica: si una idea tiene pasos, comparaciones, fechas o números, se muestra con un gráfico o diagrama, no solo con texto.

2. **Lenguaje simple, cero tecnicismos.** Todo debe poder entenderse sin conocimientos previos de marketing ni de e-commerce.
   - Si un término técnico es inevitable, se explica al lado en palabras simples la primera vez. Ejemplos: "ticket promedio (lo que gasta una persona por compra)", "CTA (la invitación a hacer algo, como 'compra aquí')", "alcance (cuánta gente vio la publicación)".
   - Preferir siempre la palabra simple: "guardados" en vez de "saves", "compartidos" en vez de "sends" (aclarando que Instagram lo mide como envíos por DM), "publicar" en vez de "postear" cuando se pueda.
   - Frases cortas. Una idea por frase.
   - **IMPORTANTE: esta regla no se menciona nunca dentro de los entregables** (nada de "explicado simple para que cualquiera entienda" ni similares). Simplemente se escribe así.

3. **Diseño mobile-first.** Todo entregable visual (especialmente las páginas HTML del sitio) se diseña primero para el celular y debe verse impecable en pantalla móvil: tipografía legible sin zoom, botones y checkboxes cómodos para el dedo (mínimo ~44px de área táctil), tablas y gráficos que se adaptan o permiten scroll horizontal contenido, menú de navegación usable con una mano. El escritorio es la mejora progresiva, no al revés. Probar mentalmente cada componente en un ancho de ~375px antes de darlo por bueno.

4. **Voz: español neutro con expresiones chilenas puntuales.**
   - PROHIBIDO el voseo rioplatense: nada de "tenés/querés/tocá/comentá/mandale". Usar tuteo estándar: "tienes/quieres/toca aquí/comenta".
   - Expresiones chilenas con moderación y solo donde sumen cercanía (ej. "al tiro", "filete"). Marca familiar, educativa y de conservación; cercana, sin solemnidad.

5. **Entregables en HTML compartibles por link.** Todo entregable destinado al cliente se produce como página HTML autocontenida (servible por GitHub Pages), para poder compartirlo con un link y que lo revisen desde cualquier dispositivo. Los archivos Markdown (docs/) son material de trabajo interno; su contenido final vive en las páginas HTML.

6. **Todo lo copiable, con copia en un clic.** Cualquier texto pensado para copiar y pegar (bios, guiones, plantillas de DM, captions, mensajes) va SIEMPRE dentro de un bloque `.copyblock` con botón "Copiar": usa `navigator.clipboard` con fallback a `document.execCommand('copy')`, feedback visual "✓ ¡Copiado!" al hacer clic, y delegación de eventos (un solo listener por página). En móvil el botón debe ser cómodo para el dedo.

## Contexto comercial clave (confirmado por el operador, jul-2026)

- Facturación actual de la tienda: **~USD 5.000/mes**. Meta: **USD 10.000/mes**. Esta es la métrica norte del plan.
- **Datos reales de Shopify (captura de Felipe, 1-24 jul-2026, todos los canales):** ventas $4,17M CLP (+32%), 110 pedidos (+34%), 10,8 mil sesiones (+9%), conversión 0,98% (+21%). Derivados: **AOV real ≈ $37.900 CLP** (reemplaza la referencia de memoria de ~$60.000), ~4,6 pedidos/día (~140/mes proyectado), ~450 sesiones/día. La palanca CRO queda cuantificada: con el mismo tráfico, subir conversión de ~1% a ~1,7% casi duplica la venta.
- Seguidores de @pedraza_ilustracion: **62.500** (confirmado por el operador, jul-2026).
- **"Cote" = María José Pedraza.** Ella es quien responde los mensajes/DMs hoy (confirmado por el operador).
- **Envío gratis: sobre $50.000 CLP** (confirmado por Felipe, jul-2026; el umbral de $30.000 que apareció en el research era una versión cacheada del sitio).
- **Marca "Pedraza Ilustración" registrada en Chile (INAPI)** ✅. Pendiente: registro en EEUU (USPTO) para la Rampa Amazon (confirmado por Felipe, jul-2026).
- Objetivo #1: escalar ventas de la tienda online (Shopify). Mercado: Chile ahora, Amazon EEUU pronto (anexo "Rampa EEUU").
- **Doble motor de audiencia** (feedback de Felipe, jul-2026): activar la base de 62.500 seguidores Y salir a buscar audiencia nueva; los **lanzamientos de producto** ahora son posibles (antes limitados por los tiempos de Cote) y son palanca comercial junto al calendario de fechas.
- **Frentes fuera del plan orgánico actual**: precios, stock, CRO, Meta Ads, Google Ads (los levantó Felipe) y email marketing (lo sumó el operador) — se definen tras la reunión del lunes 27-jul-2026 (10:00 Chile) y la entrega de accesos, con checklist propio del operador. No inventar esa estrategia antes de tener datos y accesos.
- **Email marketing — enfoque ya definido por el operador (jul-2026):** 3 campañas por semana, todas con la misma estructura: storytelling al inicio → conectar con un producto. La ejecución (herramienta, listas, calendario) se define igual tras la reunión y los accesos.
- El detalle del acuerdo comercial operador-cliente (fijo + variable) NO se incluye en ningún entregable.

## Reglas de contenido del operador (aplicar en toda la estrategia)

- **Verde de marca:** el sitio web del cliente usa el verde naturaleza `#3B5751` — debe estar presente en el sistema de diseño del sitio del plan.
- **Métrica reina por formato:** para Reels/carruseles/posts del feed = **compartidos**; para historias = **interacciones ÷ visualizaciones**.
- **Filtro 5-50:** un niño de 5 años debería entender de qué trata la pieza, y 50 de 100 personas aleatorias deberían entender al menos el 50% inicial.
- **Contenido "conciencia 1" para alcance:** piezas sobre temas universales y cotidianos (dormir, tomar agua, mentalidad) para gente que aún no piensa en comprar y solo admira la naturaleza. Referencia del operador: @mattelsa (carruseles de 30-58 mil me gusta, capturas jul-2026).
- El checkout nativo de Instagram nunca estuvo disponible fuera de EEUU: en Chile la compra SIEMPRE se cerró fuera de la app. No presentar su eliminación como un cambio que afecta a la marca.

## Reglas duras del entregable

- Nunca inventar datos ni estadísticas: cada dato con fuente (URL) o marcado 🟡 VERIFICAR / 🟡 SUPUESTO.
- Sitio: HTML autocontenido por archivo, cero dependencias externas, cero CDNs, todo CSS/JS inline. Sistema de diseño compartido vía variables CSS. localStorage con prefijo `pedraza-plan:`.
- Cada documento operativo trae plantillas listas para copiar y pegar (copy real, sin `[placeholder]`).
- Commits descriptivos al final de cada fase; push a la rama que indique el entorno.

## Proceso de cierre de cada ronda (obligatorio, en este orden)

Toda ronda de trabajo termina con estos tres pasos, siempre en esta secuencia y sin saltarse ninguno:

1. **Crear el PR** contra `main`, con cuerpo que explique qué resuelve, la tabla de páginas nuevas o modificadas, y el detalle del QC realizado.
2. **Correr el QC completo** sobre TODAS las páginas del sitio, no solo las nuevas. El QC no es opcional ni se declara: se ejecuta y se reportan los números.
3. **Merge a `main`** únicamente si el QC pasó al 100%. Si algo falla, se arregla y se vuelve a correr el QC antes del merge.

### Qué verifica el QC (todas las páginas × móvil 375px y escritorio 1280px)

- Cero errores de consola y cero excepciones de JavaScript.
- Cero scroll horizontal, con el panel de navegación **abierto y cerrado**.
- El menú abre, marca correctamente la página actual (`aria-current="page"` coincide con el nombre del archivo), y cierra con Escape.
- Todas las páginas presentes en el menú, con el mismo número de entradas en el panel y en el array `NAV_PAGES`.
- Bloque CSS canónico **byte a byte idéntico** en todos los archivos (hasta el cierre de `@media print`).
- Checkboxes que persisten en `localStorage` al recargar.
- Botones "Copiar" funcionando, con destino existente para cada `data-copy-target`.
- Cero ids duplicados, HTML balanceado, anclas internas y enlaces entre páginas sin roturas.
- Cero recursos externos (ni CDNs, ni fuentes, ni imágenes remotas).
- **Contratos de checklist aislados:** cada página usa su propio atributo `data-*` y su propio prefijo de `localStorage`. Nunca se reutiliza uno existente. Contratos tomados: `task`, `cro`, `plan90`, `bitacora`, `estado`, `preventa`, `tienda`, `clientes`, `precios`.
- Todo cálculo con fechas o plata se verifica con un script independiente antes de publicarlo.

### Al terminar

Entregar al operador el mensaje de WhatsApp para el grupo, con los links directos a lo creado y los pendientes de cada persona.
