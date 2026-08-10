# Revisión de precios — 10 de agosto de 2026

Material interno. Es la fuente de verdad numérica de `precio-venta.html`.

## Por qué se hizo

El 1 de agosto se subieron los precios por comparación con la competencia. El 10 de agosto Felipe planteó lo contrario: *"en este momento estamos muy pasados, se nota en la demanda"*, y propuso bajar para competir. Esta ronda revisa esa hipótesis con costo real, margen real y precios de mercado.

## ⚠️ Limitación de método, importante

**La investigación de competencia se hizo sin poder abrir las páginas en vivo.** La política de red del entorno bloqueó el 100% de los dominios de retail (403 en el gateway: Falabella, Mercado Libre, bendito.cl, torcachile.cl, mappin.cl, la API de Mercado Libre). Se verificó de forma independiente antes de aceptar el diagnóstico.

Consecuencia: **todo precio de competencia en estos documentos viene del índice de un buscador, no de la ficha en vivo.** El índice está demostrablemente atrasado — muestra el puzzle de Pedraza a su precio anterior al 1-ago. Sirven para acotar la banda y saber dónde mirar; **no para fijar un precio final**. La lista de captura está en `precio-venta.html` y cierra la brecha en unos 15 minutos desde un equipo sin bloqueo.

La economía unitaria, en cambio, sale de datos internos y **no depende de la red**.

## Los documentos

| Archivo | Qué contiene |
|---|---|
| `economia-unitaria.md` | Costo por producto, cascada de margen, breakeven de bajas de precio, valor del alza del 1-ago |
| `competencia-puzzles.md` | Bandas de precio de puzzles en Chile por segmento |
| `competencia-catalogo.md` | Láminas, botellas, naipes y accesorios contra el segmento diseño |
| `canal-mercadolibre.md` | Costos del canal y qué queda realmente al vendedor |
| `canal-b2b.md` | Descuento mayorista por tipo de comprador y canibalización |

## Verificación cruzada

Cada informe se verificó de forma independiente antes de publicarse. Lo que pasó y lo que no:

- 🟢 **Los 16 porcentajes de alza del 1-ago**: los 16 cuadran.
- 🟢 **Margen del puzzle 71,2%** (no 78,9%): confirmado por dos caminos.
- 🟢 **Canibalización B2B** (2,3 y 3,4 unidades): confirmado.
- 🟡 **Mercado Libre**: la aritmética es correcta pero no descontaba IVA. Corregido: la caja real por puzzle es $11.271, no $23.631.
- 🟡 **Láminas**: el "+95% contra Torca" no normalizaba superficie. Por cm² la brecha real es +49%. Lo que sí resiste: la 42×60 cuesta 1,8× por cm² lo que un 50×70 de la competencia.
- 🔴 **Cuatro errores encontrados en material ya publicado**, todos verificados a mano contra los archivos: la calculadora `.xlsx` calcula margen sobre precio con IVA; `campanas.html` anuncia un "antes $49.990" que nunca existió; las láminas ya están bajo el precio previo al alza; y varias promociones dejan el carro justo bajo el umbral de envío gratis.

## Lo que falta

Ordenado por cuánto cambia la conclusión:

1. **Costo de las láminas y de los otros 8 productos.** Hoy solo el puzzle tiene costo real: es el 64% de las unidades sin margen calculable.
2. **Comisiones de pasarela de pago.** Pendiente desde el 1-ago.
3. **Costo real de envío por pedido.**
4. **Ventas del 1 al 10 de agosto por producto.**
5. **Precios de competencia verificados en vivo.**
6. **Cómo calcula Shopify el envío gratis** (antes o después del descuento).
