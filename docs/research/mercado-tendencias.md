# Mercado, tendencias y calendario comercial — Pedraza Ilustración

**Fecha de investigación:** 23 de julio de 2026
**Alcance:** mercado de e-commerce chileno y nicho de diseño/regalo con identidad local; calendario comercial chileno 2026-2027 y comportamiento del comprador por fecha; tendencias de contenido y algoritmo de Instagram 2025-2026; panorama de Amazon EEUU para una eventual "Rampa EEUU". Documento de Fase 0 del research para el plan de crecimiento Instagram → tienda de **Pedraza Ilustración** (marca chilena de productos ilustrados de flora y fauna nativa, tienda Shopify pedrazailustracion.com, IG @pedraza_ilustracion).

> **Nota metodológica común (aplica a todo este documento):** en esta sesión de investigación, la herramienta de fetch directo de páginas (WebFetch) y `curl` devolvieron sistemáticamente `403 Forbidden` — no solo en los dominios objetivo (pedrazailustracion.com, instagram.com, amazon.com, sitios de medios chilenos), sino también en dominios de control neutros sin relación con estos clientes (`example.com`, `en.wikipedia.org`, `web.archive.org`), confirmando que se trata de un bloqueo de la política de red del entorno de trabajo (el proxy de la sesión rechaza el CONNECT a cualquier dominio externo), **no** de una protección anti-bot específica de ninguno de los sitios investigados. Por lo tanto, **todo el contenido de este documento proviene de fragmentos indexados por buscadores (WebSearch)** — snippets, resúmenes automáticos y cachés de buscador — y no de una lectura directa y completa de las páginas fuente. Cada dato lleva su URL de origen en línea, pero esa URL debe entenderse como "fuente citada por el snippet", no como "página leída en vivo". Los datos que no pudieron triangularse con confianza razonable están marcados explícitamente `🟡 VERIFICAR` (dato con fuente pero sin verificación independiente) o `🟡 SUPUESTO` (inferencia o juicio propio sin dato directo) — ninguno de estos marcadores debe tratarse como dato confirmado. El detalle de qué técnicas de búsqueda funcionaron y cuáles no se consolida al final del documento, en "Registro del playbook".

---

## A. Mercado e-commerce Chile y nicho de diseño/regalo

### A.1 E-commerce en Chile: tamaño y crecimiento

- El comercio electrónico chileno **bordeó los US$ 10.000 millones en 2025** (cerca de $9,5 billones de pesos), con un crecimiento real superior al **9%** (11,6% nominal). Para **2026 la CCS proyecta otro avance de ~6%, hasta cerca de US$ 10.600 millones**. — [CCS, "Comercio electrónico bordeó los US$ 10 mil millones en 2025" (mar. 2026)](https://www.ccs.cl/2026/03/26/comercio-electronico-bordeo-los-us-10-mil-millones-en-2025/)
- **Penetración del e-commerce sobre el retail total: 12,6%** (estadísticas experimentales del Banco Central de Chile, 2025). Por categoría: **tiendas por departamento 16,1%**, **vestuario 14,5%**, **supermercados 8,6%**. — misma fuente CCS arriba.
- En el primer cuatrimestre de 2025 las ventas digitales ya sumaban **más de $2,5 billones**, señal de recuperación de niveles históricos tras la caída post-pandemia. — [CCS, "eCommerce en Chile 2025: ventas digitales recuperan niveles históricos"](https://www.ccs.cl/ecommerce/ecommerce-en-chile-2025-ventas-digitales-recuperan-niveles-historicos-con-mas-de-25-billones-en-el-primer-cuatrimestre/)
- El retail minorista total (todos los canales) alcanzó **$75,5 billones en 2025**, superando los niveles de 2021. `🟡 VERIFICAR` (fuente secundaria, no se pudo confirmar contra el reporte CCS original por bloqueo de acceso). — [DiarioEstrategia, "CCS: Ventas del sector minorista superan niveles de 2021"](https://www.diarioestrategia.cl/texto-diario/mostrar/5749411/ccs-ventas-sector-minorista-superan-niveles-2021-alcanzan-755-billones-2025)

**Categoría relevante para Pedraza: "juguetes, juegos y regalos"**
- Según el reporte **NubeCommerce Chile 2026**, la categoría **"Juguetes, juegos y regalos" ocupa el 3er lugar en facturación** dentro del ecosistema digital chileno, con **CLP $722.293.168 en ventas durante 2025**, impulsada por estacionalidad (los peaks en fechas clave compensan el ticket unitario más bajo). — [Tiendanube, "40 productos más vendidos en Chile en 2026"](https://www.tiendanube.com/blog/productos-mas-vendidos-chile/)
- Hay una tendencia de crecimiento en decoración para el hogar ("el interés por embellecer los espacios domésticos impulsa ventas de decoración"), pero no se encontró una cifra dura de % de crecimiento específico para esa categoría — `🟡 VERIFICAR` cifra exacta. Misma fuente Tiendanube arriba.

### A.2 El nicho: diseño de autor, identidad local y "regalo con historia"

**Hallazgo clave: Pedraza Ilustración ya no está sola en este nicho — hay una categoría consolidada de "regalo chileno con diseño e identidad local", con al menos un competidor directo bien establecido.**

- **Bendito (bendito.cl)**: tienda fundada en 2014, se define por "el amor a la raíz y a la flora, fauna y cultura chilena"; trabaja con ilustradores/naturalistas para representar el entorno natural en productos de regalo y decoración. Vende por: (a) sitio propio, (b) tienda física en **MUT** (Las Condes), (c) marketplace **paris.cl**, y (d) Instagram **@benditocl con ~45K seguidores** ("la tienda de los pajaritos"). Es el comparable más cercano a Pedraza en Chile. — [Bendito — Nosotros](https://bendito.cl/pages/nosotros) · [Puntos de venta](https://bendito.cl/pages/puntos-de-venta) · [Instagram @benditocl](https://www.instagram.com/benditocl/) · [MUT — Bendito](https://mut.cl/tiendas/bendito/)
- **Chilesilvestre.com**: tienda de nicho más "naturalista/científico" (guías de campo, cámaras trampa, productos de artesanos, libros de flora y fauna descargables). Es un competidor adyacente, más educativo/técnico que de regalo-decoración. — [Chilesilvestre — tienda](https://www.chilesilvestre.com/12-tienda-online-chile-flora-fauna-naturaleza-productos-venta)
- **Creado en Chile (creadoenchile.cl)**: marketplace que agrupa **más de 500 marcas chilenas** en categorías Diseño, Artesanía, Moda, Cuidado personal, Gourmet, Juguetes y Decoración. **Pedraza Ilustración ya tiene presencia ahí**, en la colección "Ilustraciones flora y fauna" (ver también `tienda.md`, sección 3, para el detalle de precios de reventa detectado en este canal). — [Creado en Chile](https://creadoenchile.cl/) · [Colección Ilustraciones flora y fauna (con productos Pedraza)](https://creadoenchile.cl/collections/ilustraciones-flora-y-fauna)
- **Pedraza ya es multicanal**: además de su Shopify propio (pedrazailustracion.com), vende en **Mercado Libre Chile** (ej. puzzle 1000 piezas Flora y Fauna) y en Creado en Chile. — [Pedraza en Mercado Libre](https://www.mercadolibre.cl/puzzle-pedraza-ilustracion-flora-y-fauna-1000-piezas/up/MLCU2815220982)

**Canales que usan las marcas de diseño chilenas:**
1. **Espacios físicos multimarca**: **MUT (Mercado Urbano Tobalaba)**, en Apoquindo con Tobalaba (Las Condes), funciona como hub de gastronomía + cultura + diseño, con marcas locales y ferias/exposiciones rotativas; premiado en 2025 por ULI Americas Awards. — [Chileando — MUT](https://chileando.contactchile.cl/es/2025/03/28/mut-gastronomia-cultura-y-diseno-en-el-corazon-de-las-condes/)
2. **Vístete Local**, marketplace financiado por FONDART que abrió espacio físico en MUT para visibilizar diseño de autor chileno (moda, con diseñadores de RM, Punta Arenas, Puerto Montt). Modelo instructivo aunque enfocado en indumentaria. — [Portal Metropolitano — Vístete Local](https://portalmetropolitano.cl/vistete-local-el-marketplace-que-busca-potenciar-el-diseno-de-autor-chileno-llega-a-mut-las-condes/)
3. **Marketplaces online**: Creado en Chile, paris.cl (multimarca), Mercado Libre.
4. **Ferias de ilustración/diseño** (evidencia de ecosistema activo, aunque específicas de nicho): **Safari** (colectivo con ~7 años organizando ferias de ilustración), **La Furia Ilustrada** (plataforma nueva dedicada a ediciones ilustradas), **Print Santiago**, **Santiago Ilustrado Festival**. — [Publishnews — La Furia Ilustrada](https://publishnews.es/nace-la-furia-ilustrada-una-nueva-plataforma-para-la-ilustracion-chilena/) · [Print Santiago](https://printstgo.cl/)
5. **Instagram / redes sociales** como vitrina y canal de venta directa (ver sección B.2, "Comportamiento del comprador", para el detalle de canales de compra y redes sociales).

**Sobre Ñam y Matria (pedido explícito del brief):**
- **Ñam** es un **festival gastronómico** (cocina, vinos, coctelería, productos ancestrales), no una feria de diseño/ilustración. Se realizó del **10 al 12 de abril de 2026** en el Parque Padre Hurtado, Santiago. No es un canal relevante para productos de diseño/regalo salvo eventualmente como evento de marca/branding gastronómico. — [Chile es tuyo — Festival Ñam 2026](https://chileestuyo.cl/eventos/festival-nam-2026/)
- **Feria Matria**: no se encontró fuente verificable que la vincule al ecosistema de diseño/ilustración chileno en 2026. `🟡 VERIFICAR` — puede tratarse de un evento de escala muy local/reciente que no indexa bien, o el nombre puede estar confundido con otro evento.
- Nota: **"Puro Diseño"**, que suena como candidata obvia, es en realidad una **feria argentina** (Buenos Aires), no chilena — se descarta. — [Puro Diseño](https://purodiseno.lat/)

### A.3 Conservación/naturaleza chilena como ángulo de marca

**Hallazgo clave: el propio Ministerio del Medio Ambiente (MMA) usa la ilustración como herramienta central de sus campañas de conservación — es una validación directa del ángulo de marca de Pedraza, no solo una tendencia adyacente.**

- Campaña **"¿Dónde están las especies?"** del MMA: tres ilustraciones estilo "busca y encuentra" para identificar fauna nativa clasificada como amenazada, con el lema *"cuando perdemos de vista el problema, perdemos de vista a los animales"*. — [Cooperativa Ciencia (oct. 2024)](https://www.cooperativaciencia.cl/medio-ambiente/2024/10/15/donde-estan-las-especies-mma-lanza-campana-para-visibilizar-fauna-nativa-amenazada/)
- Campaña **"Conoce tu fauna"** del MMA en estaciones de Metro de Santiago: libro ilustrado interactivo para niños sobre el valor de las especies nativas, su hábitat, costumbres e historia. — [MMA](https://mma.gob.cl/ministerio-del-medio-ambiente-lanza-campana-educativa-conoce-tu-fauna-en-estaciones-de-metro/)
- El **21° Proceso de Clasificación de Especies** del MMA está abierto a participación ciudadana. En Chile hay actualmente **cerca de 960 especies clasificadas como amenazadas, en peligro crítico o vulnerables**. `🟡 VERIFICAR` cifra exacta y año de corte — viene de una síntesis de búsqueda, conviene confirmar en el sitio oficial de clasificación. — [MMA — Clasificación de Especies](https://clasificacionespecies.mma.gob.cl/), [MMA — nota 21° proceso](https://mma.gob.cl/chile-avanza-en-la-proteccion-de-su-naturaleza-21-proceso-de-clasificacion-de-especies-ya-esta-abierto-a-la-ciudadania/)
- CONAF tiene un **Programa de Reforestación 2026**; a diciembre de 2025, los viveros de la macrozona sur mantenían **603.388 plantas de especies nativas (69,6% de su producción total)**. `🟡 VERIFICAR` — dato tomado de síntesis, no se pudo aislar el artículo exacto de CONAF por bloqueo de acceso. — [CONAF — tag conservación de la biodiversidad](https://www.conaf.cl/tag/conservacion-de-la-biodiversidad/)
- Proyecto educativo **"Sharks in Sight"**: distribuyó más de 800 libros a 260 organizaciones/colegios en 2025, llegando a todas las regiones de Chile (incluidas islas oceánicas) y 7 países — evidencia adicional de que el contenido educativo ilustrado sobre fauna chilena/marina tiene tracción institucional y de alcance. `🟡 VERIFICAR` fuente puntual (no se recuperó URL individual confiable en la búsqueda).

**Lectura para Pedraza:** el terreno de "ilustración + fauna/flora nativa + educación/conservación" ya está siendo cultivado activamente por el Estado (MMA, CONAF) como estrategia de comunicación pública. Esto valida el ángulo de marca y ofrece ganchos de contenido concretos y con fecha (ej. calendario de especies amenazadas, procesos de clasificación abiertos a la ciudadanía) que Pedraza podría referenciar o incluso co-narrar en redes, sin que sean campañas competidoras (son del sector público, no retail).

---

## B. Calendario comercial chileno 2026–2027

### B.1 Tabla de fechas comerciales

| Fecha comercial | 2026 (o próxima ocurrencia) | Estado | Fuente |
|---|---|---|---|
| **CyberDay** | **1–3 de junio de 2026** (00:00 lun. 1 a 23:59 mié. 3) — **ya ocurrió** | 🟢 Confirmado (evento pasado) | [El Mostrador](https://www.elmostrador.cl/datos-utiles/2026/05/31/cyberday-2026-confirman-la-fecha-exacta-para-comprar-en-chile-y-el-truco-para-evitar-estafas/), [BioBioChile](https://www.biobiochile.cl/noticias/economia/actualidad-economica/2026/05/26/durara-3-dias-anuncian-fecha-del-cyberday-2026-y-confirman-participacion-de-572-marcas-y-tiendas.shtml) |
| **CyberMonday** | Histórico 2025: **6–8 de octubre de 2025**. Fecha 2026 **no está anunciada** todavía (a 23 jul 2026) | 🟡 VERIFICAR fecha 2026 — usar como referencia la ventana de inicios de octubre | [CCS — CyberMonday 2025 rompe récord](https://www.ccs.cl/2025/10/09/cybermonday-2025-rompe-record-historico-ventas-superaron-los-us-450-millones/), [Cooperativa](https://www.cooperativa.cl/noticias/pais/consumidores/cyber-monday-2025-cuando-comienza-y-cuantos-dias-dura/2025-10-02/103207.html) |
| **Black Sale** (evento propio chileno, no confundir con Black Friday) | **30 de marzo – 5 de abril de 2026** — ya ocurrió | 🟢 Confirmado (evento pasado) | [El Dínamo](https://www.eldinamo.cl/pais/2026/03/25/black-sale-2026-ya-tiene-fecha-en-chile-mas-de-100-marcas-ofreceran-descuentos-de-hasta-70/) |
| **Black Friday** | **27 de noviembre de 2026** (edición Wide Latam / BlackFriday.cl, hasta el 30 nov). La **CCS** organiza una edición oficial paralela, con fechas reportadas ligeramente distintas (28 nov–1 dic) — hay pequeña discrepancia entre fuentes sobre el día exacto de inicio | 🟡 VERIFICAR día exacto de inicio (27 vs 28 nov), pero el rango "última semana de noviembre" está confirmado | [Rankia](https://www.rankia.cl/blog/mejores-tarjetas-credito-debito/7076084-black-friday-2025-chile-guia-completa-para-aprovechar-ofertas), [CCS — anuncio Black Friday oficial](https://www.ccs.cl/ecommerce/ccs-anuncia-su-black-friday-oficial-con-cientos-de-empresas-verificadas-georreferenciadas-y-descuentos-imperdibles/) |
| **Navidad** | **25 de diciembre** — fecha fija, la más importante del año en volumen de venta | 🟢 Fija | [UpSeller — fechas Mercado Libre Chile 2026](https://www.upseller.com/es/blog-article-522) |
| **Día de la Madre** | **10 de mayo de 2026** (segundo domingo de mayo) — coincidió este año con la fecha legal/decreto (algo que no pasaba desde 2020) — **ya ocurrió** | 🟢 Confirmado (evento pasado) | [T13](https://www.t13.cl/noticia/te-puede-servir/nacional/dia-madre-2026-que-dia-cae-por-que-cambia-cada-ano-chile-03-05-2026), [CNN Chile](https://www.cnnchile.com/pais/dia-de-la-madre-2026-que-significa-que-el-comercio-y-el-decreto-oficial-coincidan-este-ano/) |
| **Día del Padre** | Fecha oficial (decreto): **19 de junio**. Celebración comercial/familiar: **domingo 21 de junio de 2026** (tercer domingo de junio) — **ya ocurrió** | 🟢 Confirmado (evento pasado) | [El Mostrador](https://www.elmostrador.cl/datos-utiles/2026/06/19/es-el-19-o-el-21-la-fecha-exacta-del-dia-del-padre-2026-en-chile-para-que-te-organices/) |
| **Día del Niño** | **domingo 9 de agosto de 2026** (segundo domingo de agosto; el decreto oficial fija el tercer miércoles de octubre, pero el comercio celebra en agosto) — **próximo, aún no ocurre** | 🟢 Confirmado, aún por venir | [El Mostrador](https://www.elmostrador.cl/datos-utiles/2026/07/17/cuando-es-el-dia-del-nino-2026-en-chile-revisa-la-la-fecha-exacta-de-la-celebracion/), [BioBioChile](https://www.biobiochile.cl/noticias/servicios/explicado/2026/07/13/cuando-es-el-dia-del-nino-y-la-nina-2026-y-por-que-tiene-dos-fechas-en-chile.shtml) |
| **Fiestas Patrias** | **18–19 de septiembre** (feriados; el comercio/malls/supermercados cierran esos días). La **semana previa al 18** concentra el peak de venta | 🟢 Fija | [Academia Nubimetrics](https://academia.nubimetrics.com/fiestas-patrias-independencia-chile), [BioBioChile](https://www.biobiochile.cl/noticias/servicios/toma-nota/2025/09/18/como-funcionara-el-comercio-este-18-y-19-de-septiembre-por-fiestas-patrias.shtml) |
| **San Valentín** | **14 de febrero** — fecha fija, demanda concentrada en un solo día (a diferencia de los Cyber, que duran varios días) | 🟢 Fija | [G5noticias](https://g5noticias.cl/2026/02/13/san-valentin-dispara-la-logistica-en-chile-y-las-entregas-aumentan-hasta-99/) |
| **Vuelta a clases** | Año escolar 2026: docentes vuelven **lunes 2 de marzo**, estudiantes **miércoles 4 de marzo**. Calendario **2027 aún no publicado** por Mineduc a la fecha (jul. 2026) | 🟡 VERIFICAR fecha exacta 2027 | [24Horas](https://www.24horas.cl/te-sirve/fecha-inicio-clases-chile-2026-calendario), [Mineduc](https://www.mineduc.cl/ministerio-de-educacion-oficializa-el-calendario-escolar-2026/) |

**Nota de calendario:** de las fechas de arriba, a fecha de hoy (23 jul 2026) **ya pasaron** CyberDay, Black Sale, Día de la Madre y Día del Padre 2026. **Quedan por venir en 2026**: Día del Niño (9 ago), Fiestas Patrias (18-19 sep), CyberMonday (fecha no confirmada, ventana esperada octubre), Black Friday (27-30 nov aprox.), Navidad (25 dic). Esto es directamente accionable para planificar el calendario editorial/comercial del segundo semestre. (Para el calendario comercial de EEUU relevante a una eventual Rampa EEUU, ver sección D.5 — nótese que **CyberMonday CL** y **Cyber Monday EEUU** son eventos distintos, de países y fechas distintas: no confundirlos al planificar.)

### B.2 Comportamiento del comprador chileno en fechas de descuento

**CyberDay 2026 (evento más reciente, ya con resultados finales)**
- Ventas totales: **US$ 531 millones** (+1,4% vs. CyberDay 2025). — [Ex-Ante](https://www.ex-ante.cl/cyberday-2026-ventas-llegan-a-us531-millones-y-ticket-promedio-fue-de-us104-por-compra/), [CCS](https://www.ccs.cl/2026/06/04/cyberday-2026-cerro-con-mas-de-5-millones-de-transacciones-y-us-531-millones-en-ventas/)
- **5,1 millones de transacciones** (-4% vs. edición anterior — cayeron las transacciones pero subió el ticket promedio).
- **Ticket promedio: US$ 104 por compra** (~$93.000 CLP). Otra fuente reporta el gasto promedio en ~$92.000 CLP — diferencia menor, probablemente de redondeo/metodología. — [The Clinic](https://www.theclinic.cl/2026/06/04/cyberday-2026-uno-de-cada-cuatro-chilenos-compro-algo-durante-el-evento-y-el-gasto-promedio-supero-los-92-mil)
- **1 de cada 4 chilenos (25%)** compró algo durante el evento.
- Por categoría: mayor participación en grandes tiendas, seguido de líneas aéreas, operadores turísticos y supermercados; el **mayor crecimiento (+20% YoY) fue en supermercados**. — [Epicentro Chile](https://www.epicentrochile.com/2026/06/04/cyberday-2026-logra-ventas-por-us531-millones-supermercados-lideran-el-crecimiento/)

**CyberMonday 2025 (última edición completa, referencia para proyectar 2026)**
- Cerró con **récord histórico**: más de **US$ 450 millones** (~$430.000 millones CLP), **4,4 millones de transacciones**, +5% nominal vs. 2024 — el mayor nivel de ventas desde la creación del evento en 2011. — [CCS](https://www.ccs.cl/2025/10/09/cybermonday-2025-rompe-record-historico-ventas-superaron-los-us-450-millones/)
- **Ticket promedio ~$106.000 CLP** (+8% vs. 2024), con **fuerte variación por categoría**: turismo ~$600.000, muebles/electrónica ~$290.000, pasajes aéreos ~$280.000, supermercados y vestuario/calzado ~$75.000. Esto es relevante para calibrar expectativas de ticket en la categoría de regalos de Pedraza (más cerca del rango bajo). — [Diario Financiero](https://www.df.cl/empresas/retail/cybermonday-2025-parte-con-alza-de-18-en-sus-primeras-horas-y-supera-los)

**Día de la Madre 2026 — el evento comercial más grande del primer semestre**
- Se estima que movió **más de US$ 2.000 millones** en la semana previa (3–10 de mayo), un alza de más del 7% vs. una semana normal. Es el **5º evento comercial más relevante del año**, después de Navidad, CyberDay, CyberMonday y Black Friday. — [La Tercera](https://www.latercera.com/pulso/noticia/mama-hay-una-sola-dia-de-la-madre-2026-movera-mas-de-us-2000-millones-y-proyecta-cifras-record/)
- **Gasto promedio en regalos a nivel país: $25.329** (bajó de $27.650 en 2025). Con **fuerte brecha socioeconómica**: segmento ABC1 gasta en promedio **$43.447**, segmento DE solo **$18.793**. — [Puranoticia](https://puranoticia.pnt.cl/negocios/dia-de-la-madre-2026-gasto-promedio-cae-y-perfumes-lideran-preferencias-en), [Emol](https://www.emol.com/noticias/Tendencias/2026/05/10/1199519/dia-de-la-madre-percepciones.html)
- Categorías de regalo más elegidas: **perfumería 35,1%**, **chocolates/dulces 33,3%**, **ropa/calzado 29,5%**. Los productos de Pedraza (láminas, libretas, loza) no aparecen como categoría top-3, lo que sugiere que hay que posicionarlos explícitamente como alternativa de "regalo con significado" frente a las categorías dominantes. — [The Clinic](https://www.theclinic.cl/2026/05/08/como-viven-los-chilenos-el-dia-de-la-madre-los-presupuestos-regalos-y-panoramas-que-marcaran-este-2026/)

**Fiestas Patrias — relevancia baja para el nicho de Pedraza**
- El gasto se concentra en alimentos/parrilla (carnicería +37%, carbón +76%, más de 160.000 accesorios de parrilla vendidos en septiembre) y decoración de fiesta, no en regalos de diseño. **63% de las compras las hacen mujeres**, **50% las hace gente de 45+ años**, con peak una semana antes del 18. — [Academia Nubimetrics](https://academia.nubimetrics.com/fiestas-patrias-independencia-chile)

**San Valentín — demanda muy concentrada en un solo día**
- A diferencia de los Cyber (que duran 3 días), la demanda de San Valentín se concentra casi enteramente en el 14 de febrero, forzando a la logística a desplegar **hasta 98% más vehículos de reparto** ese día. Categorías top: flores, chocolates, joyería, experiencias. — [G5noticias](https://g5noticias.cl/2026/02/13/san-valentin-dispara-la-logistica-en-chile-y-las-entregas-aumentan-hasta-99/)

**Canales de compra y redes sociales**
- Según cifras citadas de la CCS: **64%** de las compras online se hacen en sitios de grandes tiendas retail, **38%** en marketplaces, y solo **9%** directamente en redes sociales como canal de compra. `🟡 VERIFICAR` fecha de publicación exacta de este dato (la nota original discute la "informalidad" del comercio en redes, posiblemente de 2020-2021). — [La Tercera — "Búscanos en Instagram"](https://www.latercera.com/pulso-pm/noticia/buscanos-en-instagram-el-comercio-en-redes-sociales-se-triplicara-en-el-mundo-hacia-2025-y-en-chile-inquieta-la-informalidad/DSILSEZUZ5G2BPM25WURQCONWM/)
- Estudio de Accenture (dato de **2020**, época pandemia — usar con cautela por antigüedad): **58% de los consumidores chilenos inicia el proceso de compra en redes sociales**, y **Chile tiene la penetración más alta de la región (junto a Brasil) de WhatsApp en el proceso de compra: 83%**. `🟡 VERIFICAR vigencia` — es plausible que estos comportamientos se hayan acentuado, no revertido, pero el dato en sí es de 2020. — [Anda.cl](https://anda.cl/el-83-de-los-consumidores-chilenos-utiliza-whatsapp-como-parte-de-su-proceso-de-compra/)
- Uso general de redes sociales en Chile: **14,8 millones de usuarios activos (74,7% de la población)**, con un promedio de **3h39min diarias** en redes sociales, según el reporte *Digital 2026 Global Overview* de We Are Social/Meltwater/Kepios (publicado oct. 2025) — uno de los promedios más altos del mundo. `🟡 VERIFICAR` — no se pudo confirmar contra el reporte primario (bloqueo de acceso a fuentes), cifra tomada de agregadores locales. — [Rew.cl](https://rew.cl/2025/05/02/redes-sociales-en-chile-uso-tendencias-y-plataformas-favoritas-2025/), [Marketing4ecommerce Chile](https://marketing4ecommerce.cl/uso-de-redes-sociales-en-chile/)

---

## C. Tendencias de contenido y algoritmo Instagram 2025-2026

> Nota de alcance de esta sección: mezcla (a) declaraciones/observaciones de guías de marketing especializadas — fuente citable aunque no sea "dato duro" tipo encuesta — con (b) recomendaciones de práctica repetidas en múltiples guías sin estudio de respaldo, y (c) cambios de producto/política confirmados y fechados. Se distingue explícitamente dónde hay una cifra oficial vs. dónde hay una observación cualitativa o cifra "sin fuente dura".

### C.1 Algoritmo y producto de Instagram 2025-2026

**C.1.1 Señales de ranking que Mosseri confirmó**

Adam Mosseri (jefe de Instagram) confirmó en enero de 2025 que las tres señales de ranking que más pesan son **watch time (tiempo de reproducción), likes por alcance (likes per reach) y envíos por alcance (sends per reach)** — es decir, cuánta gente manda tu Reel por DM en relación a cuánta gente lo vio. Para Reels, los *sends* vía DM son la señal más pesada para la distribución hacia no-seguidores ([Socialync](https://www.socialync.io/blog/adam-mosseri-shares-instagram-algorithm-2026), [Dataslayer](https://www.dataslayer.ai/blog/instagram-algorithm-2025-complete-guide-for-marketers)).

Durante 2025-2026 Mosseri viene insistiendo en que los **compartidos (shares/sends)** son la señal a la que le da más importancia: que alguien mande tu contenido a un amigo por DM indica una conexión real, una señal más fuerte que un simple "guardado" ([Socialync](https://www.socialync.io/blog/adam-mosseri-shares-instagram-algorithm-2026)).

**Matiz por tipo de audiencia:** según la síntesis de varias guías 2026, los *likes per reach* pesarían más para el alcance entre seguidores existentes, mientras que los *sends* pesarían más para llegar a audiencias nuevas — esto es una interpretación de terceros sobre declaraciones de Mosseri, no una cita textual, así que se toma como orientación de práctica, no como cifra oficial ([Torro](https://torro.io/blog/instagram-algorithm-2025-explained), [Dataslayer](https://www.dataslayer.ai/blog/instagram-algorithm-2025-complete-guide-for-marketers)).

**Implicancia para Pedraza:** el CTA de "mándale esto a alguien a quien le encantaría" / contenido con valor de regalo (una lámina de un animal nativo raro, un dato curioso de fauna chilena) tiene más chance de generar *sends* que un post puramente estético.

**C.1.2 Alcance a no-seguidores: reach conectado vs. no conectado**

Mosseri distingue entre **Connected Reach** (contenido mostrado a quienes ya te siguen) y **Unconnected Reach** (contenido mostrado a audiencias nuevas vía recomendaciones/Explore) ([Torro](https://torro.io/blog/instagram-algorithm-2025-explained)).

Varias guías 2026 describen un sistema de "prueba" (a veces llamado *audition system* en inglés) donde el contenido público se muestra primero a un grupo pequeño de no-seguidores; si ese grupo engancha bien, se empuja a audiencias progresivamente más grandes, y si el enganche inicial es bajo, la distribución se frena antes de llegar incluso a los propios seguidores ([Dataslayer](https://www.dataslayer.ai/blog/instagram-algorithm-2025-complete-guide-for-marketers)). Esta descripción viene de blogs de marketing que sintetizan declaraciones de Mosseri, no de una cita textual única — se presenta como descripción de funcionamiento probable, no como mecanismo confirmado palabra por palabra.

**C.1.3 Originalidad: penalización a cuentas que repostean (actualización de abril 2026)**

Este es el cambio más concreto y verificable del período: **el 30 de abril de 2026 Instagram anunció** que las cuentas cuyo contenido es mayoritariamente repostear trabajo ajeno **dejan de ser recomendables** a no-seguidores en Explore, Feed y Discover. La medida extiende a fotos y carruseles una protección que ya existía para Reels ([Tubefilter](https://www.tubefilter.com/2026/04/30/instagram-removes-algorithm-recommendations-repost-content-aggregator/), [PetaPixel](https://petapixel.com/2026/04/30/new-instagram-policies-target-reposted-content/), [MediaPost](https://www.mediapost.com/publications/article/414773/instagram-algorithm-update-discourages-reposted-co.html), [TechCrunch](https://techcrunch.com/2026/04/30/instagram-restricts-reach-of-content-aggregators-in-new-crackdown/)).

Cita directa de Mosseri: *"If most of what you post to Instagram is someone else's content, your account is no longer going to be recommendable."* Aclaró además que los agregadores de contenido pueden seguir operando siempre que "transformen de forma significativa" lo que republican; el castigo algorítmico apunta a "contenido no original que [los reposteadores] no mejoraron" ([Tubefilter](https://www.tubefilter.com/2026/04/30/instagram-removes-algorithm-recommendations-repost-content-aggregator/)).

**Qué cuenta como "original" según la cobertura del anuncio:** contenido nuevo o "materialmente editado", con ejemplos como agregar texto propio que aporta contexto (no solo describir lo que se ve), agregar gráficos propios que suman información, o usar la función Remix de forma transformadora ([resumen de cobertura vía búsqueda, coincidente en varias fuentes](https://gotmenow.com/2026/05/12/instagram-original-content-rule-2026/)).

La evaluación sería sobre una ventana móvil de 30 días. 🟡 **VERIFICAR** — cifras específicas como "40-60% más distribución para contenido original" o "10+ reposts en 30 días = exclusión total" aparecen en algunos blogs (p. ej. Dataslayer) **sin fuente primaria verificable citada por ellos mismos**, y no se pudo leer el artículo original completo — se marcan aquí como **sin fuente dura**, no como estadística confiable. 🟡 **VERIFICAR** también la cifra de que "75% de las recomendaciones en EE.UU. ya son contenido original": aparece repetida en cobertura secundaria del anuncio pero no se pudo verificar contra el comunicado original de Instagram en este research.

**Implicancia para Pedraza:** la marca ya publica contenido propio (ilustración, producto, proceso), así que esta política juega a favor — pero refuerza que resposteos de fans/prensa deben ser la minoría del feed, no la base de la estrategia de contenido.

**C.1.4 Trial Reels: qué son y cómo funcionan**

**Trial Reels** son Reels publicados a una audiencia de prueba: Instagram los distribuye únicamente a personas que *no* siguen la cuenta. Mosseri anunció la función explicando su lógica: sirve para "saltarse todo el sistema de ranking conectado e ir directo a las recomendaciones no conectadas", evitando saturar a los seguidores actuales con contenido experimental ([Publer](https://publer.com/blog/instagram-trial-reels-guide/), [Fliki](https://fliki.ai/blog/trial-reels-instagram)).

Cita de Mosseri sobre el objetivo: *"Our hope is that this helps people feel more comfortable experimenting with new ideas without worrying how their followers might react."* ([Publer](https://publer.com/blog/instagram-trial-reels-guide/))

**Mecánica reportada:** se publica como Trial Reel, se revisan métricas a las 24 horas, y a las 72 horas Instagram decide (según cómo respondieron los no-seguidores) si el Reel pasa a compartirse automáticamente con los seguidores y se fija en la grilla ([Publer](https://publer.com/blog/instagram-trial-reels-guide/)).

**Disponibilidad:** se lanzó a fines de 2024 y se expandió a todas las cuentas creadoras con 1.000+ seguidores hacia mediados de 2025, requiere cuenta profesional ([Publer](https://publer.com/blog/instagram-trial-reels-guide/)).

**Novedad 2026 — programación:** ahora se pueden programar Trial Reels. Cita de Mosseri: *"Back in November, someone asked why can't you schedule a Trial Reel. And so we built it, and now you can."* ([Social Media Today](https://www.socialmediatoday.com/news/instagram-allows-creators-to-schedule-trial-reels/816549/))

**Implicancia para Pedraza:** ideal para probar formatos nuevos (ASMR de empaque, ilustración en vivo, humor sobre fauna chilena) sin arriesgar el feed principal ante los seguidores actuales, y para calibrar qué "engancha" a audiencia fría antes de invertir producción.

**C.1.5 Duración recomendada de Reels**

El límite técnico se amplió: Instagram permite ahora Reels de hasta **20 minutos** (subiendo desde el tope de 3 minutos vigente a inicios de 2026), tanto grabados en la app como subidos desde la cámara ([SellerPic](https://www.sellerpic.ai/blog/instagram-reel-size), [Inrō](https://www.inro.social/blog/instagram-reels-can-now-be-20-minutes-long-new-time-limit-explained-2025)).

**Pero hay una distinción clave entre "se puede" y "conviene":** los Reels de más de 3 minutos no se recomiendan a gente que no te sigue todavía — quedan mayormente dentro del grafo de seguidores existente en vez de llegar a audiencia nueva vía Explore o la pestaña Reels ([SellerPic](https://www.sellerpic.ai/blog/instagram-reel-size)).

El rango recomendado para alcance y enganche que citan varias guías 2026 es **45-60 segundos**, con el tramo de **15-30 segundos** como el que mejor retiene (gancho + valor + CTA, con alta tasa de finalización) ([SellerPic](https://www.sellerpic.ai/blog/instagram-reel-size), [Foxy AI](https://foxy.ai/academy/how-long-can-a-reel-be-on-instagram-2025-guide)). 🟡 **VERIFICAR** — estas cifras de "sweet spot" vienen de guías de marketing (no de un comunicado oficial de Instagram con ese rango exacto), así que se toman como recomendación de práctica consolidada, no como dato duro de Meta.

**Implicancia para Pedraza:** para contenido pensado en alcanzar gente nueva (proceso, packing, curiosidades de fauna), apuntar a 15-45 segundos. Reels más largos (tutorial extendido, "day in the studio") funcionan mejor como contenido para la comunidad ya existente, no como puerta de entrada.

**C.1.6 Carruseles y su relación con el feed de Reels**

Varias fuentes 2026 coinciden en que agregar **música/audio a un carrusel** lo hace elegible para aparecer también en el feed de Reels, ampliando su alcance potencial más allá del feed clásico ([Aurelius Media](https://www.aureliusmedia.co/blog/what-works-on-instagram-2026), [TrueFuture Media](https://www.truefuturemedia.com/articles/instagram-reach-2026-algorithm-reels-carousels-caption-seo)).

Mosseri ha sido explícito en que las fotos y los carruseles **no van a desaparecer**: el feed de posts estáticos sigue siendo parte del producto, pese al foco en video ([Aurelius Media](https://www.aureliusmedia.co/blog/what-works-on-instagram-2026)).

🟡 **VERIFICAR** — cifras puntuales como "los carruseles tienen 1,4x más alcance que los posts estáticos" o "1,92% de engagement promedio vs 0,50% en Reels" circulan en blogs de marketing 2026 pero **no se pudo confirmar una fuente primaria de Meta con esos números exactos** — se marcan como sin fuente dura. Lo que sí es consistente entre fuentes es la dirección: los carruseles generan más interacción "profunda" (varios swipes, más tiempo, más posibilidad de guardado/compartido) que una imagen única, lo cual conecta con las señales que Mosseri sí confirmó (sends, watch/view time) ([TrueFuture Media](https://www.truefuturemedia.com/articles/instagram-reach-2026-algorithm-reels-carousels-caption-seo)).

**Implicancia para Pedraza:** un carrusel "así se hizo esta lámina" (boceto → línea → color → producto final) con audio agregado es un formato de bajo costo de producción que puede aparecer tanto en feed como en Reels.

**C.1.7 SEO dentro de Instagram: keywords vs. hashtags**

Mosseri confirmó que los **hashtags nunca aumentaron el alcance de forma significativa** — cualquier efecto es marginal, y esto lo viene diciendo desde mediados de 2024. Instagram respaldó esa postura con un cambio de producto: en diciembre de 2024 eliminó la posibilidad de "seguir" hashtags ([Kontentino](https://www.kontentino.com/q-and-a/instagram-hashtags-reach/), [MeetEdgar](https://meetedgar.com/blog/are-hashtags-still-relevant)).

El rol actual del hashtag es de **contexto, no de alcance**: ayuda al algoritmo a entender de qué trata el contenido para sugerirlo en búsquedas, no funciona como palanca de descubrimiento masivo ([Kontentino](https://www.kontentino.com/q-and-a/instagram-hashtags-reach/)).

En su lugar, el **caption es la pieza de metadata más importante**: conviene poner las palabras clave relevantes en la primera oración, porque el algoritmo pondera más el inicio del caption ([usevisuals](https://usevisuals.com/blog/proven-instagram-seo-2026-optimizing-bio-and-captions-for-search)). El **alt text**, originalmente pensado para accesibilidad, ahora es una señal secundaria relevante para el algoritmo: escribir 1-2 oraciones con la keyword objetivo evita depender de la interpretación automática de la imagen por IA, que puede ser imprecisa ([usevisuals](https://usevisuals.com/blog/proven-instagram-seo-2026-optimizing-bio-and-captions-for-search)).

Instagram funciona cada vez más como motor de búsqueda: tanto Google como Bing indexan captions de Instagram, por lo que el contenido puede aparecer en resultados de búsqueda externos ([usevisuals](https://usevisuals.com/blog/proven-instagram-seo-2026-optimizing-bio-and-captions-for-search)). La recomendación de práctica es usar 3-5 hashtags relevantes en vez del viejo enfoque de 30 hashtags, y priorizar keywords en caption y alt text ([SEO.com](https://www.seo.com/blog/instagram-seo/)).

**Implicancia para Pedraza:** las keywords naturales del rubro — "ilustración flora y fauna chilena", "cóndor", "pudú", "monito del monte", "diseño chileno", "regalo hecho en Chile" — deberían ir en la primera línea del caption y en el alt text de cada foto/lámina, más que en un bloque de hashtags al final.

### C.2 Formatos que funcionan para artistas/ilustradores y marcas de producto

**C.2.1 Videos de proceso (process videos) y time-lapse**

Los videos de proceso "construyen interés" mostrando el esfuerzo y la inspiración detrás de una obra; son un formato "ideal" para Reels según guías de marketing para ilustradores ([Pixartprinting](https://www.pixartprinting.com/blog/instagram-powerhouse-illustrator/)).

Caso citado: el lettering artist James Lewis notó que su audiencia estaba interesada en ver su proceso y contenido detrás de cámara, y crear ese tipo de contenido le generó más engagement (fuente secundaria, sin cifra específica) ([Pixartprinting](https://www.pixartprinting.com/blog/instagram-powerhouse-illustrator/)).

Recomendación de práctica repetida en varias guías: mezclar obra terminada, trabajo en proceso ("work in progress") y contenido detrás de cámara — bocetos, borradores, iteraciones — para mantener el interés de la audiencia ([Pixartprinting](https://www.pixartprinting.com/blog/instagram-powerhouse-illustrator/)). Un time-lapse de 15 segundos de un dibujo (de hoja en blanco a ilustración terminada) se describe como formato "hipnótico" que retiene la mirada ([Planable](https://planable.io/blog/instagram-reels-ideas/)).

**C.2.2 ASMR de empaque de pedidos (packing orders)**

Filmar el empaque de un pedido real (sacar el producto, agregar una nota de agradecimiento o sticker de marca, sellar la caja) es una de las ideas de Reels más recurrentes para negocios pequeños. El componente ASMR (sonido del papel, la cinta) suele describirse como parte clave del enganche ([Wishpond](https://wishpond.com/blog/instagram-reels-ideas/)).

Por qué funcionaría, según estas guías: es "raramente satisfactorio" de ver, da a los clientes una idea del cuidado puesto en cada pedido, funciona como prueba social de que están entrando pedidos (generando FOMO), y el contenido ASMR conecta con marketing sensorial además de operar como señal de confianza de marca ([Wishpond](https://wishpond.com/blog/instagram-reels-ideas/)).

Recomendaciones técnicas de práctica: grabar en una sala silenciosa con buen micrófono, resaltar los sonidos de doblar caja y papel de seda, evitar música de fondo para que el sonido natural sea protagonista, y mantenerlo bajo 30 segundos para maximizar la tasa de finalización ([Wishpond](https://wishpond.com/blog/instagram-reels-ideas/)). Es un formato de bajo costo de producción — no requiere equipo de filmación grande, alcanza con un micrófono decente ([Wishpond](https://wishpond.com/blog/instagram-reels-ideas/)).

**Implicancia para Pedraza:** encaja directamente con el catálogo (láminas, libretas, calcetines) donde el empaque + un producto ilustrado atractivo es fotogénico por sí mismo. Es de los formatos más baratos de producir y más citados como "funciona" en el research.

**C.2.3 Ilustración en vivo / demostrativo**

Mostrar materiales, herramientas o técnicas —por ejemplo, qué pinceles se usan al pintar digitalmente, o cómo se hace una ilustración con acuarela para un producto— se recomienda como contenido educativo/demostrativo que retiene audiencia ([The Social Media Artist](https://www.thesocialmediaartist.com/visualartistinstagramreels/)).

Recomendación de práctica sobre el algoritmo (no cifra oficial): el algoritmo favorecería que la gente vea un Reel más de una vez, lo que señalaría contenido de calidad; por eso el gancho de los primeros segundos es crítico — si el Reel no retiene la mirada en los primeros segundos, compite en desventaja contra el resto del contenido publicado en simultáneo ([Planable](https://planable.io/blog/instagram-reels-ideas/)).

**C.2.4 Antes/después (before-after)**

El formato antes/después es señalado como especialmente potente para rubros con transformación física visible (diseño de interiores, detailing de autos), y se describe como aplicable también a productos rediseñados en general, comunicando artesanía y oficio más rápido que un texto ([Automateed](https://www.automateed.com/before-and-after-transformations-for-creators), Reframex citado en la misma búsqueda).

🟡 **VERIFICAR** — la cifra "las transformaciones reciben 6x más guardados que el contenido promedio" aparece en fuentes de marketing sin estudio o comunicado de Instagram identificable respaldándola — **se marca como sin fuente dura**, se presenta la idea (antes/después genera guardados) como observación cualitativa recurrente, no como estadística confiable.

**Implicancia para Pedraza:** aplicable a "boceto vs. lámina terminada", "diseño en pantalla vs. producto físico (plato, botella) ya fabricado", o "material en bruto vs. producto textil terminado (calcetín/bolso)".

**C.2.5 "Day in the studio" y storytelling de la creadora**

No se encontró un estudio o dato duro específico sobre este formato puntual; la evidencia es de guías generales de social media para negocios creativos que recomiendan pilares de contenido que incluyan contenido educativo, detrás de cámara, testimonios e historias personales ([Sprout Social](https://sproutsocial.com/insights/social-media-marketing-for-small-business/)).

Lo que sí hay con más respaldo es la tendencia más amplia de **contenido liderado por la fundadora/creadora** dentro de marcas de producto: varias guías de tendencias 2026 describen que el contenido con cara visible de fundador/a, equipo o creador/a genera mejor recordación que el posteo de marca "sin cara", y que la narrativa de marca madura hacia mostrar personalidad y presencia humana real en vez de contenido pulido pero "vacío" ([blog.mean.ceo](https://blog.mean.ceo/instagram-trends-may-2026/)). La tendencia identificada es hacia formatos menos editados, estilo cámara selfie/sin guion (a veces llamado "YAP" en inglés), que buscan sensación de autenticidad por sobre producción pulida ([blog.mean.ceo](https://blog.mean.ceo/instagram-trends-may-2026/)).

Esto son observaciones de blogs de tendencias de marketing (no estudios cuantitativos), así que se presentan como lectura de tendencia, no como estadística. Aun así, es coherente con el hecho de que Pedraza Ilustración ya tiene una cara pública (María José) integrada naturalmente al contenido de marca — la recomendación de práctica es seguir apalancando eso en vez de migrar a una cuenta 100% "de catálogo".

### C.3 Instagram Shopping / herramientas de venta vigentes en 2026

**C.3.1 Cambio estructural: fin del checkout nativo**

**Cambio confirmado y relevante:** Meta comenzó a eliminar el checkout nativo dentro de Facebook e Instagram Shops a partir de junio de 2025, con el grueso de las tiendas migradas hacia fines de agosto de 2025 ([GoDataFeed](https://www.godatafeed.com/blog/meta-is-dropping-native-checkout-on-facebook-and-instagram), [ppc.land](https://ppc.land/meta-phases-out-facebook-and-instagram-shops-checkout-by-august-2025/), [BigCommerce](https://www.bigcommerce.com/blog/updates-to-meta-shops-checkout-for-bigcommerce/)).

**Qué significa en la práctica para 2026:** cuando alguien toca un producto etiquetado o un anuncio con etiqueta de producto, ahora es **redirigido al sitio propio del vendedor** para completar la compra — ya no se puede pagar sin salir de Instagram. El descubrimiento y la navegación de productos siguen pasando dentro de la app, pero la transacción se completa afuera ([GoDataFeed](https://www.godatafeed.com/blog/meta-is-dropping-native-checkout-on-facebook-and-instagram)).

Beneficio reportado para el vendedor: el checkout nativo de Meta cobraba comisión por transacción; comprar en el sitio propio no tiene esa comisión de Meta (aunque el comerciante pasa a responsabilizarse de impuestos y reporting) ([GoDataFeed](https://www.godatafeed.com/blog/meta-is-dropping-native-checkout-on-facebook-and-instagram)). En Ads Manager, la métrica "Meta purchases" fue reemplazada por "Shops-assisted purchases" ([GoDataFeed](https://www.godatafeed.com/blog/meta-is-dropping-native-checkout-on-facebook-and-instagram)).

**🟢 Aclaración confirmada por el operador (jul-2026) — lectura correcta para Pedraza:** el checkout nativo de Instagram/Facebook (pagar sin salir de la app) **nunca estuvo disponible fuera de Estados Unidos**. Para una tienda chilena como Pedraza, la compra **siempre** se cerró afuera de Instagram, en el sitio propio — nunca hubo una etapa previa en la que se pudiera pagar dentro de la app. Esto significa que la eliminación del checkout nativo en 2025 **no cambió nada operativamente para la marca**: no se perdió ninguna función que estuvieran usando. No corresponde presentar este cambio como una pérdida o un retroceso para Pedraza — es un ajuste de la plataforma que solo afectó a tiendas de EEUU.

**Implicancia directa para Pedraza:** en 2026, igual que ya venía siendo el caso para una tienda chilena, Instagram funciona como canal de descubrimiento y consideración, no como tienda autocontenida — el catálogo de producto (vía Meta Commerce Manager conectado a la plataforma de tienda que use Pedraza) debe apuntar siempre al sitio propio para cerrar la venta. Esto no es un ajuste nuevo que haya que hacer a raíz del cambio de 2025: es y ha sido siempre el flujo real de compra para la marca, así que sigue siendo válido diseñar bien ese paso de Instagram a la tienda propia — simplemente no es una consecuencia de esta eliminación puntual del checkout nativo en EEUU.

**C.3.2 Etiquetas de producto**

🟡 **VERIFICAR** — los límites de etiquetado de producto reportados por formato: hasta **20 productos en posts carrusel**, **5 en imagen única**, sticker de producto disponible en Stories (hasta 5 por story), y hasta **30 etiquetas de producto por Reel** — el formato con el placement más generoso porque Reels tiene el mayor alcance orgánico de la plataforma ([GoDataFeed](https://www.godatafeed.com/blog/how-to-use-instagram-product-tags), otras fuentes coincidentes en la búsqueda). Estas cifras de límites vienen de guías de e-commerce/agencias, no de la página oficial de ayuda de Meta leída directamente en este research, así que conviene confirmarlas en el Centro de Ayuda de Instagram ([help.instagram.com](https://help.instagram.com/337910740093030)) al momento de implementar.

Novedad de producto: integración de **product links dentro del Reel** que permite a quien mira tocar y ver detalles de producto superpuestos sin interrumpir la reproducción ([GoDataFeed](https://www.godatafeed.com/blog/how-to-use-instagram-product-tags)).

**C.3.3 Link sticker en Stories**

El link sticker reemplazó al viejo "swipe up" y **democratizó el link en Stories**: ya no se necesita una cuenta grande para poner un link, cualquier cuenta puede agregarlo ([creatorflow.so vía búsqueda](https://creatorflow.so/blog/instagram-story-link-sticker/)).

Recomendaciones de práctica (no cifras oficiales, consolidadas entre varias guías 2026):
- Acompañar el sticker con un CTA de texto claro tipo "Toca aquí" — no asumir que la audiencia sabe que debe tocar el sticker.
- La posición de mayor conversión reportada es en medio de una secuencia de 3-5 slides — después de mostrar valor, antes de que la persona se vaya.
- Poner un link sticker en cada story entrena a la audiencia a ignorarlo — usarlo con criterio, no en automático.
- Usar cuenta profesional para ver los taps en Insights, y sumar parámetros UTM al link para medir en Analytics de la tienda cuánto tráfico/venta generó cada story.

(Fuente de estas prácticas: resumen de guías 2026 sobre Stories, sin estudio cuantitativo específico citado — se presentan como recomendación consolidada, no estadística.)

**C.3.4 DM automation: opciones de más simple a más avanzada**

Existe una escalera clara de herramientas, de más simple/gratis a más compleja/paga:

1. **Respuestas guardadas nativas de Instagram** (Saved Replies / Quick Replies): función gratuita incluida en cuentas Business/Creator. Se configuran en Ajustes → Negocio o Creador → Respuestas guardadas, con un atajo de palabra clave que inserta el mensaje completo al escribirlo en un DM. Limitación: es **manual** — la persona que administra la cuenta tiene que tocar para insertarla, no se dispara sola según lo que escribe el usuario.
2. **Meta Business Suite**: siguiente escalón, ya con automatización basada en reglas (hasta 5 palabras clave o frases por automatización), sin costo adicional de terceros.
3. **Herramientas de terceros vía Instagram Graph API** (ManyChat, Chatfuel, MobileMonkey, InstantDM, etc.): permiten flujos más ricos — por ejemplo, "comenta la palabra X en este Reel y te llega un DM automático con el link". Meta permite explícitamente estas herramientas verificadas para automatizar respuestas a acciones iniciadas por el usuario ([Trengo](https://trengo.com/blog/how-to-set-up-auto-reply-on-instagram), [InstantDM vía búsqueda](https://instantdm.com/blog/how-to-set-up-automated-instagram-replies-that-convert)).

**ManyChat específicamente:** el disparador de "comentario a DM" (Comment-to-DM) funciona tanto en posts de feed como en Reels; se puede dirigir a un Reel específico, a todos los Reels, o al próximo que se publique. Palabras clave reportadas como buen desempeño: "INFO", "LINK", "PRECIO", "DETALLES" ([ManyChat Help](https://help.manychat.com/hc/en-us/articles/16654065283100-Quick-Automation-Auto-DM-links-from-comments), [ManyChat](https://get.manychat.com/use-case/comment-to-dm)). Costo: automatización real de Instagram requiere como mínimo el plan Essential, desde US$14/mes ([ManyChat](https://manychat.com/blog/instagram-dm-automation-tools/)).

Guía de práctica sobre cuándo dar el salto a herramienta paga: el punto de inflexión estaría en unos 20+ DMs diarios — por debajo de eso, las respuestas guardadas nativas alcanzan; por arriba, se estaría perdiendo 1-2+ horas diarias en mensajes que se podrían automatizar por US$10-29/mes (cifra de guía de marketing, no estudio, presentada como orientación) ([resumen de búsqueda sobre auto-reply tools](https://instantdm.com/blog/what-are-the-best-auto-responder-tools-for-instagram)).

**Recomendación para empezar (más simple):** para el volumen actual de una marca chica como Pedraza, lo más simple y sin costo es partir con **Respuestas guardadas nativas** para preguntas frecuentes (talla de calcetines, tiempos de envío, "¿dónde compro?"), y evaluar Meta Business Suite o ManyChat recién cuando el volumen de comentarios/DMs lo justifique — sobre todo si se quiere automatizar "comenta LINK y te mando el link de la tienda" en Reels de producto.

### C.4 Cadencia y mejores prácticas 2026

**C.4.1 Frecuencia recomendada**

Cadencia atribuida a Mosseri para crecimiento: **2 Reels por semana + 3-5 posts de Feed**, con el énfasis en que la consistencia importa más que el volumen ([resumen de búsqueda coincidente entre varias fuentes](https://www.kontentino.com/blog/how-often-to-post-on-instagram/)). 🟡 **VERIFICAR** — análisis de Buffer sobre 9,6 millones de posts confirmaría que **3-5 posts de feed por semana** es el punto óptimo de alcance por post ([Buffer, citado en búsqueda](https://buffer.com/resources/how-often-to-post-on-instagram/); el fetch directo del artículo de Buffer no fue posible por el bloqueo de red en este entorno, por lo que la cifra queda respaldada solo por el resumen de búsqueda, no por lectura directa del artículo; conviene revalidar antes de citarlo como dato "duro").

Para Stories, la recomendación pública atribuida a Mosseri es de **"un par de Stories por día"** como base para mantener el engagement de la audiencia, con guías de terceros ubicando el rango en 2-5 por día ([resumen de búsqueda](https://www.kontentino.com/blog/how-often-to-post-on-instagram/)).

Cita/paráfrasis de Mosseri sobre el principio general: cuanto más se publica, más probable es alcanzar más gente — pero publicar más no debería ir en desmedro de la creatividad ni del bienestar de quien crea el contenido (paráfrasis recurrente en varias fuentes, sin cita textual verificada en este research).

**C.4.2 Horarios**

No hay un horario "oficial" de Instagram — son inferencias de analítica de terceros sobre grandes volúmenes de posts, así que se presentan como orientación de partida, no como regla. Consolidando varias fuentes 2026: **martes a jueves** tienden a rendir mejor que el resto de la semana, con picos en **media mañana (9-11am)** y **mediodía (12-1pm)** entre semana, y **noches (7-9pm)** favoreciendo particularmente a Reels; viernes y sábado tienden a rendir peor ([resumen de búsqueda coincidente entre Buffer, Later, Hootsuite, RecurPost](https://buffer.com/resources/when-is-the-best-time-to-post-on-instagram/)). La recomendación consistente entre todas las fuentes es usar estas ventanas como punto de partida y ajustar según el propio Insights de la cuenta, no tomarlas como verdad universal.

**C.4.3 Stories para conversión**

Ver C.3.3 (link sticker) — se resume acá el criterio central: usar Stories como puente hacia una acción concreta (link a producto, encuesta, pregunta) en vez de solo repetir el feed, y evitar el sobreuso del link sticker para no entrenar a la audiencia a ignorarlo.

**C.4.4 Hashtags vs. keywords**

Ver C.1.7 en detalle. Resumen accionable: dejar de tratar los hashtags como palanca de alcance (Mosseri lo desmintió y el producto lo refleja al haber eliminado el "seguir hashtag" en diciembre 2024) y priorizar keywords reales del rubro en la primera línea del caption y en el alt text de cada imagen ([Kontentino](https://www.kontentino.com/q-and-a/instagram-hashtags-reach/)).

### C.5 Plantilla de bitácora de pruebas de formato (para fases siguientes)

> Este research es Fase 0 — todavía no hay datos propios de Pedraza Ilustración ejecutando estos formatos. Esta es la plantilla de bitácora que debería completarse a medida que se van probando formatos, para que las fases siguientes del plan se apoyen en evidencia propia y no solo en benchmarks externos. Se deja la estructura lista para llenar.

| Fecha | Formato probado | Hipótesis (según research) | Resultado (reach no-seguidores / sends / saves / clics a tienda) | Sigue / se descarta | Notas |
|---|---|---|---|---|---|
| _(pendiente)_ | Ej: ASMR packing de pedido | Formato barato, alto potencial de saves/sends (C.2.2) | — | — | — |
| _(pendiente)_ | Ej: Carrusel "así se hizo esta lámina" con audio | Elegible para feed de Reels + carrusel, refuerza sends (C.1.6) | — | — | — |
| _(pendiente)_ | Ej: Trial Reel de ilustración en vivo | Prueba con no-seguidores sin arriesgar el feed a seguidores actuales (C.1.4) | — | — | — |
| _(pendiente)_ | Ej: Reel "day in the studio" con María José | Contenido con cara humana / storytelling de creadora (C.2.5) | — | — | — |
| _(pendiente)_ | Ej: Comment-to-DM ("comenta LINK") vía respuestas guardadas nativas | Paso más simple de automatización de venta (C.3.4) | — | — | — |

**Métricas sugeridas a registrar por prueba** (alineadas a las señales de ranking de C.1.1): sends per reach, watch time / % de reproducción completa, likes per reach, saves, alcance a no-seguidores vs. seguidores, clics al link de tienda, y — si aplica — conversión a venta en el sitio propio (dado que el checkout ya no ocurre dentro de Instagram, ver C.3.1).

### C.6 Fuentes consultadas (listado completo — algoritmo/tendencias Instagram)

- Socialync — [Adam Mosseri on Shares: The Real Instagram Signal in 2026](https://www.socialync.io/blog/adam-mosseri-shares-instagram-algorithm-2026)
- Dataslayer — [Instagram Algorithm 2026: 5 Ranking Signals Mosseri Confirmed](https://www.dataslayer.ai/blog/instagram-algorithm-2025-complete-guide-for-marketers)
- Torro — [Instagram Algorithm 2025 (Explained by Adam Mosseri)](https://torro.io/blog/instagram-algorithm-2025-explained)
- Tubefilter — [Instagram has a new penalty for unoriginal content aggregators](https://www.tubefilter.com/2026/04/30/instagram-removes-algorithm-recommendations-repost-content-aggregator/)
- PetaPixel — [New Instagram Policies Target Reposted Content](https://petapixel.com/2026/04/30/new-instagram-policies-target-reposted-content/)
- MediaPost — [Instagram Algorithm Update Discourages Reposted Content](https://www.mediapost.com/publications/article/414773/instagram-algorithm-update-discourages-reposted-co.html)
- TechCrunch — [Instagram restricts reach of content aggregators in new crackdown](https://techcrunch.com/2026/04/30/instagram-restricts-reach-of-content-aggregators-in-new-crackdown/)
- gotmenow — [Instagram Original Content Rule 2026 — Full Creator Guide](https://gotmenow.com/2026/05/12/instagram-original-content-rule-2026/)
- Publer — [What Are Instagram Trial Reels? Full Guide + Growth Strategy](https://publer.com/blog/instagram-trial-reels-guide/)
- Fliki — [Trial Reels Instagram: How They Work](https://fliki.ai/blog/trial-reels-instagram)
- Social Media Today — [Instagram allows creators to schedule Trial Reels](https://www.socialmediatoday.com/news/instagram-allows-creators-to-schedule-trial-reels/816549/)
- SellerPic — [How Long Can Instagram Reels Be in 2026?](https://www.sellerpic.ai/blog/instagram-reel-size)
- Inrō — [Instagram Reels can now be 20 minutes long](https://www.inro.social/blog/instagram-reels-can-now-be-20-minutes-long-new-time-limit-explained-2025)
- Foxy AI — [Instagram Reel Length Limits Explained (2026 Update)](https://foxy.ai/academy/how-long-can-a-reel-be-on-instagram-2025-guide)
- Aurelius Media — [What Actually Works on Instagram in 2026](https://www.aureliusmedia.co/blog/what-works-on-instagram-2026)
- TrueFuture Media — [Instagram Reach in 2026: Reels, Carousels, and Caption SEO](https://www.truefuturemedia.com/articles/instagram-reach-2026-algorithm-reels-carousels-caption-seo)
- Kontentino — [Do hashtags still work on Instagram in 2026? Mosseri finally settled it](https://www.kontentino.com/q-and-a/instagram-hashtags-reach/)
- MeetEdgar — [Are hashtags still relevant in 2026?](https://meetedgar.com/blog/are-hashtags-still-relevant)
- usevisuals — [Proven Instagram SEO 2026: Optimizing Bio and Captions for Search](https://usevisuals.com/blog/proven-instagram-seo-2026-optimizing-bio-and-captions-for-search)
- SEO.com — [Instagram SEO: 7 Tips to Grow Your Reach in 2026](https://www.seo.com/blog/instagram-seo/)
- Pixartprinting — [Instagram as a Marketing Powerhouse for Artists, Illustrators, and Designers](https://www.pixartprinting.com/blog/instagram-powerhouse-illustrator/)
- Wishpond — [25 Awesome Instagram Reels Ideas For Small Businesses](https://wishpond.com/blog/instagram-reels-ideas/)
- The Social Media Artist — [Instagram Reels Content Ideas for Visual Artists](https://www.thesocialmediaartist.com/visualartistinstagramreels/)
- Planable — [47 Instagram Reels Ideas for Engagement & Growth in 2026](https://planable.io/blog/instagram-reels-ideas/)
- Automateed — [Before and After Transformations for Creators](https://www.automateed.com/before-and-after-transformations-for-creators)
- Sprout Social — [Social Media Marketing for Small Business: Complete Guide for 2026](https://sproutsocial.com/insights/social-media-marketing-for-small-business/)
- blog.mean.ceo — [Instagram Trends | May, 2026 (STARTUP EDITION)](https://blog.mean.ceo/instagram-trends-may-2026/)
- GoDataFeed — [Meta Is Dropping Native Checkout on Facebook and Instagram Shops](https://www.godatafeed.com/blog/meta-is-dropping-native-checkout-on-facebook-and-instagram)
- ppc.land — [Meta phases out Facebook and Instagram shops checkout by August 2025](https://ppc.land/meta-phases-out-facebook-and-instagram-shops-checkout-by-august-2025/)
- BigCommerce — [Updates to Meta Shops checkout for BigCommerce](https://www.bigcommerce.com/blog/updates-to-meta-shops-checkout-for-bigcommerce/)
- GoDataFeed — [From Likes to Purchases: How Shops are Using Instagram Product Tags to Drive Sales](https://www.godatafeed.com/blog/how-to-use-instagram-product-tags)
- Instagram Help Center — [Shopping on Instagram](https://help.instagram.com/337910740093030)
- creatorflow.so — [Instagram Story Link Sticker: Add a Link in 30 Seconds](https://creatorflow.so/blog/instagram-story-link-sticker/)
- Trengo — [How to set up auto reply on Instagram DMs in 2026](https://trengo.com/blog/how-to-set-up-auto-reply-on-instagram)
- InstantDM — [How to Set Up Automated Instagram Replies That Convert](https://instantdm.com/blog/how-to-set-up-automated-instagram-replies-that-convert)
- ManyChat Help — [Quick Automation: Auto-DM links from comments](https://help.manychat.com/hc/en-us/articles/16654065283100-Quick-Automation-Auto-DM-links-from-comments)
- ManyChat — [Comment-to-DM Automation](https://get.manychat.com/use-case/comment-to-dm)
- ManyChat — [Best Instagram DM Automation Tools (2026 Guide)](https://manychat.com/blog/instagram-dm-automation-tools/)
- Kontentino — [How Often to Post on Instagram in 2026](https://www.kontentino.com/blog/how-often-to-post-on-instagram/)
- Buffer — [Best Time to Post on Instagram: 2026 Data from 9.6M Posts](https://buffer.com/resources/when-is-the-best-time-to-post-on-instagram/)

---

## D. Panorama Amazon EEUU (Rampa EEUU)

> Alcance: Amazon.com (marketplace EEUU) para las categorías de Pedraza Ilustración — láminas/prints, puzles, platos, botellas, calcetines, bolsos, libretas.

### D.1 Categorías relevantes y nivel de competencia

**D.1.1 Wall art / prints (láminas — el corazón del catálogo de Pedraza)**

- El nodo de Amazon "Best Sellers: Wall Art" existe como categoría propia dentro de Home & Garden (`amazon.com/Best-Sellers-Wall-Art/zgbs/home-garden/3736081`), lo que confirma que es una categoría con volumen y ranking propios — no se pudo leer el listado en vivo (WebFetch bloqueado a nivel de entorno, ver nota metodológica), así que esto es solo confirmación estructural vía snippet de búsqueda, no un dato de ventas. 🟡 VERIFICAR ranking en vivo.
- Tendencia de producto 2026 citada por múltiples fuentes de retail/interiorismo: el arte de pared con temática naturaleza — botánicos minimalistas, paisajes, tonos neutros — domina las listas de más vendidos en decoración; los prints enmarcados y "statement pieces" de gran formato son los favoritos de sala de estar ([buywallart.ca, "Best-Selling Wall Art 2026"](https://buywallart.ca/blogs/news/best-selling-wall-art-2026); [merchize.com, "Wall Art Trends 2026"](https://merchize.com/wall-art-trends/)).
- En paralelo, el diseño de interiores 2026 en general apunta a "biophilic design", paletas neutras/térreas y motivos botánicos a mayor escala pero con líneas más sueltas ([Parade, "Interior Designers Reveal Spring 2026 Home Decor Must-Haves"](https://parade.com/shopping/spring-2026-home-decor-trends-shopping-roundup); [Accio, "Biophilic Interior Design Trend 2026"](https://www.accio.com/business/biophilic-interior-design-trend); [pulsepathlife.com, "Home Decor Trends 2026: Botanical & Earthy Styles"](https://pulsepathlife.com/home-decor-trends-2026-a-modern-mood-board-for-botanical-earthy-styles/)). Esto calza directo con la propuesta de flora/fauna nativa chilena de Pedraza — es un argumento de posicionamiento, no un dato de demanda medida.
- Cómo entrar a la categoría: la ruta más citada para marcas chicas es print-on-demand (Merch on Demand, o conectar Seller Central a un proveedor POD tipo Printify/Printful) para partir sin stock ni logística, y recién migrar a inventario propio/FBA cuando haya validación de venta ([Gelato, "How To Sell Art On Amazon Step-By-Step In 2026"](https://www.gelato.com/blog/how-to-sell-art-on-amazon); [Printify, "How to sell art on Amazon: Your 7-step guide"](https://printify.com/blog/how-to-sell-art-on-amazon/); [sell.amazon.com/sell/art](https://sell.amazon.com/sell/art) — página oficial, listada solo como referencia). Como Pedraza ya tiene proveedor propio en EEUU (no POD genérico), esta ruta es antecedente de mercado, no necesariamente el modelo a copiar. 🟡 VERIFICAR contra el modelo real del proveedor.
- Consejo recurrente en las guías de listing: título/imagen/descripción de calidad + SEO de keywords son el filtro de descubrimiento (Amazon prioriza relevancia + calidad de listing), y evitar arte con derechos de autor de terceros (Amazon aplica "strikes" rápido ante infracciones) ([Gelato, ídem](https://www.gelato.com/blog/how-to-sell-art-on-amazon)). Esto es guía general de mejores prácticas, no un dato duro de competencia.

**D.1.2 Jigsaw puzzles**

- Una fuente de analítica de mercado (asinsight.com, herramienta de terceros, no Amazon oficial) reporta la categoría de puzles con **cerca de 57.800 listings y más de 1 millón de reseñas acumuladas** en EEUU, lo que indica un mercado maduro y de alta competencia; agrega que la banda de precio **US$10–20 concentra ~49% del surtido** y es donde la competencia es más dura para nuevos entrantes, con precio promedio del top 20/50/100 en torno a **US$17–19** ([asinsight.com, "2025 Amazon Best Selling jigsaw puzzles"](https://www.asinsight.com/report/US/jigsaw-puzzles)). 🟡 VERIFICAR — cifra de una sola herramienta de terceros, no confirmada con fuente oficial de Amazon; tratarla como orden de magnitud, no como dato preciso.
- Jugadores de marca reconocidos que aparecen recurrentemente en el top de búsqueda: Buffalo Games, Ravensburger — es decir, hay marcas establecidas con reconocimiento previo compitiendo en el mismo espacio de precio ([indexbox.io análisis de mercado](https://www.indexbox.io/blog/games-articles-for-funfair-table-or-parlour-games-including-pintables-tables-for-casino-games-bowling-alley-equipment-nes-in-heading-no-9504-usa-brands-2025-4/)). 🟡 VERIFICAR con datos propios antes de fijar precio.
- Lectura para Pedraza: la categoría es muy poblada; la diferenciación real más citable no es precio sino diseño/temática distintiva (arte propio y reconocible) — coincide con el mismo argumento de nicho de flora/fauna nativa que en wall art, pero no hay fuente que confirme que "nicho + origen país" mueva conversión en Amazon específicamente. 🟡 SUPUESTO.

**D.1.3 Home decor (platos, botellas — accesorios de mesa/cocina)**

- Referral fee de "Home & Kitchen" está congelado en 15% para 2026 (ver D.2.3). No se encontró un análisis de competencia específico y citable para "platos ilustrados" o "botellas ilustradas" como sub-nicho — es un universo muy amplio dentro de Home & Kitchen. 🟡 VERIFICAR con búsqueda de nicho más acotada antes de lanzar.
- Misma tendencia de fondo que en wall art: diseño hogar 2026 se inclina a motivos botánicos/naturaleza y materiales naturales ([pulsepathlife.com, ídem](https://pulsepathlife.com/home-decor-trends-2026-a-modern-mood-board-for-botanical-earthy-styles/)).

**D.1.4 Novelty socks (calcetines)**

- Existen nodos de "Best Sellers" propios por segmento (hombre, mujer, niña) y una categoría amplia de "animal socks"/"novelty socks" con muchísimos sellers third-party de origen chino visibles en resultados de búsqueda (ej. WeciBor y decenas de marcas de nombre genérico) — señal de categoría saturada y de precio bajo/alto volumen ([amazon.com/animal-socks/s](https://www.amazon.com/animal-socks/s?k=animal+socks); [amazon.com/Best-Sellers-Mens-Novelty-Socks](https://www.amazon.com/Best-Sellers-Mens-Novelty-Socks/zgbs/fashion/9056998011)). No se pudo confirmar volumen de venta real (WebFetch a la página de producto no disponible en este entorno). 🟡 VERIFICAR.
- Lectura: es la categoría más "commodity" y de menor barrera de entrada del catálogo de Pedraza — también la de menor diferenciación posible salvo por el arte impreso. Priorizarla después de validar wall art/puzles. 🟡 SUPUESTO (juicio, no dato).

**D.1.5 Notebooks / libretas (journals)**

- El mercado de journals/notebooks en Amazon está descrito como dividido entre tendencias virales de alto volumen (redes sociales) y nichos de e-commerce establecidos a largo plazo; los "guided journals" (gratitud, bienestar) están descritos como saturados con marcas ya posicionadas, mientras que sub-nichos más específicos (ansiedad, dietas, prompts temáticos) tendrían más espacio ([accio.com, "Amazon Top Seller Journal Trends 2025"](https://www.accio.com/business/amazon-top-seller-journal)). Esto aplica a diarios con contenido guiado, no necesariamente a libretas de tapa ilustrada sin contenido interior — que es más parecido al espacio de "papelería con diseño" que al de "low-content books". 🟡 VERIFICAR — no se encontró análisis específico de libretas con diseño de tapa (sin prompts) como sub-categoría.
- Dato de contexto: Amazon viene *reduciendo* su propio catálogo de marca privada (Amazon Basics y similares) por bajo desempeño y escrutinio antimonopolio, lo que en teoría deja algo más de espacio a marcas terceras en categorías donde antes competía Amazon directamente ([Retail Dive, "Amazon scaling back private label business"](https://www.retaildive.com/news/amazon-scaling-back-private-label-business/627373/)). Dato indirecto, no específico de libretas.

**D.1.6 Patrón general de listings que funcionan (across categorías)**

Elementos citados de forma consistente en varias fuentes como lo que distingue listings ganadores en categorías de diseño/decoración:
- Título e imágenes de alta calidad + SEO de keywords en título, bullets, descripción y "search terms" de backend ([Gelato](https://www.gelato.com/blog/how-to-sell-art-on-amazon)).
- Consistencia temática/de marca reconocible (nicho claro) en vez de catálogo genérico — mencionado como diferenciador en wall art y journals por igual.
- A+ Content y Brand Store activados (ver D.3) — citado repetidamente como palanca de conversión para marcas con Brand Registry.

### D.2 Mecánica para un seller nuevo en 2026

**D.2.1 Planes de venta (Individual vs. Professional)**

- **Individual:** US$0.99 por unidad vendida, sin suscripción mensual — pensado para menos de ~40 unidades/mes. **Professional:** US$39.99/mes fijo, sin cargo por unidad (además de los referral fees, que aplican a ambos planes) ([sell.amazon.com/blog/amazon-professional-vs-individual-selling-plan](https://sell.amazon.com/blog/amazon-professional-vs-individual-selling-plan) citado vía [Threecolts](https://www.threecolts.com/blog/amazon-individual-vs-professional-selling-plan/) y [goaura.com](https://goaura.com/blog/amazon-individual-seller); el punto de equilibrio matemático (~41 items/mes) es cálculo de terceros, no cifra oficial). 🟡 VERIFICAR el precio exacto vigente en el momento del alta, en `sell.amazon.com/pricing`.
- El plan Professional es obligatorio para acceder a Brand Registry, A+ Content, Advertising (Sponsored Products) y para conectar catálogos vía API/POD — de facto, es el plan que necesita una marca (no un revendedor ocasional).

**D.2.2 FBA vs. FBM**

- **FBA (Fulfillment by Amazon):** Amazon almacena, empaca, envía y atiende al cliente; el producto queda habilitado para el sello Prime, lo que se asocia a mayor conversión (cifras de "20–30% más conversión" citadas por fuentes de agencias/consultoras, no por Amazon — tratar como referencial, no exacto) ([texaslogisticservices.com, "FBA vs FBM in 2026"](https://texaslogisticservices.com/blog/fba-vs-fbm-in-2026-which-fulfillment-model-is-right-for-your-business/)). 🟡 VERIFICAR cifra de conversión.
- Contra: fees de FBA subieron en 2026 (ver D.2.3), y el modelo limita el control de empaque/experiencia de unboxing — no se pueden meter insertos promocionales que rompan las reglas de Amazon (ver D.4.3), y las cajas son genéricas de Amazon.
- **FBM (Fulfillment by Merchant):** el seller (o su 3PL) controla stock, empaque y envío — más margen y más control de marca en el unboxing, pero sin badge Prime automático y con la carga completa de atención al cliente (Amazon exige respuesta en 24 horas). Desde **febrero de 2026**, todas las órdenes FBM deben incluir etiqueta de devolución prepagada ([titannetwork.com, "FBA vs FBM: The 2026 EBITDA Playbook"](https://titannetwork.com/fba-vs-fbm/)). 🟡 VERIFICAR fecha exacta y alcance de esta regla con fuente oficial de Amazon.
- Para una marca chica con proveedor ya instalado en EEUU (como Pedraza), lo citado como enfoque recomendado es un **modelo híbrido**: FBA para los SKUs de mayor rotación/menor tamaño (prints, calcetines, libretas) y FBM para lo voluminoso/frágil/lento (platos, puzles grandes) — según el mismo criterio de tamaño, velocidad y margen ([titannetwork.com, ídem](https://titannetwork.com/fba-vs-fbm/)). Esto es recomendación de un blog especializado, no política de Amazon. 🟡 SUPUESTO — validar con costos reales del proveedor antes de decidir.

**D.2.3 Fees vigentes 2026 (referral fee y FBA)**

- **Referral fee:** para la enorme mayoría de categorías (incluidas **Home & Kitchen, Arts/Crafts & Sewing, Office Products y Toys & Games** — las que tocan a Pedraza) la tasa es **15% del precio total de venta** (precio del ítem + envío cobrado al comprador + gift wrap, sin incluir impuestos), con un **mínimo de US$0.30 por unidad**. Amazon "congeló" (no subió) los referral fees de EEUU tanto en 2025 como en 2026 ([Amazon Selling Partners, "Update to U.S. Referral and Fulfillment by Amazon fees for 2026"](https://sellingpartners.aboutamazon.com/update-to-u-s-referral-and-fulfillment-by-amazon-fees-for-2026) — página oficial de Amazon, citada vía snippet de búsqueda y agregadores; corroborado también por [feedvisor.com](https://feedvisor.com/university/referral-fee/) y [runfutureproof.com](https://www.runfutureproof.com/amazon-fees/handmade)).
- **FBA fulfillment fees:** suben en promedio **US$0.08 por unidad vendida** en 2026 (menos de 0.5% del precio promedio de venta, según la nota oficial de Amazon). Estructura por bandas de precio (bajo US$10 / US$10–50 / sobre US$50); los productos bajo US$10 califican automáticamente para "Low-Price FBA", con tarifas ~US$0.86 más bajas en promedio que el FBA estándar ([Amazon Selling Partners, ídem](https://sellingpartners.aboutamazon.com/update-to-u-s-referral-and-fulfillment-by-amazon-fees-for-2026); [sellercentral.amazon.com/help — "2026 US FBA fulfillment fee changes"](https://sellercentral.amazon.com/help/hub/reference/external/GABBX6GZPA8MSZGW) y ["2026 US Low Price FBA fulfillment fee"](https://sellercentral.amazon.com/help/hub/reference/external/GMUTB89XM7AATPR3) — páginas oficiales de Seller Central Help, requieren sesión iniciada por lo que no se pudieron leer en vivo aquí; se citan según lo reportado por agregadores especializados).
- **Recargo de combustible/logística:** desde el **17 de abril de 2026**, Amazon aplica un **recargo de 3.5%** sobre las tarifas de fulfillment de FBA en EEUU y Canadá (~US$0.16–0.18 adicionales por unidad en tamaños estándar) ([amzprep.com, "Amazon FBA Fees 2026: Full Breakdown + April 17 Surcharge Update"](https://amzprep.com/amazon-fba-fees/); [sellersnap.io, "Amazon Fee Changes 2026"](https://sellersnap.io/amazon-fee-changes-and-updates/)). 🟡 VERIFICAR con el rate card oficial vigente al momento de operar — este research es de julio 2026 y el recargo ya estaría activo, pero conviene confirmar en Seller Central antes de fijar precios.
- **Storage fees mensuales 2026:** entre **US$0.53 y US$4.28 por pie cúbico** para productos de tamaño estándar, según temporada (más caro oct–dic) (mismo grupo de fuentes de agregadores citado arriba). 🟡 VERIFICAR cifra exacta con el Fee Preview Report de Seller Central antes de decidir volumen de inventario.
- **Orientación práctica:** existe una herramienta oficial — el **Fee Preview Report** dentro de Seller Central — para calcular el costo real por SKU antes de fijar precio; ningún cálculo hecho por fuera de esa herramienta (incluido este research) debería usarse para fijar precio final. 🟡 VERIFICAR siempre en Seller Central.

**D.2.4 Requisitos para sellers internacionales / latinoamericanos (Chile)**

- No se requiere entidad legal en EEUU ni cuenta bancaria en EEUU para vender desde Latinoamérica: se puede operar con la empresa chilena y usar FBA para el fulfillment ([sell.amazon.com/global-selling/latin-america-to-usa](https://sell.amazon.com/global-selling/latin-america-to-usa) — página oficial de Amazon, referenciada solo por snippet de búsqueda. 🟡 VERIFICAR leyendo la página completa antes de iniciar el registro).
- Registro: dentro de Seller Central, desde el menú Inventory → "Sell globally" → seleccionar el país/región → "Register" y completar los datos adicionales que pida Amazon (fiscales, de producto, etc.) — mismo flujo mencionan fuentes oficiales y foros de sellers ([sell.amazon.com/global-selling](https://sell.amazon.com/global-selling); hilo de Seller Forums de un vendedor preguntando cómo expandirse de EEUU a Chile/Colombia — confirma que el flujo de "Sell Globally" es el mecanismo estándar: [sellercentral.amazon.com/seller-forums](https://sellercentral.amazon.com/seller-forums/discussions/t/ca76e46a-af54-4ee2-b323-88110be6ba01)).
- Documentación fiscal: los sellers internacionales completan el formulario **W-8BEN** (o W-8BEN-E si es persona jurídica) como identificación fiscal ante EEUU, más una cuenta bancaria capaz de recibir transferencias en USD ([blog.utoppia.com, "How to Receive Amazon Seller Central Payments in 2026"](https://blog.utoppia.com/how-to-receive-payments/amazon-seller-central/)). Como no hay obligación de banco en EEUU, la vía más citada para sellers latinoamericanos es un proveedor de pagos internacional tipo **Payoneer** (entrega IBAN virtual en USD/GBP/EUR para que Amazon liquide ahí; aprobación en 1–3 días hábiles) ([marcabien.com, "Amazon FBA Payoneer Account Setup"](https://marcabien.com/en/amazon-fba-payoneer-account-setup-step-by-step-guide)). 🟡 VERIFICAR cuál método de pago usará el proveedor de Pedraza en EEUU — puede que ya tengan uno resuelto.
- **Seguro de responsabilidad civil de producto:** Amazon exige a los sellers Professional (Pro Merchants) contratar seguro de responsabilidad civil comercial cuando las ventas superan **US$10.000 mensuales durante 3 meses consecutivos** (o si Amazon lo pide explícitamente), con cobertura mínima de **US$1.000.000 por evento y en agregado**, incluyendo a Amazon.com Services LLC como asegurado adicional, y deducible no mayor a US$10.000 ([compliancegate.com, "Amazon Product Liability Insurance Requirements"](https://www.compliancegate.com/amazon-product-liability-insurance/); [payoneer.com, "What Is Liability Insurance for Amazon Sellers"](https://www.payoneer.com/resources/business/what-is-liability-insurance-for-amazon-sellers/)). Cuentas Individual no están obligadas. 🟡 VERIFICAR el umbral y montos exactos en la página oficial de Seller Central antes del umbral de ventas.

**D.2.5 Amazon Handmade — ¿aplica para Pedraza?**

- Amazon Handmade es un programa para **artesanos individuales o equipos de 20 personas o menos**, donde el producto debe estar **hecho, alterado o ensamblado a mano** por el vendedor o su equipo, usando herramientas manuales y maquinaria liviana. **Prohíbe explícitamente** tercerizar la producción a fabricantes externos: "products that are designed by you but manufactured by a third party on your behalf don't qualify" — es decir, mandar a fabricar el diseño a un proveedor/fábrica externa **descalifica** al producto de Handmade, aunque el diseño sea propio ([sellerapp.com, "Amazon Handmade: Everything Sellers Need To Know In 2026"](https://www.sellerapp.com/blog/amazon-handmade/); página oficial [sell.amazon.com/programs/handmade](https://sell.amazon.com/programs/handmade) referenciada pero no legible en vivo).
- Sí hay una excepción citada para "alteración a mano" (ej. tomar una prenda de un proveedor externo como base y coserle algo a mano encima) — pero eso no aplica al modelo de Pedraza de imprimir/fabricar productos en volumen vía un proveedor en EEUU.
- **Conclusión para Pedraza:** dado que la marca ya tiene "proveedor allá" (fabricación tercerizada, no manual artesanal en el sentido de Handmade), **lo más probable es que NO califiquen para Amazon Handmade** — el modelo correcto es **Seller Central estándar (Professional selling plan) + Brand Registry**, no Handmade. 🟡 VERIFICAR de todas formas con el proveedor y, si hay dudas, contactar directamente al soporte de Amazon Handmade antes de descartarlo del todo — la definición exacta de "fabricado por terceros" puede tener matices no capturados en fuentes secundarias.
- Fee de Handmade si calificara: referral fee de 15% (igual al estándar), y la suscripción Professional se las exime a los aprobados (ahorro citado de US$480/año) ([sellerapp.com, ídem](https://www.sellerapp.com/blog/amazon-handmade/)). Dato secundario, no relevante si no califican.

**D.2.6 Brand Registry**

- **Requisito central:** tener una **marca registrada o en trámite (pending)** ante la oficina de marcas del país correspondiente (para EEUU, USPTO; también acepta marcas registradas en Chile si aplica a la tienda de Amazon correspondiente — 🟡 VERIFICAR si una marca chilena habilita Brand Registry en Amazon.com EEUU o si se necesita marca registrada en EEUU específicamente), más un logo con el nombre de marca fijado físicamente al producto o su empaque. Amazon acepta tanto marcas denominativas (texto) como mixtas/figurativas que incluyan letras o números ([junglescout.com, "Amazon Brand Registry"](https://www.junglescout.com/blog/amazon-brand-registry/); [kwickmetrics.com](https://www.kwickmetrics.com/blog/amazon-brand-registry); página oficial [sell.amazon.com/brand-registry](https://sell.amazon.com/brand-registry) no legible en vivo).
- **Beneficios citados:** protección de marca (bloqueo automático de listings de terceros no autorizados en el mismo ASIN/marca), control sobre título/imágenes/descripción del listing, acceso a **A+ Content**, herramientas de monitoreo de marca, y es requisito previo para acceder a **Amazon Stores**, **Amazon Attribution** y el **Brand Referral Bonus** (ver D.3 y D.4) ([junglescout.com, ídem](https://www.junglescout.com/blog/amazon-brand-registry/)).
- **Implicancia práctica para Pedraza:** si van a invertir en A+ Content, Store y en traer tráfico desde Instagram con el incentivo del Brand Referral Bonus, **necesitan Brand Registry** — lo que a su vez requiere haber registrado (o al menos solicitado) la marca "Pedraza Ilustración" formalmente. Esto es una dependencia de calendario: el trámite de marca puede tardar y debería iniciarse **antes** del lanzamiento en Amazon, no después. 🟡 VERIFICAR estado actual del registro de marca de Pedraza Ilustración — no investigado en este research, está fuera del alcance de "panorama Amazon" (queda como pendiente crítico, ver `pendientes-operador.md`).

### D.3 Herramientas de contenido en Amazon

**D.3.1 A+ Content**

- Disponible **gratis** para cualquier seller con Brand Registry (o vendedores 1P/vendor); permite hasta un cierto número de módulos de imagen + texto + banners debajo de los bullets del listing, para reforzar historia de marca y especificaciones visuales. Se cita un impacto de **hasta +8% en ventas** al usar A+ Content básico frente a no usarlo ([pattern.com, "Amazon A+ Content vs. Premium A+ Content"](https://www.pattern.com/blog/what-are-the-differences-between-a-content-and-premium-a-content)). 🟡 VERIFICAR esa cifra de +8% — es citada por una agencia, no por Amazon directamente; tratar como referencia optimista, no garantía.
- **Premium A+ (A++):** solo por invitación de Amazon, típicamente para marcas grandes/vendors con presupuestos de cientos de miles de dólares — **no relevante para el lanzamiento inicial de Pedraza**.

**D.3.2 Amazon Stores (Brand Store)**

- Página propia tipo "mini sitio web" dentro de Amazon, gratuita para miembros de Brand Registry, donde se puede mostrar el catálogo completo bajo una identidad de marca cohesiva y contar la historia de la marca. El costo es solo de producción de contenido y tiempo interno, no una tarifa de Amazon ([bluewheelmedia.com, "Content Considerations: Amazon Brand Store & Amazon Posts"](https://www.bluewheelmedia.com/resources-whitepapers/content-considerations-amazon-brand-store-amazon-posts)).
- Para Pedraza esto es directamente aprovechable: pueden usar el storytelling de "flora y fauna nativa chilena" que ya funciona en Instagram y trasladarlo (adaptado a inglés) a la Store — es la pieza de contenido que más se parece a lo que ya saben producir.

**D.3.3 Amazon Posts — DISCONTINUADO (dato importante para no perder tiempo)**

- **Amazon Posts fue descontinuado por Amazon** — no está disponible para nuevos lanzamientos en 2026. Cronología oficial: **3 de junio de 2025** Amazon anuncia la baja del programa (usuarios nuevos pierden acceso a la API de inmediato); **16 de junio de 2025** los usuarios existentes dejan de poder crear contenido nuevo; **31 de julio de 2025** el apagado es total (todas las APIs de Posts devuelven error, el contenido existente deja de ser accesible) ([ppc.land, "Amazon Posts officially discontinued"](https://ppc.land/amazon-posts-officially-discontinued/); [estorefactory.com, "Amazon Officially Shuts Down Posts Program"](https://www.estorefactory.com/amazon-update/amazon-officially-shuts-down-posts-program/); [myamazonguy.com](https://myamazonguy.com/brand-registry/how-to-set-up-amazon-social-posts/)). Amazon habría citado impresiones en baja y el rediseño de sus páginas de búsqueda/detalle como motivo.
- **Acción concreta para el playbook:** cualquier mención previa de "Amazon Posts" en materiales de planificación de Pedraza (si la hubiera) debe eliminarse o reemplazarse — a julio 2026 esa herramienta **ya no existe**. El foco de contenido nativo en Amazon debe ir a **A+ Content y Store** (D.3.1–D.3.2), y las campañas de "estilo social" deben vivir en Instagram/redes, no en Amazon.

### D.4 Cómo el social (Instagram) apoya el lanzamiento en Amazon

**D.4.1 Amazon Attribution**

- Herramienta **gratuita** para sellers/vendors con Brand Registry (y agencias) que genera **enlaces de seguimiento (tags de atribución)** para campañas fuera de Amazon (Instagram, Google, email, influencers, TikTok, etc.), y mide impresiones, clics, vistas de página de producto, add-to-cart y compras atribuidas a cada campaña externa. Usa un modelo de **último clic con ventana de 14 días**: si el comprador hace clic en el link y compra dentro de esos 14 días, la venta se atribuye a esa campaña ([sellerlabs.com, "Amazon Attribution: Measuring External Traffic ROI"](https://www.sellerlabs.com/knowledge-base/amazon-attribution-measuring-external-traffic-roi/); [sarasanalytics.com, "Amazon Attribution Guide 2025"](https://www.sarasanalytics.com/blog/amazon-attribution-guide); página oficial [advertising.amazon.com/library/guides/basics-of-amazon-attribution](https://advertising.amazon.com/library/guides/basics-of-amazon-attribution) no legible en vivo). Disponible en EEUU, Canadá, Reino Unido, Alemania, Francia, Italia, España y México — no se menciona Chile porque Chile no es donde se hace la venta (la venta es en Amazon.com EEUU, el requisito es Brand Registry en esa tienda, no residencia del vendedor). 🟡 VERIFICAR disponibilidad exacta para una cuenta chilena vendiendo en Amazon.com.

**D.4.2 Brand Referral Bonus**

- Programa para sellers con Brand Registry que usan Amazon Attribution: Amazon devuelve un **bono promedio de 10% del valor de la venta atribuida al tráfico externo**, aplicado como **crédito contra futuros referral fees** (no es efectivo directo). Si el comprador hace más compras de la misma marca dentro de los 14 días desde el clic, esas también califican para el bono. Hay un **retraso de ~2 meses** antes de que el crédito aparezca en la cuenta ([sagemailer.com, "Amazon Referral Bonus - How It Works?"](https://sagemailer.com/blog/amazon-launches-brand-referral-bonus-program/); [adbrew.io, "What is the Amazon Brand Referral Bonus"](https://adbrew.io/blog/what-is-the-amazon-brand-referral-bonus)). 🟡 VERIFICAR el % exacto vigente (algunas fuentes hablan de "hasta 10%", no un fijo garantizado) directamente en Seller Central al momento de inscribirse.
- **Relevancia directa para Pedraza:** esto es la pieza que conecta el plan principal (Instagram → Shopify) con el anexo Amazon: el mismo tráfico de Instagram, si se dirige con un link de Atribución hacia el listing de Amazon en vez de (o además de) Shopify, genera un descuento efectivo de hasta ~10% en fees de Amazon. Requiere Brand Registry activo antes de poder usarlo.

**D.4.3 Estrategia de reseñas legítima**

**Amazon Vine (programa oficial):**
- Programa por invitación donde Amazon conecta productos nuevos/recién lanzados de sellers inscritos con "Vine Voices" (reseñadores de confianza de Amazon), quienes reciben el producto gratis a cambio de una reseña honesta. El seller **no elige al reseñador, no aprueba la reseña ni puede pedir que la cambien**; la reseña queda marcada con la insignia "Vine Voice" y no hay garantía de que sea positiva ([sellersprite.com, "Amazon Vine Program Explained"](https://www.sellersprite.com/en/blog/amazon-vine-program-explained-legit-product-reviews); [goaura.com, "Amazon Vine Program: Is It Worth It? (2026)"](https://goaura.com/blog/amazon-vine-program)). 🟡 VERIFICAR costo/requisitos de inscripción exactos (unidades a donar, límite de ASINs) en la página oficial de Seller Central.

**Insert cards (tarjetas dentro del empaque) — qué permite y qué prohíbe Amazon:**
- **Prohibido:** pedir explícitamente una reseña *positiva*, ofrecer cualquier tipo de incentivo o compensación a cambio de una reseña (descuento, producto gratis, sorteo, etc.), y **desviar a clientes insatisfechos** para que contacten al vendedor en vez de dejar una reseña negativa en Amazon — todo esto cae bajo manipulación de reseñas y puede derivar en suspensión de cuenta ([varias fuentes convergentes: sellersprite.com](https://www.sellersprite.com/en/blog/amazon-product-inserts-for-more-reviews); [supplykick.com, "Amazon Product Inserts: Rules & Best Practices"](https://www.supplykick.com/blog/amazon-product-inserts-guide); [riverbendconsulting.com, "Amazon Product Insert Cards: Key Guidelines"](https://riverbendconsulting.com/blog/amazon-product-insert-cards/)).
- **Permitido:** un insert con un agradecimiento y una invitación **neutral** a dejar una reseña honesta basada en la experiencia del cliente (sin pedir que sea positiva, sin incentivo, sin "historias tristes" que generen presión emocional — Amazon las trata como manipulación sutil también) ([riverbendconsulting.com, ídem](https://riverbendconsulting.com/blog/amazon-product-insert-cards/)).
- 🟡 VERIFICAR el texto exacto de la política oficial de Amazon ("Community Guidelines" / "Product Review Policy") en `sellercentral.amazon.com` antes de diseñar cualquier insert — este research se basa en resúmenes de terceros, consistentes entre sí pero no leídos directo de la fuente primaria.
- **Aplicación práctica para Pedraza:** dado que ya usan un empaque con identidad de marca (probablemente con "ASMR de empaque" como parte de su contenido en Instagram — ver C.2.2), el insert permitido (agradecimiento neutral + código QR a Instagram, por ejemplo) es compatible con la política — pero cualquier insert que ofrezca descuento futuro a cambio de reseña, o que pida específicamente "5 estrellas", no lo es.

### D.5 Calendario comercial EEUU relevante

| Fecha comercial | 2026 (confirmada) | Fuente |
|---|---|---|
| **Prime Day** | **23–26 de junio de 2026** (4 días, arrancó 12:00 AM PDT del 23) — Amazon movió el evento de julio a junio en 2026, reportadamente para evitar cruce con el Mundial y el 250° aniversario de EEUU en julio | [aboutamazon.com/news/retail/amazon-prime-day-2026-date](https://www.aboutamazon.com/news/retail/amazon-prime-day-2026-date) (página oficial de Amazon, dato tomado del snippet de búsqueda que la cita); corroborado por [Variety](https://variety.com/2026/shopping/news/amazon-prime-day-june-2026-date-deals-what-to-buy-online-1236739562/) y [NBC News](https://www.nbcnews.com/select/shopping/amazon-prime-day-dates-2026-rcna347962). **Importante: ya pasó** respecto a la fecha actual del research (23 jul 2026) — no aplica para un lanzamiento inmediato, sí como referencia para planificar Prime Day 2027. |
| **Black Friday** | **27 de noviembre de 2026** | [make-a-calendar.com](https://make-a-calendar.com/when-is/black-friday); [shopback.com, "US 2026 Sale Calendar"](https://www.shopback.com/blog/finance/us-2026-sale-calendar) |
| **Cyber Monday** | **30 de noviembre de 2026** (también reportado como "1 de diciembre de 2026" en otra fuente — ver nota) | [make-a-calendar.com](https://make-a-calendar.com/when-is/black-friday); nota de discrepancia: [nationaldaycalendar.com](https://nationaldaycalendar.com/celebrations/cyber-monday-monday-after-thanksgiving) da 1 de diciembre. Cyber Monday es siempre el lunes después de Thanksgiving (26 nov 2026 es Thanksgiving en EEUU → el lunes siguiente cae **30 de noviembre**), así que 30/11 es la fecha matemáticamente consistente. 🟡 VERIFICAR — corregir la fuente que dice 1° de diciembre antes de usar en el calendario final. |
| **Mother's Day (EEUU)** | **Domingo 10 de mayo de 2026** (segundo domingo de mayo) | [wincalendar.com](https://www.wincalendar.com/Mothers-Day); [awarenessdays.com](https://www.awarenessdays.com/awareness-days-calendar/mothers-day-us/) — **ya pasó** respecto a hoy (23 jul 2026); referencia para 2027 (será 9 de mayo de 2027, segundo domingo de mayo — 🟡 VERIFICAR). |
| **Temporada navideña / holiday shopping** | Arranca en la práctica con BFCM (fin de noviembre) y se extiende hasta fines de diciembre; para FBA, Amazon suele fijar plazos de inventario entrante a fulfillment centers varias semanas antes (típicamente cierran ventanas de inbound recomendadas a inicios de noviembre) | 🟡 VERIFICAR fechas límite oficiales de inbound 2026 en Seller Central — no confirmadas en este research, cambian año a año y Amazon las publica más cerca de la fecha. |

**Lectura para el anexo Rampa EEUU:** dado que hoy es 23 de julio de 2026, las dos fechas grandes de venta que ya pasaron este año (Prime Day de junio, Mother's Day de mayo) **no son objetivo de lanzamiento 2026** — la ventana relevante más próxima y de mayor impacto es **BFCM (27–30 de noviembre de 2026)**, seguida de la temporada de regalos de diciembre. Si el objetivo es "abrir pronto" en Amazon, tiene sentido apuntar el lanzamiento a tener listing, reseñas iniciales (vía Vine) y Brand Registry resueltos **antes de la ventana de inbound de octubre/noviembre**, para llegar con inventario ya en fulfillment centers a tiempo para BFCM. 🟡 SUPUESTO de planificación — no es una fecha límite oficial de Amazon, es una inferencia razonable a partir del calendario. **Nota:** este calendario BFCM de EEUU (Black Friday 27 nov, Cyber Monday 30 nov) es un evento distinto del calendario comercial chileno de la sección B — coinciden en la fecha de Black Friday por coincidencia de cálculo (última semana de noviembre en ambos países), pero Cyber Monday CL y Cyber Monday EEUU son eventos separados con fechas propias.

---

## Registro del playbook: qué funcionó y qué no

> Consolida las bitácoras metodológicas de los tres borradores fuente. El hallazgo transversal — WebFetch/curl bloqueados por la política de red del entorno, confirmado con dominios de control neutros (`example.com`, `en.wikipedia.org`, `web.archive.org`) que dieron el mismo 403 — ya está detallado en la nota metodológica del encabezado y no se repite aquí.

**Qué funcionó bien (técnica de búsqueda):**
- Queries de WebSearch específicas, en español y con año explícito (ej. `"CyberDay 2026 fecha oficial"`, `"Día del Niño Chile 2026 fecha agosto"`) devolvieron resultados directos y bien sintetizados de medios chilenos confiables (BioBioChile, El Mostrador, T13, La Tercera, CCS).
- Buscar cada fecha comercial por separado (en vez de un query genérico tipo "calendario comercial Chile 2026") dio resultados mucho más precisos.
- Preguntar directamente por resultados post-evento (ej. "CyberDay resultados ventas ticket promedio") funcionó muy bien porque la CCS y medios especializados publican cifras oficiales de cierre con detalle.
- Buscar competidores/comparables por descripción de producto ("tienda diseño flora fauna Chile") en vez de por nombre de marca reveló a Bendito como comparable directo y confirmó la multicanalidad ya existente de Pedraza.
- Para Amazon: los fees y el congelamiento 2025-2026, y la descontinuación de Amazon Posts, se triangularon en 3-4+ fuentes independientes cada uno — alta confianza en esos datos puntuales.

**Qué no funcionó / limitaciones y pendientes específicos:**
- La feria **"Matria"** mencionada en el brief no arrojó ningún resultado verificable pese a varios intentos de query — puede no existir bajo ese nombre exacto, ser muy reciente/local, o el nombre puede estar mal recordado.
- **Ñam** resultó ser un festival gastronómico, no de diseño — importante para no incluirlo por error como canal de distribución de producto.
- La fecha de **CyberMonday Chile 2026** no está anunciada todavía (a 23 jul 2026); se espera el anuncio recién a fines de septiembre 2026 (patrón similar al de CyberDay, anunciado ~3 semanas antes). Vale la pena programar una re-consulta a fines de septiembre.
- Algunos datos de comportamiento en redes sociales (58%/83% de Accenture) resultaron ser de **2020**, no de 2026 — riesgo real de "actualidad falsa" en búsquedas sin fecha de publicación visible; se dejaron marcados 🟡 VERIFICAR por antigüedad, no se descartaron.
- **Discrepancia sin resolver** en la fecha exacta de Cyber Monday EEUU 2026 (30 nov vs. 1 dic según la fuente) — se resolvió por cálculo (lunes después de Thanksgiving = 30 nov), pero queda marcada 🟡 VERIFICAR antes de publicar el calendario final.
- **No se confirmó el estado actual del registro de marca "Pedraza Ilustración"** (Chile y/o EEUU) ni si una marca chilena habilita Brand Registry en Amazon.com EEUU — es la dependencia crítica y bloqueante de calendario para todo el anexo Amazon (Brand Registry, A+ Content, Store, Attribution y Brand Referral Bonus dependen de esto). Queda como el pendiente de mayor prioridad en `pendientes-operador.md`.
- Cifras citadas por agencias/consultoras con incentivo comercial propio (+8% en ventas por A+ Content, +20-30% de conversión con FBA/Prime, "40-60% más distribución" por contenido original, "6x más guardados" en antes/después, "1,4x más alcance" en carruseles) se marcaron explícitamente como **sin fuente dura** — no deben citarse como estadística confirmada en materiales de decisión, solo como orientación de práctica.
- No se investigó tributación de EEUU (sales tax, tratado Chile-EEUU) — recomendado como investigación aparte con fuente contable/legal, fuera del alcance de este documento de mercado.
- Sin dato de competencia específico y citable para platos, botellas y libretas de tapa ilustrada como sub-nichos en Amazon — pendiente de una búsqueda más granular o de análisis directo dentro de Seller Central ("Product Opportunity Explorer", no explorada en este research).

**Conclusión operativa para futuras fases de research:** dado que el bloqueo de WebFetch/curl fue de infraestructura y no de los sitios, el siguiente paso correcto para elevar la confianza de los datos marcados 🟡 es reintentar la lectura directa (WebFetch, products.json, páginas oficiales de Amazon/Meta/CCS) desde un entorno sin esta restricción de red, en vez de asumir que los datos actuales son definitivos. Mientras tanto, este documento debe tratarse como la mejor síntesis posible vía WebSearch, no como lectura verificada de fuente primaria.
