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

## Contexto comercial clave (confirmado por el operador, jul-2026)

- Facturación actual de la tienda: **~USD 5.000/mes**. Meta: **USD 10.000/mes**. Esta es la métrica norte del plan.
- Objetivo #1: escalar ventas de la tienda online (Shopify). Mercado: Chile ahora, Amazon EEUU pronto (anexo "Rampa EEUU").
- El detalle del acuerdo comercial operador-cliente (fijo + variable) NO se incluye en ningún entregable.

## Reglas duras del entregable

- Nunca inventar datos ni estadísticas: cada dato con fuente (URL) o marcado 🟡 VERIFICAR / 🟡 SUPUESTO.
- Sitio: HTML autocontenido por archivo, cero dependencias externas, cero CDNs, todo CSS/JS inline. Sistema de diseño compartido vía variables CSS. localStorage con prefijo `pedraza-plan:`.
- Cada documento operativo trae plantillas listas para copiar y pegar (copy real, sin `[placeholder]`).
- Commits descriptivos al final de cada fase; push a la rama que indique el entorno.
