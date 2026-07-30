# Base de datos financiera — extraída de los archivos de Felipe (jul-2026)

Fuente: `Pedraza_Historico_Financiero_v7.xlsx` y los 5 archivos base que Felipe compartió el 29-jul-2026.
Periodo cubierto: **enero 2025 a junio 2026 (18 meses)**.
Todos los montos en pesos chilenos (CLP). Material interno; es la fuente de verdad numérica de los entregables.

---

## 1. Ventas por canal (18 meses)

| Canal | Ventas | % del total | Margen bruto |
|---|---:|---:|---:|
| Shopify | $111.013.953 | 54,9% | 79,1% |
| Mercado Libre | $993.961 | 0,5% | 60,7% |
| **E-commerce (Shopify + MELI)** | **$112.007.914** | **55,4%** | **78,9%** |
| B2B (BSALE) | $66.077.363 | 32,7% | 52,4% |
| Creado en Chile (cliente B2B) | $24.065.548 | 11,9% | 52,8% |
| **B2B total** | **$90.142.911** | **44,6%** | **52,5%** |
| **TOTAL** | **$202.150.825** | 100% | 67,1% |

**Lectura clave:** el e-commerce es poco más de la mitad de la venta pero con un margen bruto muy superior (79% contra 52%). El B2B aporta volumen; el e-commerce aporta margen.

## 2. E-commerce mes a mes (la base del variable del operador)

| Mes | Ventas | Utilidad bruta | Margen |
|---|---:|---:|---:|
| 2025-01 | $4.083.717 | $3.451.230 | 84,5% |
| 2025-02 | $3.497.684 | $2.755.907 | 78,8% |
| 2025-03 | $4.747.379 | $3.530.183 | 74,4% |
| 2025-04 | $5.974.294 | $3.920.338 | 65,6% |
| 2025-05 | $4.213.098 | $3.256.617 | 77,3% |
| 2025-06 | $6.848.022 | $5.195.310 | 75,9% |
| 2025-07 | $4.959.944 | $3.142.756 | 63,4% |
| 2025-08 | $4.451.542 | $3.396.676 | 76,3% |
| 2025-09 | $4.597.004 | $3.723.391 | 81,0% |
| 2025-10 | $6.276.101 | $5.185.257 | 82,6% |
| 2025-11 | $9.393.100 | $7.601.357 | 80,9% |
| **2025-12** | **$18.256.474** | **$15.008.193** | 82,2% |
| 2026-01 | $7.012.142 | $5.862.418 | 83,6% |
| 2026-02 | $4.537.674 | $3.825.225 | 84,3% |
| 2026-03 | $4.378.749 | $3.536.967 | 80,8% |
| 2026-04 | $7.523.809 | $6.062.571 | 80,6% |
| 2026-05 | $4.330.192 | $3.546.859 | 81,9% |
| 2026-06 | $6.926.989 | $5.405.693 | 78,0% |
| **TOTAL** | **$112.007.914** | **$88.406.944** | **78,9%** |

**Promedio: $6.222.662 de venta y $4.911.497 de utilidad bruta al mes.**
**Diciembre 2025 vendió 2,9 veces el mes promedio.** Es el mes que define el año.

## 3. Puzzles vendidos por canal y mes (unidades) — base del forecast

| Canal | Total 18 meses | Promedio/mes |
|---|---:|---:|
| Shopify | 1.096 | 61 |
| B2B | 733 | 41 |
| Creado en Chile | 490 | 27 |
| Mercado Libre | 42 | 2 (solo desde jun-2026) |
| **TOTAL** | **2.361** | **131** |

**Estacionalidad medida:** noviembre + diciembre 2025 sumaron **597 unidades** = **298/mes**, es decir **2,3 veces** el promedio. Diciembre 2025 solo: **367 unidades**, el mes más alto de la serie.

Por modelo en Shopify (18 meses): Aves 624 · Cetáceos 248 · Hongos 143 · Mariposas 81. **El puzzle de aves es el 57% de la venta de puzzles del canal.**

## 4. Estado de resultados consolidado (todos los canales)

| Concepto | 18 meses | Comentario |
|---|---:|---|
| Ventas totales | $202.150.825 | |
| Costo de mercadería | −$66.437.537 | 32,9% de la venta |
| Utilidad bruta | $135.713.288 | 67,1% |
| Gastos operativos | −$21.016.956 | ⚠️ solo 15 meses con datos |
| Utilidad operacional | $104.371.491 | ⚠️ **sobrestimada** (ver sección 5) |
| Gastos financieros (intereses) | −$2.514.498 | |
| Utilidad antes de retiros de socios | $101.856.993 | |
| Remuneración socios | −$42.924.543 | |
| Utilidad neta final | $58.932.450 | |

## 5. Los cuatro problemas del modelo (⚠️ verificar con Felipe)

**a) Los gastos variables solo están cargados en junio-2026.** En los otros 17 meses figuran en cero. Totales de 18 meses que no pueden ser correctos:
- Publicidad: **$973.425** (gastan aproximadamente eso en un solo mes)
- Packner / envíos: **$966.537** (para $202M de venta es imposible)
- **Comisiones de pasarela de pago: no aparecen en ninguna parte**

Consecuencia: la utilidad operacional está inflada. **El único mes con datos completos es junio-2026.**

**b) Posible doble conteo de "Creado en Chile" ($24M, 12% de la venta).** El propio correo de Felipe advierte que esa venta se repite entre archivos, pero en el modelo aparece como columna separada junto a B2B. Si las facturas de BSALE ya la incluyen, ventas y utilidad están infladas.

**c) Los retiros de socios distorsionan la última línea.** En 3 de 15 meses la utilidad neta final quedó en cero o negativa pese a haber utilidad operacional de millones:

| Mes | Antes de retiros | Retiro socios | Neta final |
|---|---:|---:|---:|
| 2025-07 | $3.666.615 | −$3.629.497 | $37.118 |
| 2025-08 | $3.048.300 | −$4.285.000 | −$1.236.700 |
| 2026-01 | $10.586.173 | −$10.592.000 | −$5.827 |

**d) No hay separación de gastos por canal.** Felipe ya identificó este pendiente: sin asignar gastos por vertical no se puede calcular la utilidad real del e-commerce.

## 6. Deuda vigente

Dos créditos FOGAPE a 36 cuotas:
- **Crédito 1:** ~$15,5M, cuota $553.198, tasa ~1,42% mensual. Desde jul-2025.
- **Crédito 2:** ~$17,6M, cuota $613.930, tasa ~1,33% mensual. Desde jun-2026.
- **Carga mensual combinada: $1.167.128.**

## 7. Gastos fijos por categoría (18 meses, sin servicio de deuda)

Total: **$14.051.893** (~$780.661/mes). Principales: Diseñadora $4.350.000 · Bodega $1.875.146 · Bsale $1.687.950 · Klaviyo $1.463.940 · ChatGPT $826.749 · Google Suite $786.554 · Pivot $703.688 · Adobe $570.684 · Contador $360.000 · resto (Apple, computador en cuotas, Freepik, Midjourney, apps Shopify) $1.427.182.

## 8. Inventario al 13 de julio de 2026

29 SKU repartidos entre **Packner** (despacha Shopify), **bodega propia** y **Mercado Libre**. Ejemplos: Naipes Aves 77 · Botella Aves 63 · Botella Hongos 50 · Bolso Playa Aves 32 · Calcetín Ave Gris 23 · Calcetín Aves Azul 9 · láminas con existencias muy bajas (entre 1 y 6 unidades por formato).

**Los puzzles están agotados** — es el quiebre que motivó el pedido a China.

## 9. Nota metodológica del modelo de Felipe

El modelo está bien construido y documentado: tres capas (datos crudos → lógica con SUMIFS → reporte), maestra de SKU, correcciones de mapeo documentadas, calendario de amortización de ambos créditos reconstruido y validado contra el banco, y separación correcta entre capital (no es gasto) e interés (sí lo es). El propio archivo declara sus brechas abiertas. Los problemas de la sección 5 son de **completitud de datos**, no de diseño.
