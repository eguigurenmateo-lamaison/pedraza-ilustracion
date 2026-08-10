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

## Actualización: la escala de valor nueva de Felipe (10-ago, misma tarde)

Felipe entregó `Escala_Valor_Pedraza-2026-08-10.xlsx` con **el costo real de los 13 productos**, que era el dato bloqueante, y **una lista de precios nueva, más baja**. 🟢 Confirmado por el operador: **es una propuesta, todavía no aplicada.** La lista vigente en la tienda sigue siendo la del 1-ago.

Verificado con `verificacion-escala-nueva.py` y `verificacion-costo-propuesta.py`:

- **La propuesta cuesta $3.779.283 al año** a volumen constante, sin contar láminas (no hay unidades desglosadas para ellas, así que el costo real es mayor). Exige vender **10,1% más unidades** solo para quedar igual.
- **Dos tercios de ese costo son puzzle ($2,06M) y botellas ($896K)** — justo los dos donde la baja no se sostiene.
- **Tres productos caen bajo el piso de 60%** que fijó Felipe: puzzle 60 (56,3%), botellas (59,0%), totebag (59,7%). Se arreglan con $19.990, $28.990 y $15.990.
- **El costo del puzzle subió** de $7.253 a $7.463 (+2,9%). Con el precio propuesto de $27.990 el margen queda solo 2,4% sobre julio.
- **El hallazgo de las láminas se da vuelta:** a los precios propuestos quedan en línea con el mercado (A2 pasa de 1,8× a 1,3× por cm² contra Mappin; A3 de +49% a +15% contra Torca). La lámina chica es **A3 (29,7×42)**, no 33×50 — 🟢 confirmado por el operador.
- 🔴 **Las dos hojas del archivo dan costos distintos para el mismo producto:** libretas $4.200 contra $7.235 (+72%), naipes +21%, pins −20%, lámina A2 +14%. Con un costo las libretas marginan 73,7% y con el otro 54,7%. Todos los cálculos publicados usan la hoja de Shopify.
- 🟡 **El archivo usa el dólar a $900**; el forecast del pedido a China usa $950.
- 🟢 **El archivo de Felipe calcula el margen sobre el precio neto**, correctamente. El error del IVA está en `descargas/calculadora-pedraza.xlsx`, que sigue sin arreglar.

### Un hallazgo nuevo: la zona muerta del envío gratis

Cruzar los $50.000 le cuesta $3.500 al negocio, y hay que sumar $4.346 más de venta para recuperarlo. **Todo pedido entre $50.000 y $54.346 deja menos plata que uno de $49.999.** Cualquier promoción que aterrice ahí trabaja en contra.

## Lo que falta

Ordenado por cuánto cambia la conclusión:

1. **Costo de las láminas y de los otros 8 productos.** Hoy solo el puzzle tiene costo real: es el 64% de las unidades sin margen calculable.
2. **Comisiones de pasarela de pago.** Pendiente desde el 1-ago.
3. **Costo real de envío por pedido.**
4. **Ventas del 1 al 10 de agosto por producto.**
5. **Precios de competencia verificados en vivo.**
6. **Cómo calcula Shopify el envío gratis** (antes o después del descuento).
