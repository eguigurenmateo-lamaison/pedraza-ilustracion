# Reconocimiento de datos Shopify — Pedraza Ilustración (2026-09-09)

Fuente: MCP de Shopify conectado a la tienda "Pedraza Ilustración" (`pedrazailustracionmj.myshopify.com`, dominio público `pedrazailustracion.com`, moneda CLP). Todo dato marcado **NO DISPONIBLE** no pudo confirmarse; no se inventó nada. Se hicieron solo lecturas — ninguna mutación, creación ni borrado.

---

## 1. Catálogo de puzzles

### Cómo se buscó (para no dejar ninguno fuera)

| Método | Resultado |
|---|---|
| Texto "puzzle" | 43 productos (incluye los 5 puzzles reales + ~30 "Pack N puzzles..." + 1 producto mal etiquetado) |
| Texto "puzle" | 0 resultados |
| Texto "rompecabezas" | 0 resultados |
| `product_type:Puzzle` | 1 resultado (solo Cetáceos tiene ese campo seteado; el resto lo tiene vacío) |
| Colección "Puzzles" (handle `puzzles`, regla automática TAG=puzzle) | 26 productos |

### Los 5 puzzles individuales (productos reales, no packs)

| Título | Handle | Precio CLP | Variant ID (para el permalink) | Stock | Política sin stock |
|---|---|---|---|---|---|
| Puzzle ilustrado – Aves y flores de Chile (1000 piezas) | `puzzle-1000-piezas-aves-flores-chilenas` | $27.990 | **40651937120392** | 104 | CONTINUE (vende sin stock) |
| Puzzle ilustrado – Mariposas y Escarabajos de Chile (1000 piezas) | `puzzle-1000-piezas-escarabajos-mariposas-chilenas` | $27.990 | **41511835009160** | 13 | **DENY** (se corta la venta al llegar a 0) |
| Puzzle ilustrado – Cetáceos de Chile (1000 piezas) | `puzzle-1000-piezas-cetaceos-chilenos` | $27.990 | **43097085182088** | 42 | CONTINUE |
| Puzzle ilustrado – Hongos de Chile (1000 piezas) | `puzzle-ilustrado-hongos-de-chile-1000-piezas` | $27.990 | **43963478311048** | 27 | CONTINUE |
| Puzzle Naturaleza - 60 piezas (⚠️ distinto, ver riesgos) | `puzzle-naturaleza-60-piezas` | $18.990 | **44958020796552** | 36 | CONTINUE |

Todos: status `ACTIVE`, publicados en el canal Online Store (cada uno tiene `onlineStoreUrl` válido). Variante única "Default Title" en los 5 (sin opciones de talla/color). Ningún puzzle tiene `compareAtPrice` (no están en oferta individual hoy). Cantidad de piezas: **solo está disponible en el título del producto** — no existe un metafield numérico dedicado a "piezas", así que si el selector necesita ese dato estructurado hay que parsearlo del título o crearlo.

Imágenes principales (CDN Shopify), alt text de todas: **NO DISPONIBLE** (vacío en Shopify para las 5):
- Aves y flores: `https://cdn.shopify.com/s/files/1/0592/9530/1768/files/APW7380-Editar-Editar.jpg?v=1756948503`
- Mariposas y Escarabajos: `https://cdn.shopify.com/s/files/1/0592/9530/1768/files/APW7382-Editar-2.jpg?v=1756948482`
- Cetáceos: `https://cdn.shopify.com/s/files/1/0592/9530/1768/files/APW7385-Editar-Editar.jpg?v=1756948457`
- Hongos: `https://cdn.shopify.com/s/files/1/0592/9530/1768/files/Puzzlehongo_9709156f-2410-4766-9b1a-147281aef91b.jpg?v=1775594955`
- Naturaleza 60p: `https://cdn.shopify.com/s/files/1/0592/9530/1768/files/puzzlenaturaleza.jpg?v=1775069138`

Detalle completo (SKU, IDs numéricos y GID, colecciones por producto) está en el JSON adjunto.

---

## 2. Auditoría de descuentos

Se revisaron **todos** los descuentos automáticos y con código (activos, programados y expirados) vía GraphQL (`automaticDiscountNodes` + `codeDiscountNodes`).

### Relevantes para puzzles

| Título | Código | Tipo | Valor | Aplica a | Estado |
|---|---|---|---|---|---|
| dsctopuzzle | `dsctopuzzle` | Con código, monto fijo, una vez por pedido | **$3.000 CLP** (fijo, no por unidad) | Aves, Mariposas, Cetáceos (**excluye Hongos**) | ACTIVE |
| PUZZAVE2 | `PUZZAVE2` | Con código, monto fijo por artículo | **$1.395 CLP por cada** artículo elegible | Colección completa "Puzzles" (26 productos, incluye ruido) | ACTIVE |
| 37HOY | `37HOY` | Con código, BxGy 37% | Compra 1 (puzzle u otros) → 37% off en **otro** producto (llaveros, pins, libreta, naipes, bolsos) | Cross-sell, no aplica a un segundo puzzle | ACTIVE |

Automáticos relevantes: **ninguno** aplica a puzzles. El único automático de interés general es **envío gratis sobre $50.000 CLP** (Chile, activo desde 2026-04-10, sin fecha de término).

Todo lo demás (GRACIAS5/10/12/15, BIENVENIDO10/15, SECRETO, PAPA10, PEDRAZA10, cupones Judge.me por reseña, BxGy de calcetines/láminas, etc.) no tiene relación con los puzzles o está expirado.

### Las 3 preguntas obligatorias

**¿Existe ya un descuento pensado para llevar 3 puzzles?**
Solo parcialmente. `dsctopuzzle` apunta a 3 de los 4 puzzles grandes (Aves, Mariposas, Cetáceos — **no incluye Hongos**), pero no es una lógica "compra 3, ahorra X": se activa con **1 sola unidad** de cualquiera de esos productos en el carrito y da un descuento fijo de $3.000 CLP una vez por pedido. No fue diseñado como el descuento del pack de 3.

**¿Algún descuento produce un ahorro de exactamente $16.380 CLP al llevar 3 puzzles?**
**No.** Aritmética verificada en vivo:
- 3 × $27.990 = **$83.970**
- Con `dsctopuzzle`: $83.970 − $3.000 = **$80.970** (ahorro $3.000)
- Con `PUZZAVE2` en los 3 puzzles: 3 × $1.395 = $4.185 → $83.970 − $4.185 = $79.785 (ahorro $4.185)
- Ninguna combinación de descuentos vigentes llega a $16.380 de ahorro.
- Aparte, existen ~30 productos "Pack N puzzles..." creados a mano (precio fijo, no son descuentos) cuyo ahorro implícito va de $14.470 a $20.980 según la combinación (ver JSON), pero tampoco ninguno coincide con $16.380 exactos.

**¿El descuento es automático o requiere `?discount=CODIGO` en la URL?**
Es **con código**, no automático. Se probó en vivo el permalink:
`https://pedrazailustracion.com/cart/40651937120392:1,41511835009160:1,43097085182088:1?discount=dsctopuzzle`
El navegador fue redirigido directo a la pantalla de checkout mostrando **"Precio total $83.970" → "Precio rebajado $80.970"**, confirmando que:
1. Shopify sí aplica el código automáticamente cuando viaja como parámetro `?discount=` en la URL del permalink.
2. El ahorro real es $3.000, no $16.380.
3. El permalink de carrito de esta tienda **redirige directo al checkout**, no a una página de carrito intermedia.

---

## 3. Contexto para el checkout

- **Dominio confirmado**: `https://pedrazailustracion.com` (primaryDomain de Shopify, y coincide con `onlineStoreUrl` de cada producto). `pedrazailustracion.cl` **no cargó** en el navegador (falló/denegado) y no hay ningún `urlRedirect` registrado hacia o desde ese dominio — todo indica que **no existe o no está activo**. Usar `.com` para el permalink.
- **Formato de precio — ⚠️ inconsistencia real detectada**: la página de producto del tema muestra `$27,990` (**coma** como separador de miles), mientras que la pantalla de checkout de Shopify muestra `$83.970` (**punto** como separador de miles). Ambas sin decimales. Hay que decidir a cuál imitar en la página nueva.
- **Envío gratis**: sí, automático, sobre $50.000 CLP, solo Chile, sin fecha de término.
- **Páginas existentes** (handles, todas publicadas): `contact`, `sobre-mi`, `cambios-y-devoluciones`, `politica-de-envios`, `despachos`, `suscripcion`, `pedraza-ilustracion-us`. Ninguna choca con handles típicos para la nueva página del constructor de packs.

---

## 🟡 DUDAS Y RIESGOS

1. **No hay descuento de $16.380 CLP para 3 puzzles.** Si el proyecto asume que ya existe, hay que crearlo (automático o con código) o decidir el precio del pack de otra forma. Esto es el hallazgo más importante para quien construya la página: **no asumir que el número $16.380 ya está configurado en Shopify**.
2. **`dsctopuzzle` no cubre Hongos de Chile.** Si el selector permite elegir cualquier combinación de 3 entre los 4 puzzles grandes, y el flujo depende de este código, las combinaciones que incluyan Hongos no recibirán el descuento esperado.
3. **La colección "Puzzles" no es una fuente confiable** para poblar el selector automáticamente: contiene 26 productos, de los cuales solo 5 son puzzles reales; el resto son packs (mayoría DRAFT) y un producto mal etiquetado ("Juego Naipes Aves de Chile", que tiene tags `puzzle`/`puzzles` pero es un mazo de cartas). Si se automatiza la carga de productos desde esa colección, aparecerá basura. Recomendación: hardcodear los 4 (o 5) handles/variant IDs reales.
4. **"Puzzle Naturaleza - 60 piezas" es ambiguo.** Tiene tag `puzzle`, vive en la colección Puzzles, pero es un producto infantil de 60 piezas a $18.990 (vs. $27.990 de los 4 grandes de 1000 piezas). No está claro si debe ser una 5ª opción en el selector de "elige 3" o si debe excluirse. Falta confirmar con el cliente.
5. **Stock del puzzle de Mariposas y Escarabajos es bajo (13 unidades) y su `inventoryPolicy` es `DENY`** — a diferencia de los otros 3 puzzles que permiten venta sin stock (`CONTINUE`). Si se agota, el selector debe manejar ese caso (deshabilitar la opción), y es el más urgente a vigilar.
6. **Inconsistencia de formato de precio** (coma en la página de producto vs. punto en el checkout de Shopify) — confirmado en vivo, no es un supuesto. Definir cuál usar en la nueva página.
7. **Existen ~30 productos "Pack N puzzles..." ya creados a mano** (la mayoría en DRAFT, algunos ACTIVE como "Pack 3 puzzles Aves, hongos y cetáceos de Chile" a $65.490 y "Pack 2 puzzles" a $44.790). Ninguno es generado por un motor de descuentos; son productos de catálogo con precio fijo. Riesgo de duplicidad/confusión de precios si la nueva página dinámica coexiste con estos packs fijos — recomendable decidir si se archivan o se dejan como "packs curados" aparte del selector libre.
8. **No existe metafield estructurado de "cantidad de piezas"** — se obtiene solo parseando el título. Si se necesita mostrarlo de forma confiable y separada del título, hay que crearlo o seguir parseando texto (frágil si cambian los títulos).
9. **El permalink de carrito de esta tienda redirige directo a checkout**, no a una página de carrito. Confirmarlo es bueno (agiliza el flujo de "armar pack → pagar"), pero significa que no hay oportunidad de mostrar un resumen de carrito propio antes del checkout de Shopify — el resumen tiene que vivir en la página del selector, antes de generar el link.
10. **Alt text vacío en las 5 imágenes principales de los puzzles.** Si la nueva página reutiliza esas imágenes, no hay alt text real que copiar — habrá que escribirlo a mano (fuera del alcance de este reconocimiento de solo lectura).
11. **No se revisó exhaustivamente el resto de las +50 colecciones** más allá de la primera página (había `hasNextPage: true` tras las primeras 50). No debería afectar el catálogo de puzzles (ya cruzado por 4 métodos distintos), pero si se necesita el listado completo de colecciones para otro fin, falta paginar.
