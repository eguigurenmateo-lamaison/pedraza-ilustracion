# Spec — Página "Elige 3 puzzles" para la tienda Shopify

Reconocimiento documental para construir la página del pack de 3 puzzles en la tienda Shopify real de Pedraza Ilustración. Cero invención: cada afirmación tiene su fuente. Lo no documentado queda marcado 🟡 con una pregunta concreta, no con un supuesto disfrazado de dato.

**Aviso de origen de las fuentes.** Al momento de escribir este documento, el checkout local de este repo estaba en la rama `pack-3-puzzles` (basada en `main`, commit `59f5bec`). Varios de los documentos pedidos —`descuento-escalonado-2026-09-08.md`, `upsell-carrito-2026-09-08.md`, `calendario-comercial-2026-09-08.md`, `reunion-2026-09-08.md`, `iva-publicidad-chile-2026-09-08.md`— **no existen en esa rama todavía**: viven, sin fusionar a `main`, en la rama `reunion-2026-09-08` (commit `bce4655`, "Acta del 8-sep y los cuatro pendientes que bloqueaban al equipo"). Se leyeron con `git show reunion-2026-09-08:docs/<archivo>` (lectura no destructiva, sin cambiar de rama). **Antes de construir la página, alguien debe fusionar esa rama a `main`/`pack-3-puzzles`** o el constructor no va a encontrar esos archivos en el checkout normal.

Convención: 🟢 dato con fuente en el repo · 🟡 no documentado / falta decidir · 🔴 contradice una decisión ya tomada.

---

## 0. Resumen ejecutivo (léase primero)

**La aritmética de $16.380 CLP de ahorro NO cuadra con ningún dato del repositorio.** No aparece ese número en ningún archivo, de ninguna rama (búsqueda `git grep` limpia). Ver sección 1.3.

**El mecanismo que describe el encargo — "el cliente elige 3 puzzles de un catálogo y obtiene un precio especial fijo" — choca con tres decisiones y hallazgos ya documentados:**

1. La reunión del 8-sep-2026 decidió explícitamente que el descuento del carrito "siempre en porcentaje, nunca en monto fijo" (cita textual de Cote, ver sección 1.4).
2. El mismo documento de la reunión registra que "los packs predeterminados ya se probaron antes y no salieron", y `docs/upsell-carrito-2026-09-08.md` es más específico: los packs armados "exigen elegir entre varias opciones... pedirle a alguien flojo que compare packs es lo contrario de dejarle la compra fácil" (ver sección 1.4 y 4).
3. El descuento que sí está decidido y en proceso de definir su porcentaje (30% recomendado, 40% en discusión) es un **descuento escalonado por unidad** (más caro cuantas más unidades, no un precio de pack cerrado), y está pensado como aplicable en el carrito normal de Shopify — no como una página aparte con selector de catálogo.

Esto no significa que la página no se pueda construir — significa que antes de construirla hay que resolver con el operador si esta página reemplaza, complementa o contradice el descuento escalonado ya decidido. Ver sección 4 para el detalle completo y las preguntas concretas.

---

## 1. La mecánica exacta del pack de 3

### 1.1 Precio unitario de referencia del puzzle

| Afirmación | Valor | Archivo fuente |
|---|---|---|
| Precio del Puzzle 1.000 piezas (el "puzzle" estándar de la tienda) | **$29.990 CLP** | `descargas/lista-precios-pedraza.xlsx`, hoja 1, fila "Puzzle 1.000 pzs", columna "Precio sugerido" = decisión de **mantener** el precio actual |
| Mismo precio confirmado como decisión final (no la baja que proponía Felipe a $27.990) | $29.990, marcado "Mantener" | `precio-venta.html`, líneas 1005 y 1571 |
| Costo puesto en bodega del puzzle | $7.463 (según Excel) **vs.** $7.253 (según el doc de descuento escalonado) — 🔴 **contradicción entre archivos**, ver sección 5 | `descargas/lista-precios-pedraza.xlsx` fila Puzzle 1.000 vs. `docs/descuento-escalonado-2026-09-08.md` sección 4 (rama `reunion-2026-09-08`) |
| Existe una segunda referencia de "puzzle": Puzzle 60 piezas, producto nuevo, sin precio "hoy" (recién se está lanzando) | **$18.990 CLP** | `descargas/lista-precios-pedraza.xlsx`, fila "Puzzle 60 pzs" |
| Catálogo real de diseños de puzzle (para saber qué hay para "elegir") | Aves (624 unid. vendidas en 18 meses), Cetáceos (248), Hongos (143), Mariposas (81) — el de Aves es el 57% de la venta de puzzles del canal Shopify | `docs/datos-financieros-2025-2026.md`, sección 3 |
| Referencia adicional de un puzzle nuevo aún no despegando en ventas ("puzzle de niños") | Sin precio propio confirmado en este documento — probablemente el Puzzle 60 pzs ($18.990), pero no está dicho explícitamente | `docs/reunion-2026-09-08.md` sección 3 (rama `reunion-2026-09-08`) — 🟡 confirmar con el operador si "puzzle de niños" = Puzzle 60 pzs |

**No existe en el repo un "precio del pack de 3" ya fijado.** No hay ningún producto tipo "Pack 3 Puzzles" en la lista de los 6 packs existentes (ver sección 1.4).

### 1.2 Reconstrucción de la aritmética, paso a paso

Partiendo del único precio de puzzle con costo real documentado ($29.990):

```
3 × $29.990 = $89.970   (precio de lista por 3 puzzles, sin descuento)
```

Para que el ahorro sea exactamente $16.380:

```
$89.970 − $16.380 = $73.590   (precio del pack que produciría ese ahorro)
$73.590 ÷ 3 = $24.530          (precio promedio por puzzle dentro del pack)
$16.380 ÷ $89.970 = 18,2%      (descuento efectivo sobre el total, si fuera %)
```

**Ninguno de estos tres números ($73.590 pack · $24.530 por unidad · 18,2% efectivo) aparece en ningún documento del repositorio.** Tampoco cuadra con el mecanismo que sí está decidido:

| Mecanismo documentado | Ahorro real en 3 puzzles de $29.990 | ¿= $16.380? |
|---|---:|---|
| 3ª unidad con 30% de descuento (**recomendación del análisis**, `docs/descuento-escalonado-2026-09-08.md` secc. 5 y 10) | $29.990 × 0,30 = **$8.997** | No |
| 3ª unidad con 40% de descuento (lo que proponía Felipe en la llamada) | $29.990 × 0,40 = **$11.996** | No |
| 3ª unidad con 50% de descuento (el techo que se descarta en el mismo doc) | $29.990 × 0,50 = **$14.995** | No, y ya está fuera del rango recomendado |
| 3ª unidad con 55% de descuento (hipotético, no está en ninguna tabla del repo) | $29.990 × 0,546 ≈ **$16.375** | Es lo más cerca que se llega, y es un número que nadie propuso |

**Conclusión:** $16.380 CLP no se deriva de ningún dato del repositorio con el precio de $29.990 por puzzle. Es un número que hay que preguntarle a quien lo dio (Mateo/Cote/Felipe) — quizás corresponde a otra combinación de productos (p. ej. mezclando puzzle + lámina + naipes, no 3 puzzles idénticos), a un precio de puzzle distinto al vigente, o simplemente a un número aproximado que se redondeó mal. 🟡 **Pregunta concreta para el operador: ¿de dónde sale el $16.380? ¿Es 3 puzzles al mismo precio, o una combinación de productos distintos?**

### 1.3 ¿Hay niveles del descuento escalonado?

Sí, están completamente descritos en `docs/descuento-escalonado-2026-09-08.md` (rama `reunion-2026-09-08`), sección 3 y 5:

| Unidades en el carrito | Descuento aplicado | Ahorro efectivo sobre el total (con 30% en la 3ª unidad) |
|---:|---|---:|
| 1 | Ninguno | 0% |
| 2 | Ninguno (el descuento parte en la 3ª unidad) | 0% |
| 3 | 30% sobre la 3ª unidad | 10,0% efectivo |
| 4 | 30% sobre la 3ª unidad (la 4ª paga completo) | 7,5% efectivo |
| 5 | 30% sobre la 3ª unidad (4ª y 5ª pagan completo) | 6,0% efectivo |

**El punto de quiebre técnico (techo absoluto) es 35%** — sobre ese porcentaje el análisis dice que "hay que regalar más de lo que se gana" (sección 5 y 10 del mismo doc). El 40% que propuso Felipe en la llamada solo se recomienda como ráfaga de 3 días en el Cyber, no como promoción permanente.

🔴 **Todavía no está decidido el número final.** El acta de la reunión (sección 5 y 11, doc `reunion-2026-09-08.md`) dice explícitamente: "Falta el número. Felipe tiene que confirmar si es 30% o 40% en la tercera unidad." **Esto es un bloqueador para construir cualquier página que muestre un precio de pack**, porque el precio depende de ese porcentaje.

### 1.4 ¿Aplica a todos los puzzles o hay exclusiones?

Dos fuentes se contradicen parcialmente aquí, y hay que leerlas juntas:

- **La reunión (decisión de la marca, 8-sep-2026):** "Combinable con cualquier producto de la tienda (Cote fue explícita en esto)." (`docs/reunion-2026-09-08.md`, sección 5)
- **El análisis de margen (mismo día):** recomienda restringir el descuento a **puzzles, láminas y naipes únicamente**, porque son las 3 únicas categorías con costo cargado y verificado; el resto del catálogo (9 de 11 categorías: botellas, calcetines, libretas, totebag, postales, llavero, pins, lámina 42×60, lámina 33×50) no tiene costo real, así que no se puede saber si el descuento pierde plata en esos productos (`docs/descuento-escalonado-2026-09-08.md`, sección 7). Además señala un problema técnico de Shopify: una promoción "lleva 3, paga menos" configurada de forma nativa aplica el descuento sobre la **unidad más barata** del carrito, lo que puede desinflar el descuento prometido si se mezcla con productos de bajo precio.

🔴 **Contradicción sin resolver entre lo que Cote pidió en la reunión y lo que el análisis de margen recomienda.** Para la página del pack de 3 puzzles esto importa menos si el pack es literalmente "3 puzzles" (todos dentro de la única categoría con costo confirmado), pero si más adelante se quiere abrir a "3 productos cualquiera", hay que resolver esta tensión antes.

### 1.5 ¿Monto fijo, porcentaje, o precio cerrado?

**Debe ser porcentaje, no monto fijo.** Cita textual de Cote en la reunión: *"combinable con cualquier producto... siempre en porcentaje, nunca en monto fijo, porque si no se van a llevar productos con los que salimos para atrás"* (`docs/reunion-2026-09-08.md`, sección 5). Esto es una instrucción explícita de la marca sobre **cómo tiene que estar configurado el descuento en Shopify** (por %, no por CLP fijo), independiente de cómo se comunique visualmente en la página (mostrar el ahorro en pesos es aceptable para el copy — mostrar "ahorras $X" es una traducción visual del %, no la configuración real).

Un **precio de pack cerrado** (ej. "3 puzzles por $73.590" fijo, sin importar el % que representa) no está prohibido explícitamente para packs (los 6 packs existentes sí son productos con precio de venta fijo, no un %), pero **si la intención de este encargo es que sea la misma promoción del descuento escalonado ya decidido**, entonces debe expresarse en % para cumplir la instrucción de Cote y no crear un segundo mecanismo de descuento en paralelo. 🟡 **Pregunta concreta: ¿esta página del pack de 3 es el mismo descuento escalonado que se está decidiendo (30% o 40% en la 3ª unidad), presentado con una interfaz de selección, o es una oferta nueva y distinta con precio de pack cerrado, como los 6 packs preexistentes?** La respuesta cambia todo el copy, el precio a mostrar y cómo se configura en Shopify.

---

## 2. El ángulo comercial y el copy

### 2.1 Traducción de la voz de Cote a instrucciones concretas para esta página

Fuente única: `CLAUDE.md`, sección "La voz de Cote". Traducción a reglas de copy accionables para esta página específica:

| Regla de CLAUDE.md | Instrucción concreta para el copy de esta página |
|---|---|
| "Le quita presión al lector en vez de ponérsela... nadie se queda sin puzzle" | El título y el copy de esta página NUNCA deben sonar a urgencia. No es "consigue tu descuento antes de que se acabe", es "esto es lo que cuesta llevar 3 en vez de 1" |
| Prohibido: "última oportunidad", "no te lo pierdas", "quedan pocas unidades", "aprovecha", "solo por hoy", cuentas regresivas | **Ninguna de esas frases, ni sus sinónimos, puede aparecer en el copy de esta página.** Tampoco un contador de tiempo ni un contador de stock ("¡solo quedan 4!") |
| Prohibido: jerga de marketing ("colección cápsula", "drop", "edición limitada", "comunidad", "storytelling") | Nombrar la oferta con palabras simples: "3 puzzles", "el pack de 3", "llévate 3". Nunca "colección", "edición", "drop" |
| Cero emojis en el cuerpo (aplica a texto firmado por la marca; una página de tienda puede usar íconos visuales del sistema de diseño, pero no emojis decorativos en el copy) | El copy de venta (títulos, descripciones, botones) sin emojis. Los indicadores visuales de estado de la interfaz (ver 2.3) pueden usar iconografía SVG/CSS, no emojis sueltos en el texto |
| Casi nunca signos de exclamación, cero preguntas retóricas | Frases declarativas, sin "¡Arma tu pack ahora!" ni "¿Ya elegiste tus 3 favoritos?" |
| Frases cortas, una idea por frase | Copy de la página en frases cortas, sin subordinadas largas |
| Voseo rioplatense prohibido (regla 4 de CLAUDE.md, aplica a todo el sitio) | Tuteo estándar: "elige", "agrega", "tu pack", nunca "elegí", "agregá" |
| Agradece sin adular; trata al lector como alguien que acompaña un proyecto | El copy puede agradecer por elegir 3 en vez de presionar a elegir 3 |

**Importante — esta página NO es un correo firmado por Cote.** Es una página de producto/oferta de la tienda, no un email. La sección de "La voz de Cote" en `CLAUDE.md` está escrita para correos, guiones y captions firmados con su nombre. Aun así, el resto de las reglas de comunicación de la marca (comunicar la urgencia como hecho logístico, nunca como amenaza; nada de jerga de marketing; tuteo estándar) son reglas generales de voz de marca que aplican a todo el sitio y por lo tanto también a esta página, aunque no vaya firmada "Cote". 🟡 Si el operador quiere que esta página SÍ tenga copy firmado por Cote (ej. una nota corta de ella explicando el pack), ahí sí aplican todas las reglas de estructura de correo/microcopy de esa sección.

### 2.2 Tres opciones de título y tres de subtítulo

Fieles a la voz (sin urgencia, sin jerga, tuteo estándar, frases cortas):

**Títulos:**
1. "Llévate 3 puzzles"
2. "El pack de 3 puzzles"
3. "3 puzzles, un solo pedido"

**Subtítulos** (dependen de qué mecánica se confirme — sección 1.5 — así que están escritos genéricos, sin el número de ahorro hasta confirmarlo):
1. "Elige tus 3 favoritos y paga menos por el conjunto."
2. "Cada puzzle que agregas baja el precio del pedido."
3. "Arma tu pedido con 3 puzzles y ahorra en el total."

🟡 **No se puede escribir el subtítulo final con el monto exacto de ahorro hasta resolver la sección 1.3 (el % final) y la sección 1.2 (por qué no cuadra $16.380).**

### 2.3 Microcopy por estado de la interfaz

| Estado | Qué necesita comunicar | Ejemplo de microcopy (tuteo estándar, sin exclamaciones, sin jerga) |
|---|---|---|
| Nada elegido | Invitar a elegir sin presión, dejar claro cuántos hacen falta | "Elige 3 puzzles para tu pack." |
| 1 elegido | Confirmar la elección, decir cuántos faltan, sin urgencia | "1 de 3 elegidos. Te faltan 2." |
| 2 elegidos | Igual que el anterior, un paso más cerca | "2 de 3 elegidos. Te falta 1." |
| 3 elegidos (completo) | Confirmar que el pack está listo, mostrar el precio final, habilitar el botón de checkout | "Tu pack de 3 está listo." + precio final visible + botón activo |
| Intento de elegir un cuarto | No es un error del cliente ni algo que reprenderlo — es información neutra sobre cómo funciona el pack | "El pack es de 3. Quita uno de los elegidos para cambiarlo." (nunca "no puedes agregar más" en tono de restricción dura; se explica como regla del pack, no como límite impuesto al cliente) |

Estas cuatro/cinco frases son una propuesta inicial siguiendo las reglas de voz — no son las frases finales de un correo de Cote, así que no necesitan pasar por la estructura de correo de la sección "La voz de Cote"; sí deben respetar sus prohibiciones (sin urgencia, sin jerga, sin exclamaciones).

### 2.4 El envío gratis: ¿aparece, y dónde?

**Sí debe aparecer, pero en segundo plano, nunca como argumento principal.** Razón documentada: `CLAUDE.md` dice explícitamente que "lo comercial (envío gratis, reseñas, plazos) va en la P.D., nunca en el cuerpo" (regla de estructura de correo, extensible como principio general de la marca: lo comercial no es el gancho).

Dato adicional importante para esta página específica: `docs/descuento-escalonado-2026-09-08.md` sección 6 (rama `reunion-2026-09-08`) señala que **con 2 puzzles ($59.980) ya se supera el umbral de envío gratis de $50.000** (`CLAUDE.md`, sección de contexto comercial). Esto significa que **el envío gratis no es un incentivo diferencial para llegar a 3 puzzles** — ya se obtiene con 2. El documento lo dice explícitamente: "la promoción del escalonado y el envío gratis se pisan... no hay que comunicarlos como dos beneficios que se suman, porque el segundo no agrega nada." **Recomendación para el copy: si se menciona el envío gratis, que sea una nota chica al pie o en un detalle secundario ("con 2 o más puzzles el envío ya es gratis"), nunca como parte del titular o el argumento de venta del pack de 3.**

---

## 3. El sistema de diseño

### 3.1 Distinción crítica antes de cualquier otra cosa

**Esta página se monta dentro de la tienda Shopify real (tema Astucia 7.0.1, según `docs/upsell-carrito-2026-09-08.md`, rama `reunion-2026-09-08`), no en el sitio interno del plan.** Dos consecuencias:

1. **Las imágenes de producto SÍ deben venir del CDN de Shopify** (`cdn.shopify.com`). Eso es correcto y necesario en este contexto — la regla de "cero recursos externos, cero CDNs" de `CLAUDE.md` aplica al **sitio del plan** (las páginas HTML de este repo, servidas por GitHub Pages, como `index.html`, `ofertas.html`, etc.), no a esta página de Shopify. El constructor no debe intentar incrustar las imágenes de los puzzles como base64 ni descargarlas al repo: debe referenciarlas desde el CDN de Shopify como cualquier otra página del tema.
2. **El sistema de diseño que se detalla abajo (`docs/design-system.md`) fue construido para las páginas internas del plan** (`index.html`, `kit-arranque.html`, `guion-reels.html`, `sop-dm.html`, `recursos.html`, `tablero.html` — ver el encabezado del propio documento), con una estética "curada, tipo iOS" que el operador diseñó para sus propios entregables. 🟡 **No hay ninguna confirmación en el repo de que la tienda real (tema Astucia) use esta misma estética, tipografía o estos radios/sombras.** Lo único confirmado como parte de la identidad visual real del cliente es el verde `#3B5751` (`CLAUDE.md`, sección "Reglas de contenido del operador": *"el sitio web del cliente usa el verde naturaleza #3B5751"*). El constructor debería, si es posible, revisar el CSS computado real del tema Astucia (tipografía, radios de botón, colores de fondo) antes de aplicar ciegamente los tokens de abajo, y usar el bloque de variables solo como punto de partida razonable, no como verdad absoluta del tema real.

### 3.2 Bloque de variables CSS (tokens reales del repo, listo para copiar)

Fuente: `docs/design-system.md`, sección 2 ("Bloque CSS canónico completo"), y confirmado también en el `<style>` de `tienda-cambios.html` (mismo bloque, verificado byte a byte por el QC del proyecto según `CLAUDE.md`).

```css
:root {
  color-scheme: light;

  /* tinta y superficies */
  --ink: #1c2420;
  --ink-soft: #4c5850;
  --ink-faint: #7c887f;
  --paper: #f4f2ed;
  --surface: #ffffff;
  --line: rgba(28, 36, 32, .08);
  --line-strong: rgba(28, 36, 32, .16);

  /* acento (color de acción) */
  --accent: #b0223f;
  --accent-dark: #7c1830;
  --accent-soft: #f8dfe4;

  /* verde de marca — CONFIRMADO como identidad real del cliente (CLAUDE.md) */
  --brand-green: #3b5751;
  --brand-green-soft: #e3eae8;
  --brand-green-dark: #2a403c;

  /* semántico */
  --success: #2f6b4a;
  --success-soft: #dcece1;
  --warn: #a8720a;
  --warn-soft: #f8ecd2;
  --danger: #ae3d17;
  --danger-soft: #f7ddd0;
  --info: var(--brand-green);
  --info-soft: var(--brand-green-soft);

  /* forma */
  --radius-xs: 8px;
  --radius-sm: 12px;
  --radius: 20px;
  --radius-lg: 28px;
  --radius-full: 999px;

  /* sombra */
  --shadow-xs: 0 1px 2px rgba(24, 32, 28, .04);
  --shadow-sm: 0 1px 3px rgba(24, 32, 28, .05), 0 4px 10px rgba(24, 32, 28, .05);
  --shadow: 0 6px 16px rgba(24, 32, 28, .07), 0 16px 32px -12px rgba(24, 32, 28, .14);

  /* espaciado */
  --space-1: .25rem;
  --space-2: .5rem;
  --space-3: .875rem;
  --space-4: 1.25rem;
  --space-5: 1.75rem;
  --space-6: clamp(2rem, 1.6rem + 1.6vw, 2.75rem);
  --space-7: clamp(2.75rem, 2rem + 3vw, 4.5rem);
  --space-8: clamp(3.5rem, 2.3rem + 5vw, 6rem);

  /* tipografía — pila de sistema, cero fuentes web */
  --font-sans: -apple-system, BlinkMacSystemFont, "SF Pro Text", "SF Pro Display", "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  --font-mono: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, monospace;
  --fs-sm: clamp(.85rem, .81rem + .2vw, .92rem);
  --fs-base: clamp(1rem, .95rem + .25vw, 1.0625rem);
  --fs-lg: clamp(1.1rem, 1.02rem + .4vw, 1.25rem);
  --fs-h3: clamp(1.2rem, 1.1rem + .5vw, 1.4rem);
  --fs-h2: clamp(1.5rem, 1.3rem + 1vw, 1.9rem);
  --fs-h1: clamp(2rem, 1.6rem + 2.4vw, 3rem);

  /* área táctil mínima (regla mobile-first del proyecto) */
  --tap: 44px;

  /* movimiento discreto */
  --ease: cubic-bezier(.4, 0, .2, 1);
  --dur: 200ms;
}

/* breakpoints usados en todo el sitio (mobile-first: base ≈ 375px) */
@media (min-width: 480px) { /* ... */ }
@media (min-width: 640px) { /* ... */ }
@media (min-width: 960px) { /* ... */ }
```

### 3.3 Patrones de componente ya existentes, útiles para reutilizar

| Componente | Clase | Qué hace | Fuente |
|---|---|---|---|
| Tarjeta genérica | `.card` | Superficie blanca, borde hairline, radio 20px, sombra suave — para cada puzzle seleccionable o para el resumen del pack | `docs/design-system.md` sección "10. Tarjeta genérica" |
| Badge / etiqueta | `.pill`, `.pill--success`, `.pill--warn`, `.pill--danger`, `.pill--info` | Etiquetas de estado en cápsula (ej. "3 de 3 elegidos", "te falta 1") | `docs/design-system.md` sección "14. Etiquetas" |
| Barra de progreso | `.progress`, `.progress__track`, `.progress__fill` | Ideal para mostrar visualmente "2 de 3 elegidos" como barra que se llena | `docs/design-system.md` sección "12. Barra de progreso" |
| KPI / número grande | `.kpi`, `.kpi__label`, `.kpi__value` | Para mostrar el precio final del pack de forma destacada | `docs/design-system.md` sección "9. KPIs" |
| Botón cápsula | `.btn`, `.btn--ghost` | El botón final "Ir a pagar" / continuar al checkout de Shopify | `docs/design-system.md` sección "17. Botones" |
| Tabla comparativa antes/después | `.compare-box`, `.compare-box--before`, `.compare-box--after` | Útil para mostrar "precio sin pack" vs. "precio con pack" lado a lado | `tienda-cambios.html`, líneas 651-657 (no está en el doc canónico de design-system, es un patrón adicional ya usado en el sitio) |
| Tabla responsive con scroll horizontal contenido | `.table-wrap` | Si se necesita una tabla comparando los 4 diseños de puzzle disponibles | `docs/design-system.md` sección "11. Tablas responsive" |
| Callout de aviso | `.callout`, `.callout--info/success/warn/danger` | Para la nota chica de envío gratis (sección 2.4) u otras aclaraciones menores | `docs/design-system.md` sección con `.callout` |
| Bloque copiable con botón "Copiar" | `.copyblock` | **No aplica a esta página** — es para texto que el operador copia y pega (bios, DMs). La página de Shopify no tiene ese caso de uso | `CLAUDE.md`, regla 6 |

### 3.4 Reglas duras del entregable (repetidas aquí porque aplican sin excepción)

- **Mobile-first, probado mentalmente a 375px de ancho antes de darlo por bueno.** El 92% del tráfico de esta tienda es móvil (`docs/upsell-carrito-2026-09-08.md`, paso 7 de la sección 6, rama `reunion-2026-09-08`) — no es una regla genérica del proyecto, es un dato real de esta tienda que la refuerza.
- **Área táctil mínima ~44px** en cada tarjeta de puzzle seleccionable y en el botón final (token `--tap: 44px`).
- **Cero dependencias externas, cero CDNs de terceros, todo CSS y JS inline en el propio archivo/bloque de la página** — esta regla sigue aplicando dentro de Shopify: no cargar librerías de gráficos, frameworks CSS ni fuentes web externas. La única excepción real y ya explicada es el CDN de imágenes de **Shopify** (`cdn.shopify.com`), que es parte de la propia plataforma, no un CDN de terceros.
- **localStorage, si se usa** (por ejemplo, para recordar la selección del cliente si refresca la página), debe llevar un prefijo propio y distinto de los ya usados en el sitio del plan (`pedraza-plan:` es del otro proyecto — para esta página de Shopify, que es un contexto totalmente distinto, no hace falta ni tiene sentido reusar ese prefijo; si el constructor decide usar localStorage aquí, que documente su propio prefijo, ej. `pedraza-tienda-pack3:`).

---

## 4. Riesgos y conflictos

### 4.1 Contradicciones entre documentos (con cita de cada fuente)

| # | Contradicción | Fuente A | Fuente B |
|---|---|---|---|
| 1 | Costo puesto en bodega del puzzle 1.000 piezas: $7.463 vs. $7.253 | `descargas/lista-precios-pedraza.xlsx`, fila "Puzzle 1.000 pzs", columna "Costo unitario" = 7463 | `docs/descuento-escalonado-2026-09-08.md` (rama `reunion-2026-09-08`), sección 4: "Costo puesto en bodega $7.253" |
| 2 | "Combinable con cualquier producto de la tienda" (decisión de Cote en la reunión) vs. la recomendación técnica de restringirlo a puzzles/láminas/naipes por falta de costo cargado en 9 de 11 categorías | `docs/reunion-2026-09-08.md`, sección 5 | `docs/descuento-escalonado-2026-09-08.md`, sección 7 |
| 3 | El encargo de esta página (precio de pack fijo, ahorro en CLP) vs. la instrucción explícita de que el descuento "siempre en porcentaje, nunca en monto fijo" | El brief de esta tarea ("obtiene un precio especial, ahorrándose $16.380 CLP") | `docs/reunion-2026-09-08.md`, sección 5, cita textual de Cote |
| 4 | El encargo de esta página (selector de catálogo, el cliente elige) vs. el diagnóstico ya documentado de que a este cliente ("es flojo") hay que evitarle elegir, y que los packs armados con elección "no salen" | El brief de esta tarea ("el cliente elige 3 puzzles de un catálogo") | `docs/upsell-carrito-2026-09-08.md`, tabla de la sección 1, fila "Carrito" — cita: "los packs armados, que exigen elegir entre varias opciones... ya se probó — 'no salen mucho'"; y `docs/reunion-2026-09-08.md` sección 4: "Los packs predeterminados ya se probaron antes y no salieron" |
| 5 | El $16.380 CLP del encargo no coincide con ninguna combinación documentada (30%, 40% o 50% de descuento en la 3ª unidad, sobre el precio real de $29.990) | Cálculo propio, sección 1.2 de este documento | `docs/descuento-escalonado-2026-09-08.md`, sección 3 |

### 4.2 Lo que falta definir antes de construir

1. **El % final del descuento escalonado** — Felipe todavía no confirmó 30% o 40% (`docs/reunion-2026-09-08.md`, sección 11, punto 2). Sin ese número, cualquier precio que se muestre en la página es un supuesto.
2. **Si esta página es el mismo mecanismo del descuento escalonado (presentado con una interfaz de selección) o una oferta nueva y distinta** — ver sección 1.5. Cambia todo: precio, copy, y si hay que configurarlo como un descuento de Shopify o como un producto nuevo tipo "pack".
3. **De dónde sale el $16.380 CLP** — no se encontró en ningún archivo del repo, en ninguna rama. Hay que preguntarlo directamente antes de construir cualquier copy con ese número.
4. **Si el pack es solo con el Puzzle 1.000 piezas ($29.990, 4 diseños: Aves, Cetáceos, Hongos, Mariposas) o también incluye el Puzzle 60 piezas ($18.990, producto nuevo, posiblemente el "puzzle de niños")** — mezclar precios distintos en un pack de precio cerrado complica la aritmética y no está resuelto en ningún documento.
5. **Compatibilidad con el descuento escalonado que se vaya a configurar en Shopify** — si el escalonado ya aplica automáticamente al llegar a 3 unidades de puzzle en el carrito normal, hay que decidir si esta página nueva es necesaria, redundante, o si reemplaza al mecanismo del carrito.
6. **Identificadores reales de Shopify** — este repositorio es de planificación y no contiene el código del tema Astucia, ni IDs de producto/variante, ni la estructura real del carrito/checkout de esta tienda específica. El constructor va a necesitar esos datos directamente desde el panel de Shopify (Productos → cada puzzle → ID de variante) para armar el enlace al checkout; no están documentados en ningún archivo de este repo.
7. **Confirmar visualmente el tema Astucia real** antes de aplicar los tokens de diseño de la sección 3 — ver 3.1, punto 2. No hay capturas ni CSS computado del tema real en este repositorio.
8. **Si el "puzzle de niños" mencionado en la reunión es el mismo SKU que "Puzzle 60 pzs"** de la lista de precios — no está dicho explícitamente en ningún documento.

---

## 5. Fuentes citadas en este documento (resumen)

- `CLAUDE.md` (raíz del repo)
- `docs/descuento-escalonado-2026-09-08.md` — vive en la rama `reunion-2026-09-08`, no en `main`/`pack-3-puzzles`
- `docs/upsell-carrito-2026-09-08.md` — idem
- `docs/reunion-2026-09-08.md` — idem
- `docs/calendario-comercial-2026-09-08.md` — idem
- `docs/modelo-ofertas-2026-08-02.md`
- `docs/design-system.md`
- `docs/datos-financieros-2025-2026.md`
- `descargas/lista-precios-pedraza.xlsx`
- `ofertas.html`, `precio-venta.html`, `cro.html`, `tienda-cambios.html`
