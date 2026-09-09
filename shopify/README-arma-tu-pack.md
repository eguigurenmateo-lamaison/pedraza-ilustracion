# Arma tu pack de 3 puzzles — Guía rápida

## Qué hace la página

Es una página para pegar dentro de Shopify (en el `body_html` de una página de la tienda) donde el cliente:

1. Ve un catálogo de puzzles con foto, título, precio y cantidad de piezas.
2. Elige exactamente 3 tocando las tarjetas (el borde se pone verde, aparece un check y el texto cambia a "Elegido").
3. Ve en todo momento cuántos lleva ("2 de 3 elegidos"), con una barra de progreso.
4. Cuando completa 3, ve el precio final y cuánto ahorra, y el botón "Ir a pagar" se activa.
5. Al tocar "Ir a pagar", sale directo al checkout de Shopify con los 3 puzzles en el carrito.

La selección se guarda en el navegador del cliente (localStorage, clave `pedraza-pack:seleccion`), así que si recarga la página no la pierde.

Si intenta elegir un 4to puzzle con los 3 ya completos, no pasa nada en silencio: aparece el mensaje "El pack es de 3. Quita uno de los elegidos para cambiarlo." Si un puzzle no tiene stock, se ve en gris con la etiqueta "Agotado" y no se puede elegir.

## Cómo cambiar el descuento (tocando solo `PACK_CONFIG`)

Todo el precio y el copy que menciona plata sale de un solo objeto al inicio del `<script>`, dentro de `arma-tu-pack.html`:

```js
const PACK_CONFIG = {
  piezasPack: 3,
  modo: "porcentaje",        // "porcentaje" | "montoFijo" | "precioCerrado"
  porcentaje: 20,             // se usa si modo === "porcentaje"
  montoFijo: 16380,           // se usa si modo === "montoFijo"
  precioCerrado: 67176,       // se usa si modo === "precioCerrado"
  codigoDescuento: null,      // string o null
  envioGratisDesde: 50000
};
```

Cómo se usa cada campo:

| Campo | Qué controla | Cuándo se usa |
|---|---|---|
| `modo` | Cuál de las tres fórmulas de abajo se aplica | Siempre — decide el cálculo |
| `porcentaje` | % de descuento sobre la suma de los 3 puzzles elegidos | Si `modo: "porcentaje"` |
| `montoFijo` | Pesos CLP que se restan del total | Si `modo: "montoFijo"` |
| `precioCerrado` | Precio final fijo del pack, sin importar el % que represente | Si `modo: "precioCerrado"` |
| `codigoDescuento` | Si es un texto (ej. `"dsctopuzzle"`), se agrega `?discount=` al link de compra para que Shopify aplique ese código real de la tienda. Si es `null`, no se agrega nada | Siempre se revisa, sin importar el `modo` |
| `envioGratisDesde` | El monto que se muestra en la nota de envío gratis al pie de la página | Siempre |

**Ejemplo — para pasar a 30% de descuento:** cambiar `porcentaje: 20` por `porcentaje: 30`. No hay que tocar nada más: el precio final, el "ahorras $X (Y%)" y el botón se recalculan solos.

**Ejemplo — para usar el código real `dsctopuzzle`:** cambiar `codigoDescuento: null` por `codigoDescuento: "dsctopuzzle"`. Ojo: ese código, según `docs/research/shopify-puzzles-2026-09-09.json`, hoy da $3.000 fijos por pedido en Shopify — si se activa el código, conviene también poner `modo: "montoFijo"` y `montoFijo: 3000` para que el número que se muestra en pantalla coincida con lo que Shopify realmente va a cobrar en el checkout. Si el número mostrado y el del checkout no coinciden, el cliente lo va a notar.

**Ningún precio está escrito a mano en el HTML.** Se verificó con un script (ver más abajo): cero ocurrencias de `$` seguido de un número fuera de las funciones `formatoCLP()` / `formatoNumero()`.

## Tabla de variant IDs usados

Los 4 puzzles de 1000 piezas (todos al mismo precio de catálogo hoy, $27.990) más el Puzzle Naturaleza de 60 piezas, que el cliente confirmó que entra al selector. Fuente: `docs/research/shopify-puzzles-2026-09-09.json`, extraído el 2026-09-09.

| Producto | Variant ID | Piezas | Precio | Stock al extraer | Política sin stock |
|---|---|---:|---:|---:|---|
| Puzzle ilustrado – Aves y flores de Chile | `40651937120392` | 1.000 | $27.990 | 104 | CONTINUE |
| Puzzle ilustrado – Mariposas y Escarabajos de Chile | `41511835009160` | 1.000 | $27.990 | 13 | **DENY** (vigilar, es el stock más bajo) |
| Puzzle ilustrado – Cetáceos de Chile | `43097085182088` | 1.000 | $27.990 | 42 | CONTINUE |
| Puzzle ilustrado – Hongos de Chile | `43963478311048` | 1.000 | $27.990 | 27 | CONTINUE |
| Puzzle Naturaleza - 60 piezas | `44958020796552` | 60 | $18.990 | 36 | CONTINUE |

Cada ID se comparó uno por uno contra `id_numerico_variante` del JSON — los 5 coinciden exactamente. No se inventó ni se corrigió ninguno.

El Puzzle Naturaleza tiene precio y formato distintos a los otros 4 (60 piezas contra 1.000). En la tarjeta esto queda claro con la misma etiqueta de piezas que ya traían todas las tarjetas (arriba a la izquierda de la foto, ej. "60 piezas" o "1.000 piezas") — no se agregó ninguna sección ni filtro nuevo.

## Cómo se arma el link de checkout

```
https://pedrazailustracion.com/cart/ID1:1,ID2:1,ID3:1
```

y si `PACK_CONFIG.codigoDescuento` tiene un valor, se le agrega:

```
https://pedrazailustracion.com/cart/ID1:1,ID2:1,ID3:1?discount=CODIGO
```

Ejemplo real con los 3 primeros del catálogo:
`https://pedrazailustracion.com/cart/40651937120392:1,41511835009160:1,43097085182088:1`

Este permalink de esta tienda va directo al checkout (no hay carrito intermedio) — está verificado en vivo por el research, no es un supuesto.

## Qué actualizar si Pedraza agrega un puzzle nuevo

1. Conseguir del panel de Shopify (Productos → el puzzle nuevo → variante): el **variant ID numérico**, el **precio**, el **stock** y la **URL de la imagen** en `cdn.shopify.com`.
2. Agregar un objeto nuevo al array `PUZZLES` dentro del `<script>` de `arma-tu-pack.html`, con esa forma:
   ```js
   { id: "nombre-corto", variantId: 000000000, titulo: "Título real del producto", piezas: 1000, precio: 27990, stock: 50, imagen: "https://cdn.shopify.com/..." }
   ```
3. No hay que tocar nada más: la grilla, el conteo, el cálculo del precio y el permalink usan ese array automáticamente. El alt de la imagen se genera solo a partir del título y las piezas.
4. Si el puzzle nuevo tiene un precio distinto a los demás — como ya pasa con el "Puzzle Naturaleza - 60 piezas" ($18.990 contra $27.990 de los otros 4) — la lógica igual funciona: suma el precio real de cada elegido, no asume que los 3 cuestan lo mismo.
5. Si el nuevo puzzle puede quedar sin stock, no hace falta hacer nada extra: la página ya marca "Agotado" solo cuando `stock <= 0`.
6. **No usar la colección "Puzzles" de Shopify como fuente automática de datos.** El research confirmó que esa colección mezcla los puzzles reales con ~30 packs manuales y un producto mal etiquetado (un mazo de naipes). Hay que seguir agregando los puzzles a mano, uno por uno, con su variant ID verificado.

## Decisión que ya no queda pendiente

El JSON trae 5 puzzles. El constructor anterior había dejado fuera el "Puzzle Naturaleza - 60 piezas" ($18.990, variant ID `44958020796552`) por ser ambiguo (infantil, otra categoría de precio, sin confirmar con el cliente). El cliente ya confirmó que sí entra al selector, así que ahora está incluido junto a los 4 puzzles de 1000 piezas. El cálculo del pack ya sumaba el precio real de cada elegido (no asumía precio único), así que no hizo falta tocar la lógica de precios — solo agregar el producto al catálogo.

## Verificación antes de entregar

Corridas con `node` y en navegador sobre `arma-tu-pack.html` (y su copia idéntica en `preview-arma-tu-pack.html`):

- Variant IDs: **5 de 5 coinciden** con `id_numerico_variante` del JSON.
- Fragmento de `preview-arma-tu-pack.html` (entre `<body>` y `</body>`) comparado carácter por carácter contra `arma-tu-pack.html`: **idéntico**.
- Balance de tags (`div`, `span`, `p`, `button`, `svg`, `path`, `circle`, `h2`): **balance 0 en los 8**.
- IDs duplicados en el HTML: **0** (14 ids estáticos, todos únicos).
- Cifras de dinero escritas a mano fuera de `PACK_CONFIG`/`formatoCLP`/`formatoNumero` (patrón `$` + dígito literal): **0 ocurrencias**.
- Palabras prohibidas de la spec de copy ("última oportunidad", "no te lo pierdas", "quedan pocas unidades", "aprovecha", "solo por hoy", "colección cápsula", "drop", "edición limitada", "comunidad"): **0 ocurrencias**.
- Voseo rioplatense ("tenés", "querés", "tocá", "agregá", "elegí", etc.): **0 ocurrencias**.
- Emojis en el archivo: **0**.
- Prueba en navegador a 375px de ancho: `document.documentElement.scrollWidth === window.innerWidth` (375 === 375) → **sin scroll horizontal**.
- Prueba en navegador a 700px de ancho (grilla de 2 columnas): 5 tarjetas en el DOM, sin scroll horizontal (700 === 700); la 5ta tarjeta queda sola en su fila, comportamiento estándar de grilla responsiva, sin ruptura visual.
- Flujo probado en navegador: elegir el Puzzle Naturaleza (60 piezas, $18.990) + Aves ($27.990) + Mariposas ($27.990). Página muestra total `$59.976` y ahorro `Ahorras $14.994 (20%)`. Cálculo esperado a mano/con script: 2 × $27.990 + 1 × $18.990 = $74.970 subtotal; 20% de $74.970 = $14.994 de ahorro; $74.970 − $14.994 = $59.976 final — **coincide exacto**.
- Permalink de checkout para esa selección, verificado reproduciendo `armarPermalink()` con los datos reales del array `PUZZLES`: `https://pedrazailustracion.com/cart/40651937120392:1,41511835009160:1,44958020796552:1` — **contiene los 3 variant IDs correctos**.
