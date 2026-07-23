# Pendientes del operador — Fase 0

**Fecha:** 23 de julio de 2026
**Para quién:** María José Pedraza / Felipe Robinson (o quien administre Shopify, Instagram/Meta Business Suite y, más adelante, Amazon Seller Central).
**Por qué existe esta lista:** en esta ronda de research, todo intento de lectura directa de las páginas propias (Shopify, Instagram, Facebook) y de referencia (Amazon, Meta) fue bloqueado por la política de red del entorno de trabajo — confirmado con dominios de control neutros que dieron el mismo error. Todo el research (`tienda.md`, `instagram.md`, `mercado-tendencias.md`) se construyó por lo tanto con snippets de buscador, no con datos verificados en vivo. Esta lista reúne todo lo que **solo el operador puede conseguir** (capturas, exports, confirmaciones internas) para reemplazar esos datos débiles (🟡) por datos duros antes de avanzar a la siguiente fase del plan.

Los **5 ítems más urgentes** están marcados **[PRIORIDAD]** — son los que bloquean decisiones de calendario o de inversión si no se resuelven pronto.

---

## 1. Shopify / tienda

| # | Qué se necesita | Para qué se usa en el plan | Formato sugerido |
|---|---|---|---|
| 1.1 | **[PRIORIDAD]** Export CSV de productos desde Shopify Admin (Productos → Exportar), con precio, stock y categoría de todas las colecciones, incluyendo láminas individuales y packs sin precio confirmado en `tienda.md` sección 2 | Reemplazar los precios de caché de buscador (potencialmente desactualizados) por el catálogo real; completar precios de láminas, packs y variantes que no se pudieron capturar | CSV |
| 1.2 | **[PRIORIDAD]** Confirmar el AOV real en Shopify Analytics → Reportes de ventas (últimos 12 meses idealmente). Referencia del operador: ~$60.000 CLP, dato de memoria que "tal vez sea menos ahora" — implica ~75-80 pedidos/mes (~2-3 al día) con la facturación reportada | Reemplazar la referencia del operador 🟡 y la estimación anterior por precios públicos de `tienda.md` sección 6 por el dato real de AOV, pedidos/mes y mix de productos vendidos; es la base para dimensionar cualquier proyección de campaña | Captura de pantalla o export CSV del reporte |
| 1.3 | Confirmación de la política de envío vigente y el umbral de envío gratis real | Se detectó una inconsistencia entre **$50.000 CLP** (mencionado en el home) y **$30.000 CLP** (mencionado en una ficha de producto individual) — `tienda.md` sección 5 | Texto (captura de la página de envíos o respuesta directa) |
| 1.4 | Confirmación de si hacen envíos internacionales / fuera de Chile | No se encontró mención indexada de envío internacional; relevante si la estrategia de Instagram busca audiencia fuera de Chile | Texto |
| 1.5 | Aclaración sobre la relación comercial vigente con los marketplaces detectados (Creado en Chile, Decatálogo, Bazared, Mercado Libre) — ¿activa?, ¿catálogo sincronizado?, ¿quién fija el precio de reventa? | Se detectó que Creado en Chile revende el mismo puzzle ~15-28% más caro que el sitio propio — dato útil para mensajes de "mejor precio en nuestra tienda" en Instagram, pero solo si la relación sigue vigente | Texto |
| 1.6 | Confirmación de quién es "Cote" (cote@pedrazailustracion.com) y si es el canal de atención al cliente actual | Saber quién responde DMs/mails hoy, relevante para diseñar flujos de automatización de DM (ver `mercado-tendencias.md` sección C.3.4) | Texto |
| 1.7 | Aclaración sobre la línea de regalos corporativos/mayorista: si existe hoy, con qué condiciones y a través de qué canal se gestiona | El brief y un snippet mencionan esta línea B2B pero no se confirmó con detalle (¿página dedicada?, ¿mínimos de compra?, ¿contacto distinto?) | Texto |
| 1.8 | Confirmación/actualización del catálogo: si el **"Libro Aves de Chile"** (visto en Decatálogo, firmado por MJ Pedraza) sigue vigente y por qué no aparece en las colecciones detectadas del sitio propio | Puede ser un producto descontinuado que sigue listado en un reseller, o un producto vigente no indexado en el sitio propio — afecta el catálogo completo a usar en contenido | Texto |
| 1.9 | Sesiones de tienda que llegan desde Instagram (Shopify Analytics → fuente de tráfico, o Google Analytics si está conectado) | Línea base de tráfico social→tienda antes de lanzar el plan, para poder medir el efecto de las nuevas iniciativas de contenido | Captura de pantalla o export |

---

## 2. Instagram / Meta

| # | Qué se necesita | Para qué se usa en el plan | Formato sugerido |
|---|---|---|---|
| 2.1 | **[PRIORIDAD]** Instagram Insights de los últimos 90 días (idealmente 12 meses) — alcance, impresiones, visitas al perfil, clics al link en bio, desglose por tipo de contenido (Reels vs. carrusel vs. foto única) | Línea base real de desempeño para comparar contra los benchmarks externos de `mercado-tendencias.md` sección C, y para diseñar el calendario de contenido con datos propios en vez de solo benchmarks | Export CSV (Meta Business Suite) o capturas de pantalla |
| 2.2 | **[PRIORIDAD]** Top posts por alcance y por guardados (mínimo 90 días, idealmente 12 meses para ver estacionalidad Cyber/Navidad/Día de la Madre) | Identificar qué formatos y temas ya funcionan con la audiencia propia antes de invertir en producción nueva; sirve para llenar la plantilla de bitácora de `mercado-tendencias.md` sección C.5 | Captura de pantalla o export CSV |
| 2.3 | **[PRIORIDAD]** Conteo actual de seguidores de @pedraza_ilustracion y evolución histórica si está disponible (Meta Business Suite muestra crecimiento neto por período) | No se encontró en ningún resultado de búsqueda indexado (`instagram.md` sección 1); es el número base para cualquier objetivo de crecimiento del plan | Captura de pantalla |
| 2.4 | Texto completo de la bio actual y el/los link(s) en bio | No se pudo extraer por fetch bloqueado; necesario para saber el punto de partida del mensaje de marca y si usan Linktree/Linkin.bio | Captura de pantalla o texto copiado |
| 2.5 | Confirmación de cuál página de Facebook está activa — aclarar si `facebook.com/Pedraza-ilustracion-110551071531777` y `facebook.com/p/Pedraza-ilustracion-100077451231202` son la misma página o hay una duplicada/abandonada — y su conteo real de seguidores/me gusta (se encontró "495 likes" sin verificar) | Evitar duplicar esfuerzo de contenido en una página abandonada, y tener el dato real de audiencia en Facebook | Texto + captura de pantalla |
| 2.6 | Frecuencia real de publicación — capturas del feed ordenado por fecha o un export, para calcular cadencia real (posts/semana) | Los únicos datos disponibles hoy son 7 posts indexados por Google, insuficientes para inferir cadencia; se necesita para comparar contra la recomendación de C.4.1 (2 Reels + 3-5 posts/semana) | Capturas de pantalla del feed o export |
| 2.7 | Confirmación de si existen o no cuentas de marca en TikTok, Pinterest o YouTube (no se encontró evidencia pública, pero podrían existir sin indexar) | Definir si el plan debe incluir estas plataformas desde cero o simplemente activar cuentas ya existentes | Texto |
| 2.8 | Si lo tienen a mano, el listado/ficha de la marca en veredictas.com (`instagram.md` sección 3) — confirmar qué es ese sitio y si vale la pena mencionarlo como credencial | Evitar citar como "reconocimiento" algo que no se sabe con certeza qué es | Texto |

---

## 3. Amazon / marca

| # | Qué se necesita | Para qué se usa en el plan | Formato sugerido |
|---|---|---|---|
| 3.1 | **[PRIORIDAD]** Estado actual del registro de marca **"Pedraza Ilustración"** — ¿registrada, en trámite o no iniciada?, ¿en Chile, en EEUU (USPTO), o ambas? | Es la dependencia crítica y bloqueante de calendario para todo el anexo Amazon: sin marca registrada o en trámite no hay Brand Registry, y sin Brand Registry no hay A+ Content, Amazon Store, Amazon Attribution ni Brand Referral Bonus (`mercado-tendencias.md` secciones D.2.6 y D.4). El trámite puede tardar meses y debería iniciarse ya si se quiere "abrir pronto" en Amazon | Texto / documentación del trámite si existe |
| 3.2 | Modelo real del proveedor de Pedraza en EEUU: ¿fabricación bajo pedido (print-on-demand), stock propio, u otro esquema? ¿Puede operar bajo FBA, FBM, o híbrido? | El research de Amazon asumió "proveedor propio en EEUU" como antecedente pero no pudo validar el modelo exacto contra las rutas de mercado descritas (D.1.1, D.2.2, D.2.5 — incluida la exclusión de Amazon Handmade si la producción es tercerizada) | Texto |
| 3.3 | Método de pago/liquidación que usará o usa el proveedor en EEUU (cuenta bancaria en USD, Payoneer, u otro) | Amazon no exige banco en EEUU pero sí un método capaz de recibir liquidaciones en USD; si el proveedor ya tiene uno resuelto, evita duplicar gestión (`mercado-tendencias.md` sección D.2.4) | Texto |

---

## 4. Re-verificaciones con navegador (datos 🟡 que solo requieren abrir una página sin restricción de red)

Estos ítems no dependen de información interna del operador — son datos públicos que quedaron marcados 🟡 solo porque el fetch directo estuvo bloqueado en esta sesión de research. Se pueden resolver desde cualquier navegador normal, sin necesidad de acceso a sistemas internos.

| # | Qué se necesita | Para qué se usa en el plan | Formato sugerido |
|---|---|---|---|
| 4.1 | **[PRIORIDAD]** Reintentar `pedrazailustracion.com/products.json?limit=250`, `/collections.json`, `/sitemap.xml` y el HTML de colecciones/productos desde una red sin restricción de proxy | Confirmar de una vez si el catálogo completo, precios y stock se pueden leer en vivo — reemplazaría de raíz gran parte de `tienda.md` (hoy basado 100% en snippets de buscador) y resolvería si el 403 reportado por el operador es real o era el proxy del entorno de research | Export del JSON o confirmación de que sí/no funciona |
| 4.2 | Fecha de **CyberMonday Chile 2026**, que se espera se anuncie recién a fines de septiembre de 2026 (patrón de años anteriores) | Completar el calendario comercial de `mercado-tendencias.md` sección B.1, hoy marcado 🟡 VERIFICAR | Texto con fuente |
| 4.3 | Confirmar el **umbral exacto de inicio de Black Friday CL 2026** (27 nov según BlackFriday.cl/Wide Latam vs. 28 nov según la edición oficial CCS) | Resolver la pequeña discrepancia de fecha en `mercado-tendencias.md` sección B.1 antes de fijar el calendario editorial de noviembre | Texto con fuente |
| 4.4 | Confirmar la **fecha exacta de Cyber Monday EEUU 2026** (30 de noviembre según cálculo — lunes después de Thanksgiving — vs. 1 de diciembre según una fuente secundaria) | Resolver la discrepancia en `mercado-tendencias.md` sección D.5 antes de usar el calendario en decisiones de inventario/FBA | Texto con fuente |
| 4.5 | Verificar cifras de MMA/CONAF citadas en `mercado-tendencias.md` sección A.3: ~960 especies clasificadas como amenazadas/en peligro (MMA, año de corte sin confirmar) y 603.388 plantas nativas en viveros de macrozona sur a dic. 2025 (CONAF) | Estos datos alimentan ganchos de contenido de conservación; conviene citarlos con precisión si se usan públicamente en redes | Texto con fuente / captura del sitio oficial |
| 4.6 | Confirmar en `sell.amazon.com/pricing` y Seller Central los montos exactos vigentes de planes de venta, fees de FBA, recargo de combustible (3.5% desde abril 2026) y storage fees citados en `mercado-tendencias.md` sección D.2.3 | Estos montos cambian con el tiempo y afectan directamente el cálculo de margen antes de fijar precio en Amazon; Amazon mismo recomienda usar el Fee Preview Report de Seller Central, no cifras de terceros | Captura del Fee Preview Report o de la página de pricing |
| 4.7 | Confirmar si una marca registrada en Chile habilita Brand Registry en Amazon.com EEUU, o si se necesita trademark específico en USPTO — leyendo directamente `sell.amazon.com/brand-registry` | Depende parcialmente de 3.1, pero esta parte específica (¿aplica marca chilena?) es un dato público verificable con solo leer la página oficial sin restricción de red | Texto con fuente |
| 4.8 | Confirmar en `sellercentral.amazon.com/help` el umbral y la fecha exacta de la regla de etiqueta de devolución prepagada obligatoria para FBM (reportada desde febrero 2026) y los requisitos exactos de seguro de responsabilidad civil de producto (umbral de US$10.000/mes, 3 meses consecutivos) | `mercado-tendencias.md` sección D.2.2 y D.2.4 — condiciones operativas que afectan el modelo FBA/FBM híbrido propuesto | Texto con fuente |
| 4.9 | Confirmar el texto exacto de la política de reseñas de Amazon ("Community Guidelines" / "Product Review Policy") antes de diseñar cualquier insert de empaque | `mercado-tendencias.md` sección D.4.3 — este research se basó en resúmenes de terceros consistentes entre sí pero no leídos de la fuente primaria; un insert mal diseñado puede derivar en suspensión de cuenta | Texto con fuente |

---

## Notas de uso de esta lista

- Los ítems marcados **[PRIORIDAD]** son los que bloquean decisiones de calendario (registro de marca, fecha 2026) o que son la base numérica de todo el resto del plan (AOV/pedidos reales, Insights de Instagram, seguidores actuales). Conviene resolverlos antes de comprometer fechas de lanzamiento de campañas o de Amazon.
- El resto de los ítems mejora la precisión del research pero no bloquea el arranque de la Fase 1 del plan.
- A medida que se resuelva cada ítem, el dato correspondiente debería actualizarse directamente en `tienda.md`, `instagram.md` o `mercado-tendencias.md`, reemplazando el marcador 🟡 por el dato confirmado (no dejar ambos).
