# Cyber 2026 — Captación y flujos automáticos

Preparado 23-sep-2026. Cyber: viernes 2 al viernes 9 de octubre de 2026. Meta CLP 20.000.000 netos. Descuento máximo 25%. Envío gratis sobre $40.000 durante el Cyber (normal $50.000). La Botella Térmica Aves no tiene stock: no se menciona en ningún texto. Sin WhatsApp ni SMS.

Todo el copy sigue la voz de Cote: frases cortas, un hecho concreto como primera línea, cero emojis en el cuerpo, casi sin exclamaciones, lo comercial va en la P.D. Rige el principio de `CLAUDE.md` ("La voz de Cote", sección "Cómo vende"): la marca le quita presión al lector en vez de ponérsela, la urgencia se explica como hecho — nunca como amenaza — y quedan prohibidos "última oportunidad", "quedan pocas unidades", "no te lo pierdas", "aprovecha", "solo por hoy" y las cuentas regresivas; aquí la urgencia se ancla en la fecha de término del Cyber (viernes 9), no en el stock. **Lo único que se retira, y solo por esta vez, es el compromiso de entrega de esa misma cita de Cote** ("los que no alcancen esta semana los recibirán apenas repongamos stock"): con el inventario actual faltan ~114 unidades de Puzzle Hongos, ~59 de Cetáceos y ~38 de Mariposas para cubrir la meta, varias láminas están en cero, y no hay confirmación de Felipe de que se repone antes del 2-oct. Ningún texto de este documento promete fecha de reposición ni asegura que todos van a recibir el suyo. Si Felipe confirma la reposición antes del Cyber, la frase original de Cote ("Nadie se queda sin puzzle, simplemente unos lo recibirán antes que otros") se puede usar tal cual.

---

## 1. Inventario de lo que existe hoy en Klaviyo (revisado 23-sep-2026)

### Flujos (Flows)

| Flujo | ID | Estado | Disparador |
|---|---|---|---|
| Welcome Series - Customer v. Non-Customer | `RP9cfA` | **Live** | Se agrega a la lista "Newsletter" |
| Abandoned Cart Reminder (Email) | `RqYWQL` | **Live** | Métrica "Started Checkout" (excluye a quienes están en la lista de checkout abandonado jul-2026) |
| Product Page - Abandoned Cart Reminder | `T3VFL9` | **Live** | Métrica (navegación abandonada / vio producto) |
| Agradecimiento a los clientes - Nuevos y recurrentes | `WYtbJJ` | Live | Métrica (compra) |
| Flujo de reposición de stock - Estándar | `XwkjxQ` | Live | Métrica (back in stock) |
| Sunset Unagagged | `TtmgVn` | Borrador | Se agrega a lista |

**Detalle del Welcome Series (`RP9cfA`):** separa clientes nuevos vs. existentes con un split. A los nuevos les corre un test A/B de 3 variantes del Email #1 ("Qué bueno verte por aquí" / "aquí está tu regalo"), luego espera 2 días → "Nuestra historia", espera 2 días más → "Lo que dicen de nosotros" (solo si ya compró).

**Detalle del Abandoned Cart (`RqYWQL`):** espera 15 min → Email #1 con test A/B ("Guardamos algo para ti 🌿" / "Un precio especial en tu primer pedido?") → espera 3 h → Email #2 "Aún guardamos tu selección" → espera 2 días → Email #3 "última oportunidad: aún está disponible" (⚠️ esta frase ya viola la regla de Cote de no usar "última oportunidad"; no se tocó porque está viva, queda anotado como pendiente fuera de este encargo) → espera 2 días → Email #4 "Tenemos algo para ti" con 10% + envío gratis.

No se tocó ningún flujo vivo. No se creó ningún flujo nuevo en estado distinto a borrador.

### Formularios / pop-ups (Forms)

| Formulario | ID | Estado |
|---|---|---|
| PopUp (Celular) Oferta Entrada | `TcYLXB` | **Live**, con test A/B |
| PopUp A/B (Escritorio) Oferta Entrada | `SQjZs4` | **Live**, con test A/B |
| Reposición de stock Multi-paso | `YkXUcv` | Live |
| descuento secreto newsletter instagram | `QT5Ggt` | Borrador |
| PopUp A/B (Escritorio) sin promoción | `SmdTaT` | Borrador |
| PopUp (Celular) sin descuento | `W3xqB4` | Borrador |
| PopUp A/B (Escritorio) | `XQ4WJJ` | Borrador |
| PopUp (Celular) | `Su4jTz` | Borrador |

Los dos pop-ups vivos (`TcYLXB`, `SQjZs4`) capturan correo a cambio de un descuento de entrada (variantes de código probadas: SECRETO, 37HOY, BIENVENIDO10, EGRATIS). Son los que están mostrándose hoy en la tienda.

### Listas (Lists) — parcial, hay más paginadas

`suscritos`, `Newsletter` (dispara el Welcome Series), `compraron hace 5 dias`, `compraron platos azules`, `Pop Up`, `Back in stock`, `Suscriptores instagram`, `Han comprado una vez`, lista de checkout abandonado jul-2026, `clientes shopify (historico)`.

### Segmentos (Segments) — parcial, hay más paginados

Todos de reactivación/engagement (90 días, 60 días, dormidos, comprador 1 vez en riesgo, más activos 30 días, etc.). Ninguno relacionado con el Cyber existía antes de este trabajo.

---

## 2. Correos "modo Cyber" (mismo ángulo, con la urgencia de las fechas)

Estos son textos listos para pegar en las plantillas de los flujos vivos, durante la ventana del Cyber. **No se aplicaron solos**, porque tocar contenido de un flujo vivo está fuera de lo que se pidió (ver sección "Requiere Mateo").

### 2.1 Correo de bienvenida (Welcome Series, Email #1)

Reemplaza el "aquí está tu regalo" solo del 2 al 9 de octubre. Como el descuento del Cyber (25%) ya es el máximo permitido, no se ofrece un código de bienvenida adicional encima: se regala el hecho de haber llegado justo en el Cyber.

> **Asunto:** Llegaste justo para el Cyber
> **Preheader:** Del 2 al 9 de octubre, toda la tienda al 25%
>
> Hola,
>
> Llegaste en plena semana del Cyber.
>
> Desde el viernes 2 hasta el viernes 9 de octubre, toda la tienda tiene el descuento más grande del año: 25% en cada pieza.
>
> No necesitas ningún código. El precio ya sale rebajado.
>
> Ver la tienda →
>
> Un abrazo,
> Cote
>
> P.D. Envío gratis sobre $40.000 durante esa semana.

### 2.2 Carrito abandonado — Email #1 (15 minutos después)

Reemplaza "Guardamos algo para ti 🌿" solo del 2 al 9 de octubre.

> **Asunto:** Tu selección sigue esperando
> **Preheader:** Con el 25% del Cyber, hasta el viernes 9
>
> Hola,
>
> Tu selección quedó guardada.
>
> Estamos en plena semana del Cyber: 25% en toda la tienda, del 2 al 9 de octubre.
>
> Tu carrito ya tiene ese precio aplicado. Solo falta que termines.
>
> Completar mi pedido →
>
> Un abrazo,
> Cote
>
> P.D. Envío gratis sobre $40.000 hasta el viernes 9.

### 2.3 Carrito abandonado — último correo (cierre del Cyber)

Reemplaza "Tenemos algo para ti 🌿" (10% + envío gratis) solo del 2 al 9 de octubre. No se suma un 10% extra sobre el 25%: la regla del Cyber es que ningún descuento se acumula salvo el de aliados.

> **Asunto:** El Cyber se cierra el viernes
> **Preheader:** Después del 9 de octubre vuelve el precio normal
>
> Hola,
>
> El Cyber llega a su último día el viernes 9 de octubre.
>
> Tu selección sigue con el 25% aplicado. Después de esa fecha, vuelve al precio de siempre.
>
> Completar mi pedido →
>
> Un abrazo,
> Cote
>
> P.D. Envío gratis sobre $40.000 hasta el viernes 9.

Nota aparte: la memoria del proyecto menciona un código de 15% solo para carritos abandonados, válido hasta el domingo 11 de octubre, como cola post-Cyber. Ese correo es un flujo/campaña distinto, posterior al Cyber, y no estaba dentro de este encargo — queda anotado para no perderlo (ver cierre).

### 2.4 Pop-up de la tienda (entrada, `TcYLXB` / `SQjZs4`)

Durante el Cyber no se puede ofrecer un descuento de entrada adicional encima del 25% general. La versión "modo Cyber" del pop-up anuncia el Cyber en vez de regatear un código:

> **Encabezado:** Estás en plena semana del Cyber
> **Cuerpo:** Del 2 al 9 de octubre, toda la tienda tiene 25% de descuento. Ya viene aplicado, sin código.
> **Campo:** solo correo electrónico
> **Botón:** Ver la tienda

---

## 3. Lista de espera "Avísame cuando empiece el Cyber"

Creada en Klaviyo, en borrador, lista para que Mateo la revise y active cuando quiera.

### Qué pide el formulario

Un solo campo: **correo electrónico**. Nada de nombre, teléfono ni otra pregunta — cuanto menos pida, más gente se anota a tiempo.

### Texto del pop-up

> **Encabezado:** Avísame cuando empiece el Cyber
> **Cuerpo:** El viernes 2 de octubre baja el precio de toda la tienda. Te escribo apenas empiece, antes que a los demás.
> **Placeholder del campo:** tu@correo.com
> **Botón:** Avísame
> **Paso de confirmación (tras enviar):** "Listo — Guardé tu correo. El viernes 2 de octubre te escribo primero." con botón "Cerrar".

Se muestra a los 5 segundos o al intento de salida (exit intent), lo que ocurra primero.

**Creado en Klaviyo:** formulario `UPbCtr` ("Avísame cuando empiece el Cyber"), estado **borrador**, 2 pasos (formulario + confirmación), sin publicar.

### Correo de confirmación

> **Asunto:** Ya guardé tu correo
> **Preheader:** El viernes 2 de octubre te escribo primero
>
> Hola,
>
> Guardé tu correo.
>
> El viernes 2 de octubre, antes de avisarle a todos los demás, te escribo a ti.
>
> No hay nada más que hacer. Solo espera el correo esa mañana.
>
> Un abrazo,
> Cote
>
> P.D. El Cyber dura del 2 al 9 de octubre, así que vas a tener toda la semana para mirar con calma.

**Creado en Klaviyo:**
- Plantilla de correo `Ybznyn` ("Cyber 2026 - Confirmación lista de espera"), con el texto de arriba en HTML y texto plano, verde de marca `#3B5751`, con link de baja incluido.
- Flujo `UebzZj` ("Cyber 2026 - Confirmación lista de espera"), estado **borrador**, disparado por "se agrega a la lista" → envía la plantilla anterior. La acción de envío también está en estado borrador dentro del flujo. No se activó.

### Lista y segmento

- Lista `SSjJjX` — "Cyber 2026 — Avísame primero" (single opt-in). Es donde cae cada correo que se anota, y es el `list_id` que usa el botón del pop-up.
- Segmento `RVnUn8` — "Cyber 2026 — Lista de espera (avisar primero)" — todos los miembros de esa lista. Este es el segmento para avisarles primero el 2 de octubre: se les manda el correo/campaña de lanzamiento del Cyber unas horas antes (o esa misma mañana temprano) que al resto de la base.

---

## 4. Línea de tiempo única de pop-ups (un solo pop-up activo por tramo) — REQUIERE MATEO

Hoy hay tres pop-ups pensados por separado (los dos de oferta de entrada ya vivos, `TcYLXB`/`SQjZs4`, más el de lista de espera `UPbCtr` de este documento) y tres códigos de esos pop-ups (EGRATIS, SECRETO, BIENVENIDO10) que `configuracion-tienda.md` marca como riesgo de sumarse al 25% del Cyber. Esta es la secuencia única para que nunca haya más de un pop-up activo a la vez:

| Tramo | Pop-up activo | Pop-ups pausados | Códigos EGRATIS / SECRETO / BIENVENIDO10 |
|---|---|---|---|
| **23-sep al 1-oct** (hoy) | `UPbCtr` "Avísame cuando empiece el Cyber" — REQUIERE MATEO publicarlo | `TcYLXB` y `SQjZs4` (oferta de entrada) — REQUIERE MATEO pausarlos | Siguen activos como código (no se tocan en este tramo), pero dejan de ofrecerse en pantalla porque el pop-up que los mostraba está pausado |
| **2-oct al 9-oct** (Cyber) | Versión "modo Cyber" del pop-up de entrada (texto de la sección 2.4, sin código, solo anuncia el 25%) — REQUIERE MATEO editar `TcYLXB`/`SQjZs4` con ese texto y reactivarlos | `UPbCtr` (ya cumplió su función; el aviso del 2-oct ya salió por correo al segmento `RVnUn8`) | **Pausados** — REQUIERE MATEO desactivarlos en Shopify Admin → Descuentos (mismo paso "pendiente decisión" del punto 4 de `configuracion-tienda.md`, 08:00 del 2-oct), porque pueden sumarse al 25% |
| **10-oct en adelante** (post-Cyber) | `TcYLXB` y `SQjZs4` vuelven a su copy y código original de oferta de entrada — REQUIERE MATEO revertir el texto | `UPbCtr` (queda apagado; se puede reusar en la próxima fecha con lista de espera) | Reactivados — mismo paso de las 22:15 del 9-oct en `configuracion-tienda.md` ("Reactivar lo que se haya pausado en la sección pendiente decisión") |

---

## 5. Barra de aviso pre-Cyber (para la tienda) — REQUIERE MATEO

El tema publicado de Shopify no se puede editar por MCP, así que esto queda como instrucción exacta para pegar en el editor de temas.

- **Texto exacto:** `El Cyber Pedraza empieza el viernes 2 de octubre. Avísame antes →`
- **A dónde enlaza:** a la portada de la tienda, con parámetros de seguimiento: `/?utm_source=barra&utm_medium=preaviso&utm_campaign=cyber2026`. Ahí es donde debe mostrarse el pop-up "Avísame cuando empiece el Cyber" (ver sección 3) una vez que Mateo lo publique.
- **Desde cuándo:** hoy, miércoles 23 de septiembre de 2026.
- **Hasta cuándo:** jueves 1 de octubre de 2026, 23:59 (el Cyber arranca el viernes 2 y a partir de ahí la barra debería cambiar de mensaje — ese texto de "Cyber en curso" no estaba pedido en este encargo, queda como pendiente natural para la semana del Cyber).

**Paso exacto:** Personalizar tema → sección de barra de anuncio (announcement bar) → pegar el texto de arriba → configurar el link → programar visibilidad del 23-sep al 1-oct si el tema lo permite, o poner un recordatorio para desactivarla a mano el 1 de octubre en la noche.

---

## Qué queda hecho, qué queda en borrador y qué necesita a Mateo

1. **Hecho y en Klaviyo, sin activar:** lista `SSjJjX`, segmento `RVnUn8`, plantilla de correo `Ybznyn`, flujo `UebzZj` (borrador) y formulario `UPbCtr` (borrador, 2 pasos) para la lista de espera del Cyber.
2. **Ningún flujo ni pop-up vivo fue tocado:** Welcome Series, Abandoned Cart, y los pop-ups de oferta de entrada (`TcYLXB`, `SQjZs4`) siguen exactamente como estaban.
3. **REQUIERE MATEO — seguir la línea de tiempo única de pop-ups (sección 4):** un solo pop-up activo por tramo — `UPbCtr` ahora, el pop-up de entrada en "modo Cyber" (sin código) del 2 al 9-oct, y el pop-up de entrada original desde el 10-oct — pausando/reactivando en cada cambio los códigos EGRATIS/SECRETO/BIENVENIDO10 según la tabla.
4. **REQUIERE MATEO — pegar los correos "modo Cyber" (sección 2):** en las plantillas del Welcome Series y del Abandoned Cart, solo durante el 2–9 de octubre, y revertir al texto original después.
5. **REQUIERE MATEO — barra de anuncio pre-Cyber** en el tema de Shopify (sección 5): texto, link y fechas exactas ya definidos.
7. **REQUIERE MATEO — enviar el aviso del 2 de octubre primero al segmento `RVnUn8`**, y horas después (o al día siguiente) a la base general.
8. **Pendiente anotado, fuera de este encargo:** el correo #3 del Abandoned Cart vivo usa "última oportunidad", que rompe la regla de Cote de no amenazar con urgencia — se deja anotado, no se tocó por estar vivo.
9. **Pendiente anotado, fuera de este encargo:** el código de 15% solo para carritos abandonados post-Cyber (hasta el domingo 11 de octubre) que menciona la memoria del proyecto no se construyó aquí; es un flujo/campaña aparte para después del 9 de octubre.
