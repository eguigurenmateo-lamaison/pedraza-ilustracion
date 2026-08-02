# Auditoría de Shopify y Klaviyo — 2 de agosto de 2026

Auditorías corridas por el operador sobre las cuentas reales.
Periodo: últimos 90 días (4 de mayo al 2 de agosto de 2026).
Material interno. **Fuente de verdad para `cro.html`, `email.html` y `tienda-cambios.html`.**

---

## 1. EL HALLAZGO PRINCIPAL: el 23% del tráfico va a un producto que no se puede comprar

El **Puzzle Aves y Flores de Chile** es el producto más visto y más vendido de la tienda: **8.558 vistas y $3.108.644 en 90 días**. Hoy tiene **0 unidades y la venta sin stock desactivada**: literalmente no se puede comprar.

Esas 8.558 vistas son el **23% de las 37.747 sesiones** del periodo.

Hay 6 productos activos con stock en cero, tres de ellos puzzles que siguen recibiendo tráfico: Aves y Flores, Cetáceos y Mariposas y Escarabajos.

🟢 **Y se está pagando por ese tráfico.** La auditoría de Google mostró que los productos "agotados" son el 18% del gasto publicitario. Se paga por llevar gente a fichas que no pueden convertir.

**Esto explica de una vez tres cosas que estaban sueltas:**
- Por qué la conversión general es de 1,11%.
- Por qué la tasa de agregar al carrito en móvil es tan baja.
- Por qué en Google los productos agotados "convierten" con retorno 6,40: la gente llega buscando el puzzle, no lo puede comprar, **y compra otra cosa igual**.

El stock llega el 15 de agosto y la preventa abre el 6. Es la corrección de mayor impacto de todo el diagnóstico y ya tiene fecha.

---

## 2. El embudo real (90 días)

| Paso | Cantidad | % del total | % del paso anterior |
|---|---:|---:|---:|
| Sesiones | 37.747 | 100% | — |
| Agregaron al carrito | 1.358 | 3,59% | 3,59% |
| Llegaron al pago | 1.004 | 2,65% | 73,9% |
| **Compraron** | **420** | **1,11%** | **41,8%** |

**420 pedidos en 90 días = 140 al mes.** Coincide con la proyección que se venía usando.

### Móvil contra escritorio: la brecha se abre en el primer paso

| | Sesiones | Agregan al carrito | Llegan al pago | Compran | Conversión |
|---|---:|---:|---:|---:|---:|
| **Móvil** | 34.396 (92%) | 1.095 (**3,18%**) | 789 (72,1%) | 324 (41,1%) | **0,94%** |
| **Escritorio** | 3.152 (8%) | 259 (**8,22%**) | 211 (81,5%) | 94 (44,5%) | **2,98%** |

🟢 **El móvil convierte a carrito 2,6 veces peor que el escritorio, y es el 92% del tráfico.** Del paso al pago en adelante los dos se comportan casi igual: **todo el problema está en el primer paso.**

### Cuánto vale cerrar esa brecha 🟡

| Escenario | Compras en 90 días | Diferencia | Venta neta adicional |
|---|---:|---:|---:|
| Hoy | 324 | — | — |
| Cerrar la mitad de la brecha (3,18% → 5,7%) | 580 | **+85/mes** | **+$2.388.938/mes** |
| Igualar al escritorio (3,18% → 8,22%) | 836 | +171/mes | +$4.777.877/mes |

Es la oportunidad más grande de las cuatro auditorías. Y las tres causas probables ya están identificadas: el producto estrella agotado, las reseñas invisibles y la carga de la ficha en móvil.

---

## 3. La respuesta que faltaba: cuánta venta llega sin pagar por ella

Atribución de último clic de Shopify, 90 días:

| Fuente | Sesiones | Conversión | Pedidos | % del total |
|---|---:|---:|---:|---:|
| Instagram | 22.536 | 0,78% | ~176 | 42% |
| Directo | 4.388 | 1,93% | ~85 | 20% |
| Google orgánico | 2.535 | **3,27%** | ~83 | 20% |
| Facebook | 6.059 | 0,52% | ~32 | 8% |
| Meta Ads (etiquetado) | 756 | 2,51% | ~19 | 5% |
| Klaviyo | 326 | **5,21%** | ~17 | 4% |
| **Suman** | | | **~411** | 98% (reales: 420) |

🟢 **Como mínimo el 40% de los pedidos llega por canales que nadie está pagando** (Google orgánico 20% + directo 20%). Sumando Instagram orgánico, la cifra es bastante mayor.

### Y aquí se cierra el problema de atribución

| | Compras en 90 días |
|---|---:|
| Meta se atribuye (105/mes × 3) | 315 |
| Shopify ve de Meta Ads etiquetado | ~50 |
| Shopify ve de **todo** lo social (Instagram + Facebook + Meta Ads) | ~226 |

**Meta reclama 1,39 veces lo que Shopify le reconoce incluso contando todo el tráfico social.** Ese 1,39 es del mismo orden que el 1,75 de inflación del píxel que se detectó en la auditoría de Meta. Las dos mediciones apuntan a lo mismo.

⚠️ Nota: solo 756 sesiones llegan etiquetadas como Meta Ads contra 22.536 de Instagram. **El etiquetado de campañas está roto**, así que el tráfico pagado se está contando como orgánico.

---

## 4. Lo que está apagado y ya tiene demanda

Tres arreglos que no cuestan nada y tienen tráfico esperando:

| Qué | Evidencia | Estado |
|---|---|---|
| **Los packs están en borrador** | 6 productos "Pack" con **más de 9.000 vistas combinadas y cero ventas**. Pack Naturaleza Chilena 4.476 vistas, Pack Coleccionista 2.195, Pack Tarde de Naturaleza 530. | No se pueden comprar |
| **El widget de reseñas nunca se instaló** | 227 reseñas (222 de producto). En Configuraciones → Widgets, el "Widget de reseñas" figura como **"Instalar"**: nunca se agregó a la plantilla. Solo están la insignia de estrellas y el formulario. | Invisible en la ficha |
| **Puzzle Aves agotado** | 8.558 vistas, el producto más vendido | Sin stock |

🟢 Sobre los packs: en `ofertas.html` se propuso crear una colección de packs. **Ya existen, solo están sin publicar.**

---

## 5. Los otros hallazgos de Shopify

**Búsquedas del sitio (209 en 90 días).** Lo más buscado está en catálogo: puzzle (16), pin (13), naipes (11), hongos (11), calcetines (10), postales (10). **Cerca del 15% no arroja resultados**, y ahí hay demanda sin cubrir: tazas y vajilla, manta, memorice, reloj, funda, y especies sin producto (picaflor, bandurria, chincol).

**Checkouts abandonados.** 185 registrados por **$6.362.945**, todos "no recuperado" y sin automatización activa. Ojo con el matiz: 584 sesiones llegaron al pago sin completar, pero solo 185 quedan registradas, porque Shopify solo lo anota cuando la persona alcanzó a dejar su correo. En los casos revisados aparece la dirección completa pero sin intento de pago: **el quiebre está en el paso del pago**, que era la fricción reportada y no ubicada.

**Configuración del pago.** El **teléfono es obligatorio** en la dirección de envío (fricción evitable). Se permite comprar sin crear cuenta ✅. No hay pago exprés tipo Shop Pay porque no se usa Shopify Payments: van en paralelo Mercado Pago Tarjetas, Checkout Flow y Mercado Pago Checkout Pro.

**Envíos.** 16 zonas con tarifa plana por peso ($5.990 hasta 6kg, $20.990 de 6 a 10kg, $21.390 sobre 10kg). El envío gratis sobre $50.000 está bien configurado y se usó 157 veces sobre ~420 pedidos: **el 37% de los pedidos alcanza el umbral**.

⚠️ **Hay un código "egratis" activo, sin monto mínimo y válido para todos los países, usado 16 veces.** Contradice la política de los $50.000.

**Descuentos.** "SECRETO" se usó **389 veces sin ninguna restricción de cliente**: dejó de ser secreto y probablemente circula público. Le siguen BIENVENIDO10 (136), DESCUENTO65K (43), SECRETOAGOSTO (39).

**Apps.** 15 instaladas. Con costo visible: Judge.me ($15/mes) y DECO Labels ($9/mes); Selleasy cobra por uso. **Cuatro no aportan nada:** Instafeed (instalada hace 4 años, sin actividad), Tarificador (sin extensiones activas), AMP Bundles (instalada hace una semana, duplica la app nativa que ya existe desde 2024) y Ezy WhatsApp (duplica a CK WhatsApp, que sí funciona).

**Velocidad.** LCP 1.501ms e INP 96ms, ambos "bueno". Móvil 23% más lento que escritorio (1.517ms contra 1.228ms). El INP empeoró 9%, consistente con la acumulación de scripts de 15 apps.

---

## 6. Klaviyo: el canal que mejor convierte y menos se usa

🟢 **El correo aporta el 11,8% de la venta** ($1.841.728 de $15.587.362 en 90 días), por encima del 9% que se venía manejando.

Y convierte mejor que cualquier otra fuente: **5,21%**, contra 3,27% de Google orgánico y 0,78% de Instagram. **Convierte 6,7 veces mejor que Instagram trayendo el 0,9% del tráfico.**

### La lista

9.836 perfiles totales: 5.810 activos, 3.939 suprimidos (2.845 bajas voluntarias, 882 suprimidos en una limpieza masiva del 6 de febrero de 2025, 191 rebotes).

La lista operativa es "Newsletter" con **5.439 miembros**, creciendo de forma sostenida: de 2.918 en agosto de 2025 a 5.437 hoy. **Neto de 12 meses: +4.146 suscriptores.**

Origen de las altas: Shopify/checkout 52%, pop-up móvil 25%, pop-up escritorio 7%, importación manual 15%. **Todo el crecimiento orgánico viene de dos pop-ups**; no hay formulario embebido en la web que aporte.

### Los flujos

| Flujo | Estado | Entradas (90d) | Ingreso (90d) |
|---|---|---:|---:|
| Bienvenida (cliente vs no cliente) | Activo | 1.317 | $468.002 |
| Carrito abandonado (Checkout Started) | Activo | ~814 | $246.971 |
| Página de producto abandonada | Activo | ~602 | $225.355 |
| Agradecimiento post-compra | Activo | 430 entraron / 170 recibieron | $28.490 |
| **Reposición de stock** | **Apagado** | 0 | $0 |
| **Reactivación (sunset)** | **Apagado** | 0 | $0 |

🟢 **Los flujos automáticos ya generan más que las campañas** (56% contra 44% del ingreso atribuido) con solo cuatro activos.

⚠️ **El flujo de reposición de stock está apagado.** Con el producto estrella agotado y el stock llegando el 15 de agosto, es una fuga directa: nadie recibe aviso cuando vuelve.

### Los dos arreglos concretos del correo

**1. El primer correo de bienvenida para quien nunca compró es una copia mal renombrada.** En el editor se llama literalmente *"Copy of Welcome Email #1: Existing Customers"*: le cambiaron el asunto pero no el contenido. Aun así es la rama que más convierte (2,5%), lo que sugiere que el descuento del asunto funciona a pesar del texto reciclado.

**2. El cuarto correo del carrito abandonado no convierte nada.** El primero genera $118.131 de los $246.971 del flujo completo; el cuarto genera $0.

### Los segmentos existen y no se usan

Hay 8 segmentos bien construidos, creados el 27 y 28 de julio: Universo Aves (4.227), Suscriptores sin Compra (2.613), **Comprador 1 vez · Dormido +180 días (2.175)**, Universo Cetáceos (1.009), Universo Hongos (930), y los de comprador reciente y en riesgo.

⚠️ **Ninguno se ha usado en ninguna campaña ni flujo.** Todos los envíos reales van a listas antiguas sin segmentar.

### La observación de Cote, matizada

Cote notó que los correos simples funcionaban mejor que los muy producidos. **Los datos no permiten confirmar esa causa**: de 20 campañas, 19 usan la misma plantilla de marca y solo una es estilo carta personal, enviada a 65 personas. La muestra es demasiado chica.

Pero **Cote sí detectó algo real, con otra explicación**: lo que separa a los ganadores de los perdedores es el tamaño y la calidad del segmento, no el diseño.

| Tipo de envío | Apertura | Ingreso por destinatario |
|---|---:|---:|
| Audiencia filtrada y chica (ej. "mail urgencia cyber", 802 destinatarios) | **58%** | **$111** |
| Envío masivo a toda la lista sin filtrar | 17-25% | $10-35 |

🟢 **No es "diseño contra texto plano": es "lista completa contra audiencia segmentada".** Y los segmentos para hacerlo ya están construidos.

### Entregabilidad y SMS

Dominio verificado ✅. Puntaje "Bueno". Apertura 54,4% (excelente), rebote 0,12% (excelente), spam 0%. **Clic 0,90%**, bajo el 1,2% recomendado. **Bajas 0,32%**, apenas sobre el límite de 0,30%.

La campaña "último día del padre" tuvo 1,5% de bajas pese al filtro automático de Klaviyo: hay fatiga real en la parte más activa de la lista, no solo en los dormidos.

**SMS nunca se configuró.**

### Los pop-ups

Dos activos, ambos con descuento "secreto" de $2.000: el de escritorio captura **7,8%** y el de móvil solo **2,3%**. Como el 92% del tráfico es móvil, esa diferencia importa: vale revisar diseño y momento de aparición del pop-up móvil.

---

## 7. El orden de las correcciones

**Gratis y con demanda ya esperando:**

| # | Qué | Dónde | Impacto |
|---|---|---|---|
| 1 | Publicar los packs que están en borrador | Shopify | +9.000 vistas que hoy rebotan |
| 2 | Instalar el widget de reseñas en la plantilla | Shopify | 227 reseñas invisibles |
| 3 | Activar el flujo de reposición de stock | Klaviyo | Crítico: el stock llega el 15 de agosto |
| 4 | Quitar el código "egratis" | Shopify | Rompe la regla de los $50.000 |
| 5 | Restringir o rotar el código "SECRETO" | Shopify | 389 usos sin restricción |
| 6 | Usar los 8 segmentos ya construidos | Klaviyo | $200.000-400.000/mes 🟡 |
| 7 | Reescribir el correo de bienvenida para no-clientes | Klaviyo | Hoy es una copia sin trabajar |
| 8 | Quitar el cuarto correo del carrito abandonado | Klaviyo | Convierte cero |
| 9 | Desinstalar las 4 apps que no aportan | Shopify | Menos scripts, móvil más rápido |
| 10 | Sacar el teléfono obligatorio del checkout | Shopify | Fricción evitable |

**Con la preventa y el stock (6 y 15 de agosto):**

| # | Qué |
|---|---|
| 11 | Reponer el Puzzle Aves: el 23% del tráfico deja de rebotar |
| 12 | Atacar el paso de sesión a carrito en móvil, que es donde está la plata |
| 13 | Activar el flujo de reactivación con los 2.175 dormidos |
| 14 | Arreglar el etiquetado de campañas para medir bien lo pagado |
