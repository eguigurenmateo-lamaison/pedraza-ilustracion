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

## Contexto comercial clave (actualizado ago-2026)

- Facturación actual de la tienda: **~USD 5.000/mes**. Meta: **USD 10.000/mes**. Esta es la métrica norte del plan.
- **Datos reales de Shopify (captura de Felipe, 1-24 jul-2026, todos los canales):** ventas $4,17M CLP (+32%), 110 pedidos (+34%), 10,8 mil sesiones (+9%), conversión 0,98% (+21%). Derivados: **AOV real ≈ $37.900 CLP** (reemplaza la referencia de memoria de ~$60.000), ~4,6 pedidos/día (~140/mes proyectado), ~450 sesiones/día. La palanca CRO queda cuantificada: con el mismo tráfico, subir conversión de ~1% a ~1,7% casi duplica la venta. **Estos datos quedan como histórico de julio — los vigentes están en la sección "El embudo" más abajo, y el ticket promedio bajó de $37.900 a $31.181.**
- Seguidores de @pedraza_ilustracion: **62.500** (confirmado por el operador, jul-2026).
- **"Cote" = María José Pedraza.** Ella es quien responde los mensajes/DMs hoy (confirmado por el operador).
- **Envío gratis: sobre $50.000 CLP** ✅ verificado en Shopify el 23-ago-2026: descuento automático "Envío gratis en compras sobre $50.000", activo desde el 10-abr-2026. El umbral de $30.000 del research era una versión cacheada del sitio. **La propuesta de bajarlo a $44.990 existe pero NO está aplicada** — no usarla como si rigiera.
- **Marca "Pedraza Ilustración" registrada en Chile (INAPI)** ✅. Pendiente: registro en EEUU (USPTO) para la Rampa Amazon (confirmado por Felipe, jul-2026).
- Objetivo #1: escalar ventas de la tienda online (Shopify). Mercado: Chile ahora, Amazon EEUU pronto (anexo "Rampa EEUU").
- **Doble motor de audiencia** (feedback de Felipe, jul-2026): activar la base de 62.500 seguidores Y salir a buscar audiencia nueva; los **lanzamientos de producto** ahora son posibles (antes limitados por los tiempos de Cote) y son palanca comercial junto al calendario de fechas.
- **Frentes fuera del plan orgánico actual**: precios, stock, CRO, Meta Ads, Google Ads (los levantó Felipe) y email marketing (lo sumó el operador) — se definen tras la reunión del lunes 27-jul-2026 (10:00 Chile) y la entrega de accesos, con checklist propio del operador. No inventar esa estrategia antes de tener datos y accesos.
- **Email marketing — enfoque ya definido por el operador (jul-2026):** 3 campañas por semana, todas con la misma estructura: storytelling al inicio → conectar con un producto. La ejecución (herramienta, listas, calendario) se define igual tras la reunión y los accesos.
- El detalle del acuerdo comercial operador-cliente (fijo + variable) NO se incluye en ningún entregable.

## El negocio en 30 segundos

Tienda Shopify chilena (`pedrazailustracion.com`, CLP, UTC-04) que vende objetos ilustrados de flora y fauna de Chile: puzzles de 1000 y 60 piezas, naipes, botellas térmicas, láminas, calcetines, pines, libretas, totebags y postales.

- **Cote (María José Pedraza)** — ilustradora y fundadora. Decide precios, producción y stock. Es quien responde los mensajes y DMs.
- **Mateo Eguiguren** — Fractional COO. Ejecuta Meta Ads, Google Ads y Klaviyo. Es quien pide y aprueba el trabajo de este repo.
- **Felipe Robinson** — 🟡 POR CONFIRMAR. En las actas de julio y agosto de 2026 decide precios, descuentos y stock junto a Cote, y es contraparte en todas las reuniones. El documento de contexto de ago-2026 no lo menciona. Preguntar antes de asumir que salió del equipo.
- Fabricación en China, contenedor de **75 a 90 días** de tránsito. El catálogo no puede reaccionar rápido.
- **5 de los 6 productos más vendidos son preventa.** El modelo comercial es lanzamiento con fecha y cupo, no catálogo permanente. Por eso la fecha de despacho es información crítica en la ficha de producto, no un detalle.

## El embudo: dónde está la fuga

Verificado en Shopify el 23-ago-2026, últimos 30 días 🟢:

| Etapa | Cantidad | % de sesiones |
|---|---|---|
| Sesiones | 13.016 | — |
| Agregan algo al carrito | 497 | **3,8%** |
| Llegan al pago | 346 | 2,7% |
| Completan la compra | 129 | **0,99%** |

Pedidos: 135 · Ventas brutas: $4.301.590 · **Ticket promedio: $31.181** (meta: $45.000).

**De cada 100 visitas, 96 no agregan nada al carrito.** Eso no es problema de precio ni de envío: es la ficha de producto. La conversión debería estar entre 1,8% y 3%. Cada punto que se recupera vale del orden de **$4,6M CLP al mes** sin gastar un peso más en publicidad.

**53% del tráfico viene de Instagram orgánico en celular** 🟡 (dato heredado, no verificado en esta sesión). Mobile primero no es una preferencia, es la mayoría del negocio.

## Los productos y los márgenes

### Los 4 que importan (cerca del 60% de la facturación)

| Producto | Precio |
|---|---|
| Naipes Aves de Chile | $19.490 ✅ |
| Puzzle Aves y Flores de Chile | $23.790 (precio de preventa, con el 15%) |
| Puzzle Hongos de Chile | $23.790 |
| Botella térmica Aves de Chile | $27.990 ✅ |

La línea **"Aves de Chile"** completa es ~45% del negocio. Todo se construye desde ahí.

### Márgenes por familia

Confirmados por el operador (ago-2026), **calculados sobre el precio con IVA**:

Postales 82% · Pins 82% · Llaveros 78% · Naipes 76% · Láminas A2 69% · Puzzle 1000 69% · Calcetines 69% · Láminas A3 67% · Botellas 59% · Totebag 57% · Libretas 55% · Puzzle 60 pzs 46%

**Postales, pins y llaveros son los que se ofrecen como segunda unidad.** Libretas, totebags y el puzzle de 60 piezas no se promocionan.

## Números que se usan en la interfaz

- **Envío gratis: sobre $50.000** ✅ verificado. Los envíos se cobran **por peso, no por monto**: base $5.990, y sube hasta $16.000-$34.590 en regiones para paquetes pesados. Cualquier barra de progreso hacia el envío gratis tiene que apuntar al descuento automático, no a una tarifa de envío.
- **Pack 2 puzzles $44.790 · Pack 3 puzzles $65.490** ✅ verificados.
- **Precios de puzzles:** hoy con el 15% de preventa — adulto **$23.790**, niños **$15.990**. **En septiembre de 2026 vuelven a los de antes: adulto $27.990, niños $18.990** (confirmado por el operador, ago-2026).
- **Nunca hardcodear precios, fechas de despacho ni textos de campaña.** Van como metafields o settings editables por Cote sin tocar código.

## Inventario

- **El inventario negativo es normal y esperado:** es preventa vendiendo bajo cero. Se regulariza cuando llega el contenedor. Nunca tratar un SKU negativo como quiebre sin antes revisar si es preventa.
- **La tienda tiene cerca de 40 packs en borrador**, varios duplicados entre sí: el trío de aves (puzzle + botella + naipes) existe tres veces a $62.600, $69.870 y $69.990, y el dúo de hongos dos veces a $39.990 y $47.990. Antes de publicar cualquiera hay que limpiar los duplicados.
- Tres packs **"Semana Pedraza"** están armados con imagen, descripción y stock, solo apagados: Coleccionista $81.990, Descubrimiento $73.990, Explorador $52.990.
- Ya existe **"Colección completa Láminas Flora y Fauna" a $200.940** en borrador. Es el pendiente del "lleva 5, paga 4" — revisar y ajustar ese, no crear uno nuevo.

## Accesos conectados

| Plataforma | Estado | Identificador |
|---|---|---|
| Meta Ads | ✅ conectado, con escritura | `10150190815478583` |
| Klaviyo | ✅ conectado, con escritura | `RAYABY` · remitente `cote@pedrazailustracion.com` |
| Shopify | ✅ conectado, con escritura | `pedrazailustracion.com` |
| Google Ads | ❌ pendiente de conectar | inversión ~$16.000 CLP/día |

### Regla de ejecución con los accesos

- **Se ejecuta sin preguntar** todo lo reversible que no ve un cliente: borradores, colecciones ocultas, campañas en pausa, plantillas de correo sin enviar, lecturas y análisis.
- **Se deja listo y se espera el visto bueno de Mateo** para todo lo que ve un cliente o gasta plata: publicar un producto, cambiar un precio, enviar una campaña, encender o modificar un anuncio activo.

## MER — la métrica de verdad del negocio

**MER = ventas brutas de Shopify ÷ inversión total en publicidad (Meta + Google).**

- Equilibrio **2,9** · piso operativo **3,5** · **freno automático bajo 3,2**.
- **NUNCA calcular el MER con el revenue atribuido por Meta.** Meta se auto-atribuye del orden del 79% de la facturación total y está inflado. Mostrar ambos por separado y etiquetar cuál es cuál.
- Mientras Google Ads no esté conectado, el MER se arma con la inversión real de Meta más la de Google cargada a mano (~$16.000 CLP/día) y **se marca como parcial**.

## El reporte diario

- **Se entrega como mensaje listo para copiar y pegar en WhatsApp, no en Slack.** La comunicación del equipo pasa por WhatsApp.
- Contenido: ventas de ayer contra el mismo día de la semana anterior, pedidos, ticket promedio, conversión, inversión en publicidad, MER, ingreso por destinatario de correo, top 5 productos y alertas de stock bajo 30 días de cobertura.
- Alertas: MER del mes bajo 3,2 · campañas con ROAS bajo 2 y más de $50.000 gastados · SKU en cero o negativo **que no sea preventa**.
- Credenciales siempre en variables de entorno, nunca en el código. Histórico en CSV o SQLite.

## Voz y diseño de la tienda

La marca es **acuarela naturalista chilena**. Sobria, cercana, primera persona de Cote. Habla de observar aves, caminar cerros, viajar con la cámara. La frase que define el tono: *"El primer paso para proteger algo es conocerlo."* El detalle completo de cómo escribe Cote está en la sección "La voz de Cote" más abajo, y manda por sobre esto.

**Nunca:** contadores regresivos rojos, banners de urgencia agresiva, mayúsculas sostenidas, el descuento como argumento principal, ni nada que parezca dropshipping.

**Siempre:** español de Chile, la ilustración como héroe visual (no el copy), mobile primero.

## Reglas para el repo del tema de Shopify

🟡 Ese repo todavía no existe. Estas reglas quedan guardadas para cuando se cree y **no aplican a este repo**, que es el sitio de páginas HTML del plan.

1. **Nunca publicar al tema en vivo.** Todo trabajo va en una rama. Mateo revisa y publica.
2. **Nunca hardcodear precios, fechas de despacho ni textos de campaña.** Van como metafields o settings del theme editor.
3. **Medir el peso y el tiempo de carga antes y después.** El tráfico es móvil chileno; cada kilobyte cuenta.
4. **No agregar apps de terceros** sin preguntar. Ya hay demasiadas capas.
5. Entregar siempre: resumen de qué se tocó + capturas móvil y escritorio del antes y el después.

**Cola de trabajo de ese repo, en orden:** fichas de los 4 productos principales (bloque de preventa con fecha de despacho sobre el botón de compra, reseñas sobre el pliegue, especificaciones concretas, barra hacia el envío gratis, sección "va bien con") · bloque de segunda unidad en el carrito y el drawer (máximo 3 sugerencias de alto margen, nunca productos ya en el carrito, misma colección primero, no mostrar sobre $60.000) · plantilla de landing para tráfico de Instagram (un protagonista, fecha de cierre visible, historia corta de Cote, reseñas, un solo CTA repetido 3 veces, sin menú ni sliders) · reporte diario.

## Glosario

- **MER**: ventas brutas totales ÷ inversión total en publicidad. Equilibrio 2,9 · piso operativo 3,5 · freno automático bajo 3,2.
- **AOV / ticket promedio**: valor promedio del pedido. Hoy $31.181 CLP.
- **Preventa**: producto vendido antes de tenerlo en bodega, con fecha de despacho comprometida. Es el motor comercial, no una excepción.
- **Breakage**: valor de gift cards que nunca se redime. Real: 10-19%, no 85%.

## Reglas de contenido del operador (aplicar en toda la estrategia)

- **Verde de marca:** el sitio web del cliente usa el verde naturaleza `#3B5751` — debe estar presente en el sistema de diseño del sitio del plan.
- **Métrica reina por formato:** para Reels/carruseles/posts del feed = **compartidos**; para historias = **interacciones ÷ visualizaciones**.
- **Filtro 5-50:** un niño de 5 años debería entender de qué trata la pieza, y 50 de 100 personas aleatorias deberían entender al menos el 50% inicial.
- **Contenido "conciencia 1" para alcance:** piezas sobre temas universales y cotidianos (dormir, tomar agua, mentalidad) para gente que aún no piensa en comprar y solo admira la naturaleza. Referencia del operador: @mattelsa (carruseles de 30-58 mil me gusta, capturas jul-2026).
- El checkout nativo de Instagram nunca estuvo disponible fuera de EEUU: en Chile la compra SIEMPRE se cerró fuera de la app. No presentar su eliminación como un cambio que afecta a la marca.

## La voz de Cote (obligatoria en TODO texto firmado por la marca)

Destilado de 15 correos escritos por María José "Cote" Pedraza (jul-ago 2026): los 6 de la
preventa de puzzles y las 9 historias. Aplica a correos, guiones de Reels, captions,
plantillas de DM y cualquier texto que salga con su nombre. **Rige por sobre cualquier
instinto de redacción publicitaria.**

**Estructura de correo:** `Hola,` solo → primera línea que es anzuelo → párrafos de 1 a 3
líneas con mucho aire → puente al producto en 1 o 2 líneas al final → enlace en su propia
línea con formato `Ver la preventa →` → cierre `Con cariño,` o `Un abrazo,` + `Cote` →
P.D. opcional. **Lo comercial (envío gratis, reseñas, plazos) va en la P.D., nunca en el cuerpo.**

**La primera línea es un hecho que ya ocurrió**, con acción y algo que se pueda ver. Nunca
un estado ni una reflexión genérica. Sirve: "La primera vez que fui a Torres del Paine no
vi las Torres." No sirve: "Hay encuentros que uno recuerda toda la vida."

**El asunto** sale de esa primera línea, recortado (máx. ~45 caracteres), concreto y en
primera persona. El **preheader** (máx. ~90 caracteres) continúa el asunto, nunca lo parafrasea.

**Cómo suena:**
- Frases cortas, una idea por frase. Líneas sueltas como golpe de silencio, una o dos por
  pieza: "La llama tenía otros planes." / "Ahí estaba el puma."
- Empieza frases con "Y" o "Pero" para dar ritmo.
- Casi nunca signos de exclamación. Cero emojis en el cuerpo. Cero preguntas retóricas.
- Nombres propios y fechas reales siempre: "Hotel Unai", "Bahía Inútil", "Ladera Sur",
  "el año 2009". Nunca "un viaje al sur". La especificidad es lo que la hace creíble y es
  lo primero que se pierde al reescribir.
- Un detalle sensorial corto por pieza: "pequeños pompones cafés".
- **Se pone en ridículo, nunca por encima.** La escupe una llama, vuelve del cerro sin ver
  nada, camina cinco días bajo la lluvia sin ver las Torres. Si un pasaje la deja como
  experta o como heroína, está mal escrito. Nunca elogia su propio trabajo.

**Cómo vende (la regla más importante):** le quita presión al lector en vez de ponérsela.
Literal de ella: *"Los puzzles no desaparecen… Nadie se queda sin puzzle, simplemente unos
lo recibirán antes que otros."* La urgencia se explica como hecho logístico, jamás como
amenaza. **PROHIBIDO:** "última oportunidad", "no te lo pierdas", "quedan pocas unidades",
"aprovecha", "solo por hoy", cuentas regresivas. Agradece sin adular: trata al lector como
alguien que acompaña un proyecto, no como un cliente a convertir.

**Prohibiciones:** voseo rioplatense (ver regla 4 de comunicación); jerga de marketing
("colección cápsula", "drop", "edición limitada", "comunidad", "storytelling"); explicar la
naturaleza como enciclopedia (cuenta lo que le pasó, no dicta clase); palabras ajenas a su
registro como "robot"; moralizar o sacar lecciones de vida — cuenta el hecho y deja que el
lector concluya.

**Vicios propios de ella que hay que corregir al editar:** repite "las ilustraciones empiezan
mucho antes del pincel" en cuatro correos distintos (rotar el remate); alterna firma
"María José" y "Cote" (**siempre Cote**, decisión del operador ago-2026); mezcla tres escenas
en una historia (una historia = una escena); sus borradores de historia terminan sin puente
al producto (hay que agregarlo).

**Largo:** correo de historia 180-320 palabras; correo de venta 200-320.

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
- **Contratos de checklist aislados:** cada página usa su propio atributo `data-*` y su propio prefijo de `localStorage`. Nunca se reutiliza uno existente, y **toda casilla debe guardar su estado** — una casilla sin contrato `data-*` es una falla de QC. Contratos tomados: `ads`, `bitacora`, `campanas`, `clientes`, `correo`, `correosp`, `cro`, `digital`, `estado`, `inventario`, `navidad`, `ofertas`, `pedido`, `plan90`, `preventa`, `react`, `tablero`, `task`, `tienda`.
- Todo cálculo con fechas o plata se verifica con un script independiente antes de publicarlo.

### Al terminar

Entregar al operador el mensaje de WhatsApp para el grupo, con los links directos a lo creado y los pendientes de cada persona.
