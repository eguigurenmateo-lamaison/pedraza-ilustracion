# Correcciones de Felipe — 1 de agosto de 2026

Respuestas de Felipe a las 11 preguntas, más la base de Shopify corregida y la lista final de precios.
Material interno. **Este documento reemplaza los datos equivalentes de `datos-financieros-2025-2026.md`.**

---

## 1. La corrección más grande: la venta de Shopify estaba inflada 26%

**Lo que dijo Felipe:** *"La venta de Shopify está considerando IVA + envíos. Por lo que la venta está inflada en $111 millones, cuando debería ser $82 millones."*

**Verificado de forma independiente** sobre la base corregida, mismo periodo del modelo (enero 2025 a junio 2026, 2.950 pedidos pagados):

| Concepto | Monto |
|---|---:|
| Total cobrado al cliente | $110.572.581 |
| menos envío | −$12.812.550 |
| = producto con IVA | $98.232.561 |
| **÷ 1,19 = producto NETO** | **$82.548.371** |

El modelo registraba **$111.013.953**, que es prácticamente el total cobrado al cliente. Es decir, contabilizaba como venta el IVA y el envío.

🟢 **Cifra correcta de Shopify: $82.548.371 netos** (18 meses). Coincide con el $82M que estimó Felipe.

**Sobrestimación: $28.465.582 (26%).**

### Qué arrastra esta corrección

| Dato | Antes (incorrecto) | Corregido |
|---|---:|---:|
| Venta Shopify 18 meses | $111.013.953 | **$82.548.371** |
| Venta Mercado Libre | $993.961 | **~$835.262** 🟡 (mismo ajuste de IVA) |
| Venta total 18 meses | $202.150.825 | **~$173.526.000** |
| Margen bruto Shopify | 79,1% | **~72%** 🟡 (mismo costo sobre menos venta) |
| Ticket promedio | $37.900 bruto | **~$27.980 neto** |

⚠️ **Todos los márgenes del e-commerce estaban sobrestimados.** Sigue siendo un margen sano y muy superior al B2B (52%), pero la brecha entre canales es menor de lo que decía el modelo.

---

## 2. La base de Shopify corregida — el forecast estaba 64% corto

La base anterior mostraba una unidad por pedido con tickets de $88.000 y más. La corregida trae el detalle por línea.

| Dato | Valor |
|---|---:|
| Pedidos pagados | 3.101 |
| Unidades vendidas | 5.097 |
| **Unidades por pedido** | **1,64** 🟢 |
| Ticket promedio bruto | $37.450 |
| Ticket promedio neto (sin IVA ni envío) | ~$27.980 |

🟢 **El forecast de unidades usaba 1 unidad por pedido. Son 1,64.** La demanda de unidades es 64% mayor de lo calculado — dato central para decidir la cantidad del pedido a China.

### Unidades por categoría (18 meses)

| Categoría | Unidades | % |
|---|---:|---:|
| Puzzle | 1.837 | 36,0% |
| Calcetines | 682 | 13,4% |
| Naipes | 664 | 13,0% |
| Otros | 566 | 11,1% |
| Botellas | 320 | 6,3% |
| Pins | 298 | 5,8% |
| Llaveros | 268 | 5,3% |
| Totebags | 164 | 3,2% |
| Libretas | 154 | 3,0% |
| Postales | 144 | 2,8% |

El puzzle es el 36% de las unidades pero el **43% de la venta** ($44M de $103M con IVA): es el producto que más pesa.

### La tasa de recompra real es peor de lo que creíamos

| Clientes | Cantidad | % |
|---|---:|---:|
| Compraron 1 vez | 2.643 | 92,8% |
| Compraron 2 veces | 168 | 5,9% |
| Compraron 3 o más | 37 | 1,3% |
| **Total** | **2.848** | |

🟢 **Tasa de recompra sobre toda la base: 7,2%**, no el 10% del panel de Shopify (ese mide 30 días). **93 de cada 100 clientes compran una sola vez y no vuelven nunca.**

### Estacionalidad (unidades por mes)

| Mes | Unidades |
|---|---:|
| jul-2025 | 133 |
| ago-2025 | 188 |
| sep-2025 | 204 |
| oct-2025 | 297 |
| nov-2025 | 439 |
| **dic-2025** | **889** |
| ene-2026 | 315 |
| jul-2026 | 266 |

🟢 **Diciembre vende 3,3 veces un mes normal** (889 contra ~270). Noviembre 1,6 veces. La curva empieza a subir en octubre.

---

## 3. El pedido que llega el 15 de agosto — composición real

De la factura de la fábrica (imagen enviada por Felipe):

| Producto | Unidades | FOB unitario USD | Total USD |
|---|---:|---:|---:|
| Puzzle aves | 500 | $4,80 | $2.400 |
| Puzzle cetáceos | 350 | $5,80 | $2.030 |
| Puzzle hongos | 200 | $6,48 | $1.296 |
| Juego de cartas | 1.000 | $2,75 | $2.750 |
| Puzzle niños 60 piezas | 240 | $0 | $0 |
| **Total** | **2.290** | | **$8.476** |

- Puzzles para adulto: **1.050**. Con los de niños: **1.290 puzzles**. Más 1.000 juegos de cartas.
- Pago: 30% de anticipo ($2.944) + 70% contra entrega ($5.532).
- Los 240 puzzles de niños vienen **sin costo** 🟡 (verificar si es compensación por las piezas faltantes del pedido anterior).

⚠️ **Corrección a lo publicado:** el sitio decía "1.000 unidades, 500 de aves". Son **2.290 unidades en total**, de las cuales 500 son de aves. La proporción de aves sobre puzzles de adulto es 48%, consistente con el 47,3% que representa en la venta histórica.

---

## 4. El plazo real: 85 días

**Lo que dijo Felipe:** *"La orden con pago la hicimos el 22 de mayo. Por lo que fueron 85 días. Es la compra que más se nos ha demorado."*

Verificado: del 22 de mayo al 15 de agosto son exactamente 85 días.

⚠️ **Corrección a lo publicado ayer.** El sitio decía que con 90 días la fecha para cubrir todo noviembre había vencido el 27 de julio. Con el dato real de 85 días **la fecha es hoy, 1 de agosto — no venció**.

Fechas límite recalculadas (85 de tránsito + 7 de Partner = 92 días):

| Hito | Fecha límite | Días desde hoy |
|---|---|---:|
| Stock todo noviembre | **1 de agosto** | **hoy** |
| Black Friday (27-nov) | 27 de agosto | 26 |
| Navidad (20-dic) | 19 de septiembre | 49 |

**Lectura:** noviembre está al límite exacto y depende de que el pedido salga hoy o mañana. Black Friday y Navidad tienen holgura razonable.

---

## 5. Los demás puntos aclarados

| # | Pregunta | Respuesta de Felipe |
|---|---|---|
| 1 | ¿El costo de $7.253 del puzzle es FOB o puesto en Chile? | 🟢 **Puesto en bodega en Santiago.** Incluye FOB, provisión, seguro de carga, forwarder, desconsolidación y flete. |
| 3 | ¿Hay puzzles comprometidos con B2B para Navidad? | 🟢 **Ninguno comprometido aún**, pero saben que llegarán: clientes actuales (hoteles en temporada alta de verano) y compras corporativas. |
| 6 | ¿Dónde están las comisiones de las pasarelas de pago? | 🟡 **Pendiente.** Felipe confirmó que faltan y las va a buscar. |
| 7 | ¿"Creado en Chile" está contado dos veces? | 🟢 **No.** El consolidado de ventas tiene el detalle por tienda; el consolidado B2B tiene la factura hecha a partir de ese detalle. **La venta total son $24M netos**, contados una vez. |
| 10 | ¿Qué es "Pivot" ($703.688)? | 🟢 La plataforma que **integra Bsale con Shopify**. Gasto fijo legítimo. |
| 11 | ¿La asesoría de Amazon ($471.000) entra en estos números? | 🟢 **Aparte para efectos de margen** (es otra unidad de negocio), **pero la caja sale de la empresa**. Se excluye del margen y se incluye en el flujo de caja. |

### La pregunta 5 sigue abierta — y el pendiente es mío de aclarar

Felipe respondió: *"Tanto en la planilla Consolidado Compras y gastos 2025-2026 como en Pedraza_Historico_Financiero_v7 están cargados los gastos variables desde abril/2025."*

**Dónde está la diferencia:** yo leí `Pedraza_Historico_Financiero_v7.xlsx` en su hoja consolidada, y ahí las columnas de gasto variable están en cero en todos los meses salvo junio-2026, con totales de 18 meses de $973.425 en publicidad y $966.537 en Packner.

**Conclusión:** el dato existe en las planillas de origen pero **no se traspasó a la hoja consolidada**. No es información faltante, es un error de consolidación. Hay que pedirle a Felipe el nombre exacto de la hoja donde sí están cargados para rehacer el cruce.

---

## 6. Precios: Felipe cambió el criterio (y con razón)

La propuesta publicada era por tramos (10% / 7,5% / 5% según precio). **Felipe lo hizo por comparación con la competencia**, no por porcentaje escalonado:

> *"Más que hacerlo por un % específico o escalonado, fue por benchmark, viendo lo que está ofreciendo la competencia. Hay harta oportunidad de alza, estábamos muy competitivos y nosotros ofrecemos mayor calidad y diseño."*

**Es mejor criterio:** el porcentaje por tramo era una regla a priori; el benchmark usa lo que el mercado ya validó. La lista final manda.

### Lista final 🟢 (definida por Felipe)

| Categoría | Shopify hoy | Shopify final | Δ | Mercado Libre hoy | ML final | Δ |
|---|---:|---:|---:|---:|---:|---:|
| Botellas | $28.990 | **$32.990** | +13,8% | $30.990 | **$35.990** | +16,2% |
| Calcetines | $9.390 | **$9.990** | +6,4% | — | — | — |
| Naipes | $22.990 | **$22.990** | 0% | $24.990 | **$24.990** | 0% |
| Láminas 42×60 | $48.390 | **$52.990** | +9,5% | $51.990 | **$56.990** | +9,6% |
| Láminas 33×50 | $36.980 | **$40.990** | +10,8% | — | — | — |
| Libretas | $17.490 | **$18.990** | +8,6% | — | — | — |
| Llavero | $8.790 | **$9.990** | +13,7% | — | — | — |
| Pins | $5.490 | **$7.990** | +45,5% | — | — | — |
| Postales | $10.990 | **$11.990** | +9,1% | — | — | — |
| Puzzle | $27.290 | **$29.990** | +9,9% | $29.990 | **$31.990** | +6,7% |
| Totebag | $16.490 | **$17.990** | +9,1% | $17.990 | **$18.990** | +5,6% |

**Observaciones:**
- El posicionamiento por canal quedó consistente: **Mercado Libre siempre por encima de la tienda propia**, entre $1.000 y $4.000 más. Exactamente lo acordado en la reunión.
- **Los naipes quedan sin alza (0%)** y son el único producto sin cambio. Vale revisarlo: llegan 1.000 unidades el 15 de agosto y son el 13% de las unidades vendidas 🟡.
- **Los pins suben 45,5%**, de lejos el mayor salto. A $5.490 estaban muy por debajo del mercado.
- Casi todo termina en 990, consistente con la tienda.
