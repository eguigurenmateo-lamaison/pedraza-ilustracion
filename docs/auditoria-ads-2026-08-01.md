# Auditoría de Google Ads y Meta — 1 de agosto de 2026

Auditorías corridas por el operador sobre las cuentas reales. Periodo: últimos 30 días (2 al 31 de julio de 2026).
Material interno. **Fuente de verdad para `ads.html`.**

---

## 1. El número real: lo que dice la caja, no la atribución

Se manejan tres cifras de retorno distintas y solo una sirve para decidir:

| Cifra | Valor | Qué es |
|---|---:|---|
| ROAS que reporta Meta | 5,93 | Lo que Meta se atribuye a sí misma |
| "ROAS" de la reunión | ~5,5 | Venta total ÷ inversión total (no es atribución) |
| **Retorno sobre venta neta real** | **4,58** | **Venta neta de IVA y envío ÷ inversión total** |

**El cálculo de caja (julio 2026):**

| Concepto | Monto |
|---|---:|
| Inversión publicitaria total | $919.649 |
| — Meta (incluye campañas pausadas) | $746.502 |
| — Google | $173.147 |
| Venta neta real (sin IVA ni envío) | $4.214.684 |
| Margen bruto al 72% | $3.034.573 |
| **Queda después de publicidad** | **$2.114.924** |

**Por pedido** (151 pedidos reales en julio):

| Concepto | Monto |
|---|---:|
| Costo publicitario por pedido | $6.090 |
| Utilidad bruta por pedido | $20.097 |
| **Queda por pedido** | **$14.006** |

🟢 El negocio publicitario es rentable y con holgura. El problema no es que la publicidad no funcione: es que está mal configurada y mal medida.

---

## 2. Las cuentas no cierran: la atribución se solapa

| Fuente | Compras | Valor |
|---|---:|---:|
| Meta dice | 105 | $3.816.810 |
| Google dice | 17 | $482.054 |
| **Suman** | **122** | **$4.298.864** |
| **Shopify real (julio)** | **151** | **$5.559.034** |

La publicidad se atribuye el **81% de los pedidos** y el **77% de la venta**. Quedarían solo **29 pedidos (19%)** para orgánico, correo y directo.

⚠️ **Eso es imposible.** El correo solo aporta cerca del 9% (≈14 pedidos) y la marca tiene 62.500 seguidores en Instagram que generan venta directa.

**Qué está pasando:** la misma venta la cuentan dos plataformas. La persona ve un anuncio en Instagram, después busca "Pedraza Ilustración" en Google, hace clic y compra. Meta se la atribuye por la vista; Google por el clic.

**Evidencia concreta:** de las 17 conversiones de Google, **7 vienen de buscar la marca por su nombre**. Esa es demanda que creó Meta y que Google se está anotando.

🟢 **Conclusión práctica: no se pueden sumar los retornos de las plataformas.** La única medición limpia es venta real de Shopify ÷ inversión total.

---

## 3. El píxel de Meta está contando compras de más

| Dato | Valor |
|---|---:|
| Eventos de compra del píxel (28 días) | 239 |
| — por navegador | 99 |
| — por servidor (API de Conversiones) | 144 |
| Pedidos reales de Shopify (28 días) | ~136 |
| **Ratio eventos ÷ pedidos reales** | **1,75×** |
| Ratio solo del servidor | **1,06×** |

🟢 **El canal de servidor por sí solo cuadra casi exacto con la realidad.** Los 99 eventos del navegador se están sumando encima en vez de deduplicarse.

Meta tiene una **advertencia activa** en el Administrador de Eventos: *"No se configuró la deduplicación para este evento"*.

**Por qué importa:** si el sistema cree que hay más ventas de las que hay, optimiza hacia el público equivocado y el retorno reportado queda inflado. Es la causa más probable de que Meta muestre 5,93.

También hay un píxel viejo sin actividad ("María José Pedraza - Píxel de Facebook", 0 eventos) que conviene limpiar.

---

## 4. Dónde rinde cada peso

| Plataforma | Inversión | % del presupuesto | Retorno atribuido |
|---|---:|---:|---:|
| Meta | $643.255 (campaña activa) | 79% | 5,93 |
| Google | $173.147 | 21% | 2,78 |

**Cada peso en Meta rinde 2,1 veces lo que rinde en Google.**

Dos matices importantes:
- El 5,93 de Meta está inflado por el problema de deduplicación.
- Google tiene el crédito del 5 de septiembre, que le duplica el rendimiento efectivo.

---

## 5. Google: el hallazgo que parece un error y no lo es

| | Gasto | Conversiones | Valor | Retorno |
|---|---:|---:|---:|---:|
| Productos marcados "agotado" (7) | $30.897 | 6,17 | $197.618 | **6,40** |
| Todo el resto | $142.250 | 10,83 | $284.436 | **2,00** |
| Cuenta completa | $173.147 | 17,00 | $482.054 | 2,78 |

🟢 **Los productos agotados son el 18% del gasto pero el 41% del valor, y convierten 3,2 veces mejor que el resto.**

**Por qué:** la gente busca el puzzle, hace clic, llega al sitio, lo encuentra agotado **y compra otra cosa igual**. El puzzle es el imán que trae al comprador aunque no sea lo que termina comprando.

⚠️ **La auditoría automática recomendaba cortar ese gasto. Es un error: sería cortar la mejor parte de la cuenta.** La acción correcta es arreglar el sincronizado de stock del feed.

Esto valida toda la apuesta de la preventa: hay demanda de puzzle empujando venta del catálogo completo, incluso sin producto disponible.

### Los otros problemas de Google

- **25 de 28 productos excluidos** del grupo de recursos "General" (89% del catálogo). Solo el puzzle de aves y flores recibe impresiones. Todas las láminas, llaveros, pines, botellas, calcetines, libretas, bolsos, naipes y postales están fuera.
- **No existe ninguna lista de palabras clave negativas.** $6.035 al mes se van en términos con cero ventas: djeco chile, funky zoo, toyng puzzle, puzzleshop cl, la puzzleria chile, puzzle la joven de la perla, puzzle a sheep.
- **Marca contra no-marca:** una conversión de marca cuesta $426; una sin marca cuesta $12.290. **29 veces más.**
- **Un solo grupo de recursos** llamado "General", sin separación por categoría.
- **70% de las impresiones caen en sitios de la red de display de bajo valor** (owlsquiz.com, cici9game.com, apktogame.com y similares).
- Segunda campaña ("Puzzle Cetaceos") detenida con $8.377 gastados y cero conversiones.

### La promoción que vence el 5 de septiembre

| Concepto | Valor |
|---|---:|
| Meta a alcanzar | $323.656 |
| Días disponibles (1-ago al 5-sep) | 35 |
| Presupuesto actual ($7.000/día) | $245.000 |
| **Falta** | **$78.656** |
| **Presupuesto necesario** | **$9.247/día** |

Con el crédito, $323.656 se convierten en $647.312 de medios: el retorno efectivo pasa de 2,78 a **5,57**, comparable a Meta. Vale la pena, pero **solo después de los arreglos estructurales**.

---

## 6. Meta: el remarketing que no existe

| Concepto | Monto | % |
|---|---:|---:|
| Presupuesto a público que ya conoce la marca | $644 | **0,10%** |
| Lo acordado en la reunión | $128.651 | 20% |
| **Diferencia sin usar** | **$128.007/mes** | |

🟢 **Hay 9 públicos personalizados y 19 similares ya construidos y prácticamente sin usar**, incluido uno de compradores de 730 días y otros de gente que agregó al carrito o inició el pago sin comprar.

⚠️ **Uno de los públicos similares caduca hoy** (5% de personas que vieron la web en 30 días) y otro en 62 días.

**Conexión directa con el problema de recompra:** solo el 7,2% de los clientes vuelve a comprar. El público para atacar eso ya está construido; simplemente no se usa.

### Estructura actual de Meta

- **Una sola campaña activa:** "MRZ | CONVERSION CBO", presupuesto $15.000/día.
- Dentro: 4 conjuntos. "CONVERSION|WINNERS" absorbe el 61% del gasto y está en aprendizaje limitado con un anuncio con error.
- Las otras 91 campañas están pausadas.
- **3 catálogos conectados**, solo uno en uso real ("Catálogo_Productos", 23 productos, todos elegibles). Los otros dos son duplicados heredados.
- **No existe campaña dedicada de venta por catálogo**; el catálogo se usa como una creatividad más.

---

## 7. Los anuncios ganadores históricos

| # | Anuncio | Formato | Gasto | Valor generado | Retorno | Compras |
|---|---|---|---:|---:|---:|---:|
| 1 | Campaña de compra Advantage+ | Catálogo | $2.884.416 | $13.233.782 | 4,59 | 412 |
| 2 | catalogo productos invierno | Carrusel/Catálogo | $1.132.524 | $8.347.672 | **7,37** | 263 |
| 3 | Puzzle aves video cayendo | Video | $1.135.786 | $7.983.251 | **7,03** | 214 |
| 4 | naipes video | Video | $980.200 | $6.633.392 | **6,77** | 211 |
| 5 | catalogo 1 públicos personalizado 30 días | Catálogo | $724.330 | $3.345.117 | 4,62 | 135 |
| 6 | **Preventa cetaceos** | Imagen estática | $236.326 | $1.826.252 | **7,73** | 56 |
| 7 | Nuevo anuncio de Ventas | Video | $281.013 | $1.735.537 | 6,18 | 57 |
| 8 | REEL \| CARTAS AVES | Video (Reel) | $283.226 | $1.608.002 | 5,68 | 44 |
| 9 | naipes video BOSQUE | Video | $227.357 | $1.604.280 | **7,06** | 50 |
| 10 | STATIC \| BOTELLA HONGOS AVES | Imagen | $325.746 | $1.550.796 | 4,76 | 38 |

### Tres lecturas que cambian decisiones

🟢 **"Preventa cetaceos" tiene el mejor retorno de todo el top 10 (7,73).** Ya hicieron una preventa antes, en marzo de 2025, y fue el anuncio más rentable de la historia de la cuenta. Es el precedente directo de la preventa del 6 de agosto.

🟢 **Los naipes aparecen tres veces entre los ganadores** (retornos 6,77 / 7,06 / 5,68). Llegan 1.000 unidades el 15 de agosto y son el único producto que Felipe dejó sin subir de precio. Anuncio probado + stock entrante + precio sin cambio.

🟢 **"Puzzle aves video cayendo": retorno 7,03 con 214 compras.** Coincide con que el puzzle de aves es el 47% de la venta de puzzles y que llegan 500 unidades.

### Formatos

Video es el **65,9% del gasto** y sostiene el mejor retorno con volumen real (el Reel del puzzle de aves cayendo llegó a 11,42). El catálogo rinde parejo (~7,4). Las imágenes estáticas muestran retornos altos pero con muy pocas compras, así que son ruido estadístico salvo el caso de la preventa.

---

## 8. El plan, en orden

**Primero lo estructural, que no cuesta plata.** Subir presupuesto sobre una cuenta mal configurada es echarle más plata a una cañería rota.

| # | Qué | Dónde | Por qué ahora |
|---|---|---|---|
| 1 | Configurar la deduplicación del evento Compra | Meta | Todo lo demás se mide mal hasta que esto se arregle |
| 2 | Revivir los públicos antes de que caduquen | Meta | Uno vence hoy |
| 3 | Desbloquear los 25 productos excluidos | Google | 89% del catálogo sin una sola impresión |
| 4 | Arreglar el stock del feed (no cortar el gasto) | Google | Son las fichas que mejor convierten |
| 5 | Crear la lista de palabras negativas | Google | $6.035/mes con cero ventas |
| 6 | Separar el grupo de recursos por categoría | Google | Hoy hay uno solo, no se puede saber qué funciona |

**Después, con la preventa andando (desde el 6 de agosto):**

| # | Qué | Monto |
|---|---|---|
| 7 | Llevar el remarketing al 20% | $128.651/mes |
| 8 | Revivir los tres anuncios ganadores | — |
| 9 | Subir Google a $9.247/día | para alcanzar $323.656 antes del 5 de septiembre |

---

## 9. Qué se mide de aquí en adelante

La métrica que manda **no es el retorno que reporta cada plataforma**, porque se solapan entre sí y el píxel está inflado.

**La única medición limpia:**

> venta neta real de Shopify (sin IVA ni envío) ÷ inversión publicitaria total

Hoy: $4.214.684 ÷ $919.649 = **4,58**.

Se calcula una vez por semana con datos de Shopify, no de las plataformas. Es la única cifra que no se puede inflar.
