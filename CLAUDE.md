# Memoria del proyecto — Plan Pedraza Ilustración

Reglas permanentes para TODOS los entregables de este repo (documentos, páginas HTML, README, plantillas). Aplican a cualquier sesión y a cualquier subagente.

## Reglas de comunicación (obligatorias)

1. **Visual primero.** Usar gráficos y elementos visuales donde sea posible: la gran mayoría de las personas entiende mejor una idea viéndola que leyéndola.
   - En páginas HTML: gráficos con SVG/CSS inline (sin librerías externas), diagramas de embudo, barras de progreso, líneas de tiempo, calendarios visuales, tarjetas comparativas, íconos.
   - En documentos Markdown: diagramas Mermaid (GitHub los renderiza), tablas simples y visuales, emojis como señalética (🟢🟡🔴).
   - Regla práctica: si una idea tiene pasos, comparaciones, fechas o números, se muestra con un gráfico o diagrama, no solo con texto.

2. **Lenguaje simple, cero tecnicismos.** Todo debe poder entenderse sin conocimientos previos de marketing ni de e-commerce.
   - Si un término técnico es inevitable, se explica al lado en palabras simples la primera vez. Ejemplos: "ticket promedio (lo que gasta una persona por compra)", "CTA (la invitación a hacer algo, como 'compra aquí')", "alcance (cuánta gente vio la publicación)".
   - Preferir siempre la palabra simple: "guardados" en vez de "saves", "compartidos" en vez de "sends" (aclarando que Instagram lo mide como envíos por DM), "publicar" en vez de "postear" cuando se pueda.
   - Frases cortas. Una idea por frase.
   - **IMPORTANTE: esta regla no se menciona nunca dentro de los entregables** (nada de "explicado simple para que cualquiera entienda" ni similares). Simplemente se escribe así.

3. **Diseño mobile-first.** Todo entregable visual (especialmente las páginas HTML del sitio) se diseña primero para el celular y debe verse impecable en pantalla móvil: tipografía legible sin zoom, botones y checkboxes cómodos para el dedo (mínimo ~44px de área táctil), tablas y gráficos que se adaptan o permiten scroll horizontal contenido, menú de navegación usable con una mano. El escritorio es la mejora progresiva, no al revés. Probar mentalmente cada componente en un ancho de ~375px antes de darlo por bueno.

4. **Voz: español neutro con expresiones chilenas puntuales.**
   - PROHIBIDO el voseo rioplatense: nada de "tenés/querés/tocá/comentá/mandale". Usar tuteo estándar: "tienes/quieres/toca aquí/comenta".
   - Expresiones chilenas con moderación y solo donde sumen cercanía (ej. "al tiro", "filete"). Marca familiar, educativa y de conservación; cercana, sin solemnidad.

5. **Entregables en HTML compartibles por link.** Todo entregable destinado al cliente se produce como página HTML autocontenida (servible por GitHub Pages), para poder compartirlo con un link y que lo revisen desde cualquier dispositivo. Los archivos Markdown (docs/) son material de trabajo interno; su contenido final vive en las páginas HTML.

6. **Todo lo copiable, con copia en un clic.** Cualquier texto pensado para copiar y pegar (bios, guiones, plantillas de DM, captions, mensajes) va SIEMPRE dentro de un bloque `.copyblock` con botón "Copiar": usa `navigator.clipboard` con fallback a `document.execCommand('copy')`, feedback visual "✓ ¡Copiado!" al hacer clic, y delegación de eventos (un solo listener por página). En móvil el botón debe ser cómodo para el dedo.

## Contexto comercial clave (confirmado por el operador, jul-2026)

- Facturación actual de la tienda: **~USD 5.000/mes**. Meta: **USD 10.000/mes**. Esta es la métrica norte del plan.
- Ticket promedio (AOV): referencia del operador **~$60.000 CLP** (dato de memoria, puede ser menor hoy; 🟡 confirmar en Shopify).
- Seguidores de @pedraza_ilustracion: **62.500** (confirmado por el operador, jul-2026).
- **"Cote" = María José Pedraza.** Ella es quien responde los mensajes/DMs hoy (confirmado por el operador).
- Objetivo #1: escalar ventas de la tienda online (Shopify). Mercado: Chile ahora, Amazon EEUU pronto (anexo "Rampa EEUU").
- El detalle del acuerdo comercial operador-cliente (fijo + variable) NO se incluye en ningún entregable.

## Reglas de contenido del operador (aplicar en toda la estrategia)

- **Verde de marca:** el sitio web del cliente usa el verde naturaleza `#3B5751` — debe estar presente en el sistema de diseño del sitio del plan.
- **Métrica reina por formato:** para Reels/carruseles/posts del feed = **compartidos**; para historias = **interacciones ÷ visualizaciones**.
- **Filtro 5-50:** un niño de 5 años debería entender de qué trata la pieza, y 50 de 100 personas aleatorias deberían entender al menos el 50% inicial.
- **Contenido "conciencia 1" para alcance:** piezas sobre temas universales y cotidianos (dormir, tomar agua, mentalidad) para gente que aún no piensa en comprar y solo admira la naturaleza. Referencia del operador: @mattelsa (carruseles de 30-58 mil me gusta, capturas jul-2026).
- El checkout nativo de Instagram nunca estuvo disponible fuera de EEUU: en Chile la compra SIEMPRE se cerró fuera de la app. No presentar su eliminación como un cambio que afecta a la marca.

## Reglas duras del entregable

- Nunca inventar datos ni estadísticas: cada dato con fuente (URL) o marcado 🟡 VERIFICAR / 🟡 SUPUESTO.
- Sitio: HTML autocontenido por archivo, cero dependencias externas, cero CDNs, todo CSS/JS inline. Sistema de diseño compartido vía variables CSS. localStorage con prefijo `pedraza-plan:`.
- Cada documento operativo trae plantillas listas para copiar y pegar (copy real, sin `[placeholder]`).
- Commits descriptivos al final de cada fase; push a la rama que indique el entorno.
