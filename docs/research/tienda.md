# Investigación de la tienda — Pedraza Ilustración

**Fecha de investigación:** 23 de julio de 2026
**Alcance:** catálogo, precios, propuesta de valor, envíos y AOV estimado de pedrazailustracion.com (Shopify), Fase 0 del research para el plan Instagram → tienda.

> **Nota metodológica importante:** todo intento de fetch directo a `pedrazailustracion.com` (HTML, endpoints JSON de Shopify, robots.txt, sitemap.xml), tanto vía la herramienta WebFetch como vía `curl` directo y vía un proxy de lectura de terceros (r.jina.ai), devolvió **403 Forbidden**. Sin embargo, esto **no se puede atribuir al sitio**: se verificó con un dominio de control (`example.com`) que el mismo 403 ocurre para *cualquier* dominio externo desde esta sesión — el proxy de red del entorno de trabajo rechaza la conexión (CONNECT) a nivel de sandbox, antes de que el request llegue al destino. En ningún momento de esta sesión se comprobó de forma independiente un bloqueo anti-bot del lado de Shopify/pedrazailustracion.com; la única referencia a un "403 por protección Shopify" es una observación previa del operador citada en el brief de la tarea, no un dato verificado acá. Todos los datos de catálogo y precios de este documento se obtuvieron por lo tanto de **snippets indexados por buscadores** (WebSearch), no de un fetch directo verificado del HTML/JSON vivo. Esto se explica en detalle en la sección final "Registro del playbook". Cada precio está marcado con su URL de origen, pero debe tratarse como **dato de caché de buscador**, potencialmente desactualizado, y no como una lectura en tiempo real del sitio.

---

## 1. Catálogo: colecciones detectadas

Colecciones identificadas vía `site:pedrazailustracion.com` y búsquedas dirigidas (no se pudo confirmar si esta lista es exhaustiva, ya que no se logró leer `/collections.json` ni `/sitemap.xml` directamente — 🟡 VERIFICAR lista completa con el operador):

| Colección | URL |
|---|---|
| Todos los productos | https://pedrazailustracion.com/collections/all |
| Puzzles | https://pedrazailustracion.com/collections/puzzles |
| Láminas | https://pedrazailustracion.com/collections/laminas |
| Láminas Aves | https://pedrazailustracion.com/collections/laminas-aves |
| Láminas Flora y Fauna | https://pedrazailustracion.com/collections/laminas-flora-y-fauna |
| Láminas Mariposas | https://pedrazailustracion.com/collections/laminas-mariposas |
| Loza (platos/vajilla) | https://pedrazailustracion.com/collections/loza |
| Platos | https://pedrazailustracion.com/collections/platos |
| Papelería | https://pedrazailustracion.com/collections/papeleria |
| Libretas de nota | https://pedrazailustracion.com/collections/libretas-de-nota |
| Accesorios (calcetines, bolsos, botellas, llaveros) | https://pedrazailustracion.com/collections/accesorios |
| Ofertas / "¡Black!" | https://pedrazailustracion.com/collections/ofertas |

Fuentes: resultados de `site:pedrazailustracion.com` y variantes de búsqueda (ver listado de URLs devuelto por WebSearch el 2026-07-23).

Temáticas transversales por especie/grupo taxonómico que se repiten en varias categorías (láminas, puzzles, packs): aves de Chile, flores de Chile, mariposas y escarabajos de Chile, hongos de Chile, cetáceos de Chile. Esto confirma el ángulo de "flora y fauna nativa" mencionado en el brief, aplicado como sistema de series repetibles entre categorías (mismo motivo en lámina, puzzle, plato, calcetín, etc.) — patrón relevante para pensar en cross-sell por especie/serie en la Fase de Instagram.

## 2. Productos con precio confirmado (snippet de buscador)

### Puzzles (1000 piezas)

| Producto | Precio | Precio regular (si hay oferta) | Fuente |
|---|---|---|---|
| Puzzle ilustrado — Aves y Flores de Chile | $24.990 CLP | $27.290 CLP | https://pedrazailustracion.com/products/puzzle-1000-piezas-aves-flores-chilenas |
| Puzzle ilustrado — Hongos de Chile | $24.990 CLP | $27.290 CLP | https://pedrazailustracion.com/collections/puzzles (URL de producto individual no capturada; ver también reseller: https://www.bazared.cl/products/puzzle-ilustrado-hongos-de-chile-1000-piezas) |
| Puzzle ilustrado — Mariposas y Escarabajos de Chile | $27.290 CLP | — | https://pedrazailustracion.com/collections/puzzles (URL de producto individual no capturada) |
| Puzzle ilustrado — Cetáceos de Chile | $24.990 CLP | — | https://pedrazailustracion.com/products/puzzle-1000-piezas-cetaceos-chilenos |

Características del producto (recurrentes en varias fichas): 1000 piezas, arma 50x70 cm, incluye guía con la imagen completa y nombres (comunes/científicos) de cada especie — refuerza el ángulo educativo. Fuente: snippets de https://pedrazailustracion.com/collections/puzzles.

### Loza / vajilla

| Producto | Precio | Precio regular | Fuente |
|---|---|---|---|
| Juego Loza Aves Azul — 12 piezas (PREVENTA, incluye calcetín de regalo) | $69.990 CLP | $83.990 CLP | https://pedrazailustracion.com/products/platos |
| Juego Loza Aves Rojo — 12 piezas | 🟡 VERIFICAR (no se capturó precio explícito; por título parece ser una variante de color del mismo set) | — | https://pedrazailustracion.com/products/platos-color |

Detalle: acuarelas de aves chilenas, apto microondas y lavavajillas. Fuente: snippet de https://pedrazailustracion.com/products/platos.

### Accesorios

| Producto | Precio | Fuente |
|---|---|---|
| Calcetines Aves de Chile | $9.390 CLP | https://pedrazailustracion.com/products/calcetin-1 |
| Llavero Martín Pescador | $8.790 CLP | https://pedrazailustracion.com/collections/accesorios (URL de producto individual no capturada) |
| Bolso Aves de Chile | $16.490 CLP | https://pedrazailustracion.com/collections/accesorios (URL de producto individual no capturada) |
| Bolso Flores de Chile | $16.490 CLP | https://pedrazailustracion.com/collections/accesorios (URL de producto individual no capturada) |
| Botella térmica Aves de Chile | $28.990 CLP | https://pedrazailustracion.com/collections/accesorios (URL de producto individual no capturada) |
| Botella térmica Hongos de Chile | $28.990 CLP | https://pedrazailustracion.com/collections/accesorios (URL de producto individual no capturada) |

### Papelería

| Producto | Precio | Precio regular | Fuente |
|---|---|---|---|
| Libreta Flores de Chile | $13.590 CLP | $19.390 CLP | https://pedrazailustracion.com/collections/papeleria y https://pedrazailustracion.com/collections/libretas-de-nota |
| Libreta Aves | $13.590 CLP | $19.390 CLP | https://pedrazailustracion.com/collections/papeleria y https://pedrazailustracion.com/collections/libretas-de-nota |
| Pack 8 postales Aves de Chile | 🟡 VERIFICAR (precio no capturado) | — | https://pedrazailustracion.com/products/pack-8-postales-aves-de-chile |

### Láminas (fine art prints)

No se logró capturar el precio de venta de ninguna lámina individual pese a varios intentos de búsqueda dirigida — 🟡 VERIFICAR con el operador. Sí se confirmaron ficha técnica y formatos vía snippets:

- Formatos: 33x50 cm y 42x60 cm (una ficha menciona además 24x26 cm para el formato "pack"). Fuente: https://pedrazailustracion.com/products/laminas-flora-y-fauna-grande-42x60-cm y https://pedrazailustracion.com/products/pack-laminas-loica-y-siete-colores-copia.
- Técnica: impresión FineArt / Giclée con tintas de pigmento sobre papel Hahnemühle libre de ácido (premium, sin marca genérica). Fuente: snippet agregado de la colección https://pedrazailustracion.com/collections/laminas.
- Producto "Lámina 35 aves de Chile": acuarela de 35 especies de aves con nombre común y científico. Fuente: snippet de búsqueda "pedraza ilustración tienda online láminas Chile".
- Productos individuales detectados (sin precio): Lámina Mariposas de Chile (https://pedrazailustracion.com/products/lamina-mariposas-de-chile), Lámina Cetáceos de Chile (https://pedrazailustracion.com/products/lamina-cetaceos-de-chile-copia), Lámina Sietecolores (https://pedrazailustracion.com/products/lamina-sietecolores). Nota: una ficha titulada "Lámina Escarabajos de Chile" resuelve a la URL `/products/lamina-flores-de-chile-copia`, lo que sugiere una inconsistencia de indexación (título vs. slug) — 🟡 VERIFICAR cuál es el nombre/URL correcto.
- Packs de láminas (2 unidades, caja rígida protectora): "Pack Láminas Martín Pescador y Chucao" (https://pedrazailustracion.com/products/pack-laminas-loica-y-siete-colores-copia) y "Pack Láminas Loica y Siete Colores" (https://pedrazailustracion.com/products/pack-laminas-loica-y-siete-colores) — precios 🟡 VERIFICAR.

## 3. Presencia en marketplaces / reventa (fuera del sitio propio)

| Marketplace | Qué se encontró | Precio (si visible) | Fuente |
|---|---|---|---|
| Creado en Chile | Página de marca del vendedor + producto Puzzle Aves y Flores de Chile | $31.990 CLP (vs. $24.990–27.290 en el sitio propio → **markup de ~15–28% en este reseller**) | https://creadoenchile.cl/collections/vendors?q=pedraza+ilustraci%C3%B3n y https://creadoenchile.cl/products/puzzle-aves-y-flores-de-chile |
| Decatálogo | Página de colección de marca con múltiples productos: Bolso Aves, Libreta de Ave, Libreta de Flores, Puzzle Aves y Flores de Chile, Puzzle Mariposas y Escarabajos de Chile, Llavero Martín Pescador, y **"Libro Aves de Chile" firmado por MJ Pedraza** (producto no visto en el sitio propio — 🟡 VERIFICAR si es un producto vigente/descontinuado) | Rango agregado $8.790–$27.990 CLP | https://www.decatalogo.cl/collection/pedraza-ilustracion |
| Bazared | Fichas propias para Puzzle Cetáceos de Chile y Puzzle Hongos de Chile | 🟡 VERIFICAR (no se capturó precio) | https://www.bazared.cl/products/puzzle-ilustrado-cetaceos-de-chile-1000-piezas, https://www.bazared.cl/products/puzzle-ilustrado-hongos-de-chile-1000-piezas |
| Mercado Libre Chile | Ficha "Puzzle Pedraza Ilustración Flora y Fauna 1000 Piezas", con mención de "cuotas sin interés" | 🟡 VERIFICAR (no se capturó precio) | https://www.mercadolibre.cl/puzzle-pedraza-ilustracion-flora-y-fauna-1000-piezas/up/MLCU2815220982 |

**Lectura para el plan de crecimiento:** la marca ya tiene distribución multicanal más allá del sitio propio (al menos 4 marketplaces chilenos curados/de diseño local detectados). El caso de Creado en Chile muestra que el mismo producto se vende más caro fuera del sitio propio — dato útil para mensajes de "mejor precio en nuestra tienda" en Instagram. 🟡 VERIFICAR con el operador si estas relaciones de reventa son activas/vigentes, y si el catálogo/stock está sincronizado.

## 4. Propuesta de valor actual del sitio

- **Tagline / meta título del home:** "Pedraza Ilustración – Láminas, Puzles y Regalos Ilustrados Únicos". Fuente: https://pedrazailustracion.com/ (snippet de resultado de búsqueda).
- **Descripción agregada del negocio** (vía snippets de home y colecciones): ilustraciones originales y exclusivas de flora y fauna de Chile aplicadas a productos de decoración y regalo — láminas, puzzles, platos/loza, calcetines, bolsos, botellas y papelería. Fuente: snippets de https://pedrazailustracion.com/ y https://pedrazailustracion.com/collections/all.
- **Página "Quiénes somos"** (https://pedrazailustracion.com/pages/sobre-mi): María José Pedraza —descrita como ilustradora y fotógrafa— y Felipe Robinson —ingeniero comercial— son hermanos que fundaron el proyecto juntos. El propósito declarado es mostrar la biodiversidad chilena, con el objetivo de **educar y generar conciencia sobre la importancia de proteger el entorno natural**. Cada ilustración se describe como hecha a mano, inspirada en la naturaleza. Esto confirma textualmente el ángulo de educación/conservación mencionado en el brief, tal como lo comunica hoy el propio sitio.
- **Ángulo educativo aplicado a producto:** varias fichas (puzzles, láminas) incluyen explícitamente nombre común + nombre científico de cada especie, y en el caso de los puzzles una guía de referencia — el contenido educativo está integrado al producto físico, no es solo un mensaje de marketing.
- **Materiales/calidad como argumento de valor:** impresión FineArt/Giclée con papel Hahnemühle (premium) para las láminas; loza apta microondas/lavavajillas. Fuentes citadas arriba en catálogo.
- **Contacto:** cote@pedrazailustracion.com, según https://pedrazailustracion.com/pages/contact. **🟢 Confirmado por el operador (jul-2026): "Cote" es María José Pedraza**, y es ella quien responde hoy los mensajes (DMs) y los correos de este canal de contacto.

## 5. Envíos y mercados atendidos

- **Envío gratis Región Metropolitana (RM):** sobre compras de $50.000 CLP. 🟢 **Confirmado por Felipe (cliente), jul-2026:** este es el umbral vigente. (Snippet original agregado del home: https://pedrazailustracion.com/, vía búsqueda "envíos internacionales Latinoamérica".)
- **Envío a regiones:** se despacha a todo Chile; el costo y tiempo se calculan/muestran en el checkout según la comuna. Fuente: snippet de política de envío, https://pedrazailustracion.com/pages/contact (agregado con otras páginas de envío).
- **Santiago:** despacho en 1 a 3 días hábiles, según el mismo snippet.
- ✅ **RESUELTO — ya no es 🟡:** la ficha de producto individual (lámina) que mencionaba un esquema de envío distinto — $3.500 CLP dentro de Santiago, $5.990 CLP a otras regiones, y envío gratis sobre $30.000 CLP (fuente: snippet de https://pedrazailustracion.com/products/lamina-flores-de-chile-copia) — resultó ser una versión cacheada/desactualizada del sitio. **Felipe (cliente), jul-2026, confirma que el umbral vigente es $50.000 CLP**, no $30.000. Este caso concreto valida la advertencia metodológica de la nota al inicio del documento: los datos de este research vienen de caché de buscador y pueden estar desactualizados, tal como ocurrió acá.
- **Envíos internacionales:** no se encontró ninguna mención de envío fuera de Chile en ningún snippet indexado (búsquedas específicas por "envíos internacionales" y "Latinoamérica" no devolvieron resultados relevantes del dominio). Esto **no es evidencia concluyente de que no exista** envío internacional, solo de que no está indexado o no se promociona activamente. 🟡 VERIFICAR directamente con el operador si atienden pedidos fuera de Chile (relevante si la estrategia de Instagram busca audiencia internacional).
- **Regalos corporativos / mayorista:** el brief original y un snippet de búsqueda anterior mencionaron opciones para clientes corporativos y partnerships mayoristas, pero una búsqueda dirigida no devolvió resultados propios del dominio que lo confirmen con detalle — 🟡 VERIFICAR alcance real de esta línea B2B (¿existe una página dedicada, mínimos de compra, contacto distinto?).

## 6. AOV — referencia del operador 🟡 y estimación de contraste

### Dato nuevo: referencia del operador (23 de julio de 2026) — 🟡 dato de memoria, por confirmar

El operador aportó una referencia del ticket promedio (AOV — lo que gasta una persona en una compra) de memoria, de cuando trabajó directamente con el cliente: estaría "más o menos en los $60.000 CLP", con la advertencia textual del propio operador de que "tal vez sea menos ahora".

Este dato **no viene de un reporte de Shopify Analytics**, sino del recuerdo del operador. Se registra como **referencia del operador 🟡 (por confirmar con Shopify)**, no como un dato duro. Pasa a ser la referencia principal de trabajo del plan, en reemplazo de la estimación por precios públicos que se explica más abajo, pero sigue pendiente confirmarla con el reporte real de Shopify (ver sección 8 y `pendientes-operador.md`, ítem 1.2).

### Implicancia: pedidos al mes

Con la facturación reportada por el operador (~USD 5.000/mes ≈ **CLP 4.625.000/mes**, usando el tipo de cambio de referencia de $925 CLP/USD ya explicado más abajo) y el AOV de referencia de ~$60.000 CLP, el volumen de pedidos mensual implícito sería de aproximadamente **75 a 80 pedidos al mes (~2 a 3 pedidos por día)**.

Esta cifra **reemplaza** a la estimación anterior de 130 a 230 pedidos/mes (que se apoyaba en el AOV estimado por precios públicos, más abajo). Sigue siendo una doble inferencia (AOV de referencia × facturación reportada) y **no debe tratarse como dato duro** — solo como orden de magnitud para dimensionar campañas. 🟡

### Estimación anterior por precios públicos — se conserva como contraste, 🟡 SUPUESTO

Antes de tener la referencia del operador, y **sin acceso a datos reales de Shopify**, se había construido una estimación derivada a partir de los precios públicos del catálogo. Se conserva acá como contraste, porque la brecha entre ambas estimaciones es en sí misma una pista útil (ver más abajo):

1. **Dato confirmado por el operador (no derivado):** la tienda factura en promedio ~USD 5.000/mes (fuente: operador, julio 2026).
2. **Tipo de cambio de referencia:** USD/CLP se movió aproximadamente entre $919 y $932 CLP durante julio de 2026 (fuente: agregación de Wise y Bloomberg Línea vía búsqueda, https://wise.com/us/currency-converter/usd-to-clp-rate/history). Para este cálculo se usa **$925 CLP/USD** como punto medio redondeado — 🟡 SUPUESTO de tipo de cambio, no un dato puntual verificado para un día específico.
   → USD 5.000/mes ≈ **CLP 4.625.000/mes** de facturación promedio.
3. **Rango de precios observado en el catálogo (todos los precios con fuente en la sección 2):** desde $8.790 CLP (llavero) hasta $83.990 CLP (set de loza de 12 piezas), con la mayoría de los productos individuales confirmados concentrados entre **$9.000 y $29.000 CLP** (calcetines, llaveros, libretas, bolsos, botellas, puzzles).
4. **Supuesto de composición de carrito:** no hay evidencia pública de qué combinación de productos compra un cliente promedio. Asumiendo (🟡 sin evidencia directa, solo lógica de categoría) que el pedido típico de un e-commerce de regalos/decoración de este tipo incluye 1 a 1.3 unidades por compra (sin bundles obligatorios grandes, salvo los "packs" de 2 láminas que ya existen como producto único):
   - **AOV estimado por este método: rango CLP $20.000–$35.000 por pedido** (aprox. **USD 22–38** al tipo de cambio de referencia de julio 2026). Esta cifra ya **no se usa como referencia principal** del plan — queda documentada como el punto de partida antes del dato del operador.

### La brecha entre ambas estimaciones: hipótesis de carrito multi-producto — 🟡

La referencia del operador (~$60.000) queda muy por sobre la estimación por precios públicos ($20.000–$35.000). Una explicación posible — 🟡 **hipótesis de trabajo, sin evidencia directa todavía, no un hecho confirmado** — es que el carrito típico de un pedido en Pedraza Ilustración lleva más de un producto: por ejemplo, una lámina más una libreta de la misma serie. El catálogo facilita justamente esa combinación, porque las series por especie (aves, flores, mariposas, etc.) se repiten entre lámina, libreta, puzzle y plato. Esta hipótesis se retoma en `estrategia-nucleo.md` para el argumento del avatar (posicionamiento premium + empujar packs y carritos de varios productos).

**Qué NO se pudo estimar de forma responsable:** AOV real, tasa de conversión, tráfico del sitio, mix real de productos vendidos, LTV de cliente. Ninguna de estas métricas se intentó inferir por no contar con una base pública confiable — quedan en `pendientes-operador.md`.

## 7. Registro del playbook: qué funcionó y qué no

| Método | Resultado | Detalle |
|---|---|---|
| WebFetch a `https://pedrazailustracion.com/products.json?limit=250` | ❌ Falló | HTTP 403 — origen no determinado desde esta sesión (ver nota abajo) |
| WebFetch a `https://pedrazailustracion.com/collections/all/products.json?limit=250` | ❌ Falló | HTTP 403 — origen no determinado desde esta sesión |
| WebFetch a `https://pedrazailustracion.com/collections.json` | ❌ Falló | HTTP 403 — origen no determinado desde esta sesión |
| WebFetch a `https://pedrazailustracion.com/sitemap.xml` | ❌ Falló | HTTP 403 — origen no determinado desde esta sesión |
| WebFetch a `https://pedrazailustracion.com/robots.txt` | ❌ Falló | HTTP 403 — origen no determinado desde esta sesión |
| WebFetch al home (`/`) y a páginas de colección/producto individuales | ❌ Falló | HTTP 403 en todos los casos probados (home, `/collections/laminas`, `/products/lamina-mariposas-de-chile`) — origen no determinado desde esta sesión |
| `curl` directo desde bash (con User-Agent de navegador) | ❌ Falló | El proxy de egress de la sesión rechazó la conexión a `pedrazailustracion.com:443` con 403 a nivel de CONNECT ("policy denial or upstream failure"), es decir, el request nunca llegó al sitio. Confirmado con `curl http://127.0.0.1:34557/__agentproxy/status`, que registra el host en `recentRelayFailures` |
| **Prueba de control:** WebFetch y `curl` a `https://example.com/` | ❌ Falló igual que el dominio del cliente | Mismo 403 / "CONNECT tunnel failed, response 403" para un dominio neutro sin ninguna protección anti-bot. **Esto confirma que el 403 es un bloqueo de la política de red del entorno de trabajo (proxy de la sesión rechaza CONNECT a cualquier dominio externo), no un bloqueo del sitio de Shopify.** Ningún request de esta sesión llegó realmente a `pedrazailustracion.com` — por lo tanto no se pudo verificar de forma independiente el bloqueo anti-bot que reporta el operador en el brief |
| Proxy de lectura de terceros `r.jina.ai` (bypass común de 403 anti-bot) vía WebFetch | ❌ Falló | Mismo 403 — consistente con bloqueo de red del entorno, ya que `r.jina.ai` tampoco es Shopify ni tiene por qué compartir su protección anti-bot |
| WebFetch a fichas de reseller (mercadolibre.cl, bazared.cl) | ❌ Falló | HTTP 403 — mismo patrón que el dominio de control, consistente con bloqueo de red del entorno más que con protección anti-bot propia de cada reseller |
| **WebSearch con `site:pedrazailustracion.com`** | ✅ Funcionó | Devolvió URLs de colecciones y productos indexados, más un resumen agregado con precios extraídos de la caché del buscador |
| **WebSearch con queries dirigidas** (`pedrazailustracion.com [categoría] precio`, `"pedraza ilustración" [producto] precio CLP`) | ✅ Funcionó, fue el método principal | Esta fue la única vía que produjo precios y descripciones concretas. La cobertura fue desigual: algunas categorías (puzzles, accesorios, papelería, loza) devolvieron precios específicos; otras (láminas individuales, packs) devolvieron ficha técnica pero no precio |
| WebSearch de marketplaces (`creadoenchile.cl`, `decatalogo.cl`, `bazared.cl`, `mercadolibre.cl`) | ✅ Funcionó | Confirmó presencia multicanal y, en el caso de Creado en Chile, un precio de reventa más alto que el del sitio propio |

**Conclusión operativa para futuras fases de research sobre este cliente:** en esta sesión, **todo** el fetch directo a dominios externos (incluido un dominio de control sin relación con el cliente) fue bloqueado por la política de red del entorno de trabajo, no por el sitio. Por lo tanto **no corresponde asumir todavía** que `pedrazailustracion.com` tiene un bloqueo anti-bot propio — esa es una observación del operador citada en el brief, pendiente de confirmar de forma independiente. El siguiente paso correcto es **reintentar `products.json`, `collections.json` y el fetch directo del HTML desde una red sin esta restricción** (otra sesión/entorno con la política de red ampliada, o pidiendo al operador que habilite el dominio). Si ese reintento también devuelve 403, recién ahí queda validada la hipótesis de bloqueo anti-bot de Shopify, y vale la conclusión de apoyarse en WebSearch dirigido por categoría/producto más un export/CSV del operador como única vía confiable. Hasta entonces, este documento se basó 100% en snippets de WebSearch por necesidad operativa de la sesión, no por una limitación confirmada del sitio.

## 8. Qué debería aportar el operador (para `pendientes-operador.md`)

- **Probar `products.json` / `collections.json` / fetch directo del sitio desde una red sin proxy restrictivo** (otra sesión, otro entorno, o con el dominio habilitado en la política de red) — en esta sesión el 403 fue causado por el proxy del entorno de trabajo (confirmado con un dominio de control), no verificado como bloqueo del sitio; este reintento es el paso pendiente antes de dar por buena la hipótesis de bloqueo anti-bot de Shopify que reportó el operador en el brief.
- Export de productos de Shopify (CSV o acceso admin) con precio, stock y categoría — para reemplazar los precios de este documento (obtenidos de caché de buscador) por datos verificados y completos, incluyendo las láminas individuales y packs sin precio confirmado aquí.
- ✅ RESUELTO — Confirmación de la política de envío vigente y el umbral de envío gratis real: **el umbral vigente es $50.000 CLP; el $30.000 que aparecía en una ficha de producto era caché desactualizada del buscador** (Felipe, cliente, jul-2026) — ver sección 5.
- Confirmación de si hacen envíos internacionales / fuera de Chile.
- Aclaración sobre la relación comercial vigente con los marketplaces detectados (Creado en Chile, Decatálogo, Bazared, Mercado Libre): ¿activa?, ¿catálogo sincronizado?, ¿quién fija el precio de reventa?
- Datos reales de AOV, número de pedidos/mes y mix de productos vendidos (Shopify Analytics) — para confirmar (o corregir) la referencia del operador de ~$60.000 CLP, dato de memoria 🟡 (sección 6), y reemplazarla por un número real.
- ✅ RESUELTO — Confirmación de quién es "Cote" (cote@pedrazailustracion.com): **es María José Pedraza, y es quien responde mensajes y correos hoy (confirmado por el operador, jul-2026)** — ver sección 4.
- Aclaración sobre la línea de regalos corporativos/mayorista: si existe hoy, con qué condiciones y a través de qué canal se gestiona.
- Confirmación/actualización del catálogo: si el "Libro Aves de Chile" (visto en Decatálogo) sigue vigente y por qué no aparece en las colecciones detectadas del sitio propio.
