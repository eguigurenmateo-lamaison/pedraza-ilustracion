# Sistema de diseño — Sitio del plan Pedraza Ilustración

Especificación única para las 6 páginas del sitio (`index.html`, `kit-arranque.html`, `guion-reels.html`, `sop-dm.html`, `recursos.html`, `tablero.html`). La construyen 6 desarrolladores en paralelo, cada uno en su propio archivo — por eso **todos los bloques de código de este documento se copian tal cual, sin modificar**. Solo cambia el contenido específico de cada página (texto, tablas, gráficos), nunca la estructura de clases, variables ni scripts base.

Este documento es material de trabajo interno (vive en `docs/`, no se comparte con el cliente). El resultado final — las 6 páginas HTML — sí es el entregable compartible.

## Índice

1. Identidad visual (paleta, tipografía, variables CSS)
2. Bloque CSS canónico completo
3. Markup canónico de navegación
4. JS canónico del botón Copiar
5. Contrato de localStorage y checklist
6. Parser CSV del tablero
7. Reglas de página y plantilla de esqueleto HTML
8. Checklist de calidad por página

---

## 1. Identidad visual

### Paleta

La marca ilustra flora y fauna nativa de Chile en acuarela — el sitio debe sentirse como una guía de campo bien editada, no como un dashboard de software genérico: fondo tipo papel, tinta oscura para el texto, un solo acento con carácter.

**Acento elegido: rojo copihue** (`#b0223f`), no verde bosque.

Justificación (2 líneas): el copihue es la flor nacional de Chile y ya es rojo intenso — le da al acento una identidad chilena inequívoca y reconocible, en vez de un "verde naturaleza" genérico que comparte cualquier marca de conservación. Además, al ser cálido, resalta con fuerza sobre el verde que ya domina las ilustraciones de flora del catálogo (contraste, no competencia).

El verde bosque no se descarta: se usa como color de apoyo semántico para "éxito", donde además refuerza el eje de conservación de la marca.

| Token | Valor | Uso |
|---|---|---|
| `--ink` | `#1c2420` | Texto principal, fondo del nav |
| `--ink-soft` | `#4c5850` | Texto secundario, etiquetas |
| `--ink-faint` | `#7c887f` | Texto terciario, marcas de tiempo |
| `--paper` | `#faf6ee` | Fondo de página (papel cálido, no blanco puro) |
| `--surface` | `#fffefb` | Fondo de tarjetas y bloques |
| `--line` | `#e6ded0` | Bordes suaves |
| `--line-strong` | `#d6c9b0` | Bordes de énfasis, separadores de sección |
| `--accent` | `#b0223f` | Rojo copihue — acento principal, CTA, links activos |
| `--accent-dark` | `#7c1830` | Hover/gradiente del acento |
| `--accent-soft` | `#f8dfe4` | Fondos tenues de acento (pills, badges) |
| `--success` | `#2f6b4a` | Verde bosque — éxito, cifras positivas |
| `--success-soft` | `#dcece1` | Fondo tenue de éxito |
| `--warn` | `#a8720a` | Alerta 🟡 (mismo código de color que el resto del proyecto) |
| `--warn-soft` | `#f8ecd2` | Fondo tenue de alerta |
| `--danger` | `#ae3d17` | Peligro / error — terracota, deliberadamente distinto del rojo copihue para no confundirse con el acento |
| `--danger-soft` | `#f7ddd0` | Fondo tenue de peligro |
| `--info` | `#35606c` | Información neutra |
| `--info-soft` | `#dde7ea` | Fondo tenue de información |

Solo 5 familias de color en total (tinta, papel, acento, y 4 tonos semánticos de bajo protagonismo que casi nunca cubren superficies grandes, solo bordes/iconos/pills). Mantiene el sitio con aspecto de sistema diseñado, no de paleta improvisada por 6 personas distintas.

### Tipografía

System stack, cero fuentes web. Los títulos usan la pila serif del sistema (Georgia y equivalentes) para dar un aire editorial de "guía de campo" — el mismo espíritu que las fichas de especies del catálogo (nombre común + nombre científico); el cuerpo de texto usa la pila sans-serif del sistema, más legible en bloques largos y en pantallas chicas.

```css
--font-sans: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
--font-serif: Georgia, "Iowan Old Style", "Times New Roman", serif;
--font-mono: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, monospace;
```

Tamaños fluidos con `clamp()` — se ven bien desde 375px sin romper en pantallas grandes (ver variables `--fs-*` en el bloque CSS).

### Radios, sombras y espaciado

Radios generosos (16px en tarjetas) para un aire orgánico, coherente con acuarela — nada de esquinas duras de dashboard corporativo. Sombras muy suaves, casi imperceptibles, solo para separar superficies. Escala de espaciado en `rem` de 8 pasos.

---

## 2. Bloque CSS canónico completo

Este bloque completo va dentro de un único `<style>...</style>` en el `<head>` de cada una de las 6 páginas. Se copia **entero y sin editar** — el contenido de cada página se ajusta con las clases ya definidas aquí, nunca escribiendo CSS nuevo suelto en cada archivo (si una página necesita algo muy puntual, un `style=""` inline puntual es aceptable; no crear una segunda hoja de estilos).

```css
/* ==========================================================================
   Sistema de diseño — Plan Pedraza Ilustración
   Bloque único y canónico. No editar por página: solo usar estas clases.
   ========================================================================== */

:root {
  color-scheme: light;

  /* --- tinta y superficies --- */
  --ink: #1c2420;
  --ink-soft: #4c5850;
  --ink-faint: #7c887f;
  --paper: #faf6ee;
  --surface: #fffefb;
  --line: #e6ded0;
  --line-strong: #d6c9b0;

  /* --- acento: rojo copihue --- */
  --accent: #b0223f;
  --accent-dark: #7c1830;
  --accent-soft: #f8dfe4;

  /* --- apoyo semántico --- */
  --success: #2f6b4a;
  --success-soft: #dcece1;
  --warn: #a8720a;
  --warn-soft: #f8ecd2;
  --danger: #ae3d17;
  --danger-soft: #f7ddd0;
  --info: #35606c;
  --info-soft: #dde7ea;

  /* --- forma --- */
  --radius: 16px;
  --radius-sm: 10px;
  --radius-full: 999px;
  --shadow-sm: 0 1px 3px rgba(28, 36, 32, .1);
  --shadow: 0 6px 20px rgba(28, 36, 32, .12);

  /* --- espaciado --- */
  --space-1: .25rem;
  --space-2: .5rem;
  --space-3: .75rem;
  --space-4: 1rem;
  --space-5: 1.5rem;
  --space-6: 2rem;
  --space-7: 3rem;
  --space-8: 4rem;

  /* --- tipografía --- */
  --font-sans: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  --font-serif: Georgia, "Iowan Old Style", "Times New Roman", serif;
  --font-mono: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, monospace;
  --fs-sm: clamp(.82rem, .78rem + .2vw, .9rem);
  --fs-base: clamp(1rem, .95rem + .25vw, 1.0625rem);
  --fs-lg: clamp(1.1rem, 1.02rem + .4vw, 1.25rem);
  --fs-h3: clamp(1.15rem, 1.05rem + .5vw, 1.35rem);
  --fs-h2: clamp(1.35rem, 1.15rem + 1vw, 1.75rem);
  --fs-h1: clamp(1.75rem, 1.4rem + 2vw, 2.75rem);

  /* --- área táctil mínima (regla mobile-first del proyecto) --- */
  --tap: 44px;
}

/* ===== 1. Reset mínimo ===== */
*, *::before, *::after { box-sizing: border-box; }
html { -webkit-text-size-adjust: 100%; scroll-behavior: smooth; }
body { margin: 0; }
img, svg { max-width: 100%; display: block; }
h1, h2, h3, h4, p, ul, ol, dl, figure { margin: 0 0 var(--space-4); }
ul, ol { padding-left: 1.2em; }
a { color: inherit; }
button { font: inherit; }
table { border-collapse: collapse; width: 100%; }

/* ===== 2. Tipografía base ===== */
body {
  font-family: var(--font-sans);
  font-size: var(--fs-base);
  line-height: 1.55;
  color: var(--ink);
  background: var(--paper);
  -webkit-font-smoothing: antialiased;
}
h1, h2, h3 { font-family: var(--font-serif); line-height: 1.2; color: var(--ink); }
h1 { font-size: var(--fs-h1); }
h2 { font-size: var(--fs-h2); }
h3 { font-size: var(--fs-h3); }
p { max-width: 68ch; }
strong { color: var(--ink); }
:focus-visible { outline: 3px solid var(--accent); outline-offset: 2px; }

/* ===== 3. Layout ===== */
.wrap { max-width: 960px; margin: 0 auto; padding: 0 var(--space-4) var(--space-8); }

/* ===== 4. Nav superior (.docnav) ===== */
.docnav {
  position: sticky;
  top: 0;
  z-index: 50;
  background: var(--ink);
  border-bottom: 1px solid rgba(255, 255, 255, .08);
}
.docnav__inner {
  display: flex;
  overflow-x: auto;
  -webkit-overflow-scrolling: touch;
  scrollbar-width: thin;
  max-width: 960px;
  margin: 0 auto;
  padding: 0 var(--space-2);
}
.docnav__link {
  flex: 0 0 auto;
  display: flex;
  align-items: center;
  min-height: var(--tap);
  padding: 0 var(--space-3);
  color: #eae6dd;
  text-decoration: none;
  font-size: var(--fs-sm);
  font-weight: 600;
  white-space: nowrap;
  border-bottom: 3px solid transparent;
}
.docnav__link:hover { color: #fff; }
.docnav__link.active {
  color: #fff;
  border-bottom-color: var(--accent);
}

/* ===== 5. Hero ===== */
.hero {
  padding: var(--space-7) var(--space-4);
  background: linear-gradient(135deg, var(--accent) 0%, var(--accent-dark) 100%);
  color: #fff;
}
.hero__inner { max-width: 960px; margin: 0 auto; }
.hero h1 { color: #fff; margin-bottom: var(--space-3); }
.hero p { color: rgba(255, 255, 255, .92); font-size: var(--fs-lg); max-width: 60ch; margin: 0; }

/* ===== 6. Secciones numeradas (.sec) ===== */
main { counter-reset: sec; }
.sec { counter-increment: sec; margin-top: var(--space-7); }
.sec:first-of-type { margin-top: var(--space-6); }
.sec > h2 {
  display: flex;
  align-items: baseline;
  gap: var(--space-3);
  padding-bottom: var(--space-2);
  border-bottom: 2px solid var(--line-strong);
}
.sec > h2::before {
  content: counter(sec);
  flex: 0 0 auto;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 1.9em;
  height: 1.9em;
  border-radius: var(--radius-full);
  background: var(--accent);
  color: #fff;
  font-family: var(--font-sans);
  font-size: .55em;
  font-weight: 700;
}

/* ===== 7. Callouts ===== */
.callout {
  display: flex;
  gap: var(--space-3);
  padding: var(--space-4);
  border-radius: var(--radius-sm);
  border: 1px solid var(--line);
  background: var(--surface);
  margin: var(--space-4) 0;
}
.callout::before { flex: 0 0 auto; font-size: 1.3em; line-height: 1; }
.callout p:last-child { margin-bottom: 0; }
.callout--info { border-color: var(--info); background: var(--info-soft); }
.callout--info::before { content: "💡"; }
.callout--success { border-color: var(--success); background: var(--success-soft); }
.callout--success::before { content: "✅"; }
.callout--warn { border-color: var(--warn); background: var(--warn-soft); }
.callout--warn::before { content: "🟡"; }
.callout--danger { border-color: var(--danger); background: var(--danger-soft); }
.callout--danger::before { content: "🔴"; }

/* ===== 8. Bloque copiable (.copyblock) ===== */
.copyblock {
  position: relative;
  margin: var(--space-4) 0;
  padding: var(--space-8) var(--space-4) var(--space-4);
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: var(--radius);
  box-shadow: var(--shadow-sm);
}
.copyblock__text {
  font-family: var(--font-mono);
  font-size: var(--fs-sm);
  white-space: pre-wrap;
  word-break: break-word;
  color: var(--ink);
}
.copyblock__btn {
  position: absolute;
  top: var(--space-3);
  right: var(--space-3);
  min-height: var(--tap);
  padding: 0 var(--space-4);
  border: none;
  border-radius: var(--radius-sm);
  background: var(--accent);
  color: #fff;
  font-size: var(--fs-sm);
  font-weight: 700;
  cursor: pointer;
}
.copyblock__btn:hover { background: var(--accent-dark); }
.copyblock__btn.is-copied { background: var(--success); }

/* ===== 9. KPIs (.kpi) ===== */
.kpi-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: var(--space-3);
  margin: var(--space-4) 0;
}
.kpi {
  padding: var(--space-4);
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: var(--radius);
  box-shadow: var(--shadow-sm);
}
.kpi__label { display: block; font-size: var(--fs-sm); color: var(--ink-soft); margin-bottom: var(--space-2); }
.kpi__value { display: block; font-family: var(--font-serif); font-size: clamp(1.5rem, 1.3rem + 1vw, 2.1rem); font-weight: 700; color: var(--ink); }
.kpi__delta { display: inline-block; margin-top: var(--space-2); font-size: var(--fs-sm); font-weight: 600; padding: 2px var(--space-2); border-radius: var(--radius-full); }
.kpi__delta--up { color: var(--success); background: var(--success-soft); }
.kpi__delta--down { color: var(--danger); background: var(--danger-soft); }

/* ===== 10. Tarjeta genérica (.card) ===== */
.card {
  padding: var(--space-4);
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: var(--radius);
  box-shadow: var(--shadow-sm);
  margin: var(--space-4) 0;
}
.card h3 { margin-top: 0; }

/* ===== 11. Tablas responsive ===== */
.table-wrap { overflow-x: auto; margin: var(--space-4) 0; border: 1px solid var(--line); border-radius: var(--radius-sm); }
.table-wrap table { min-width: 480px; }
.table-wrap th, .table-wrap td { padding: var(--space-3); text-align: left; border-bottom: 1px solid var(--line); font-size: var(--fs-sm); }
.table-wrap thead th { background: var(--ink); color: #fff; position: sticky; top: 0; }
.table-wrap tbody tr:last-child td { border-bottom: none; }
.table-wrap tbody tr:nth-child(even) { background: var(--paper); }

/* ===== 12. Barra de progreso (.progress) ===== */
.progress { margin: var(--space-4) 0; }
.progress__track { height: 14px; background: var(--line); border-radius: var(--radius-full); overflow: hidden; }
.progress__fill { height: 100%; background: var(--accent); border-radius: var(--radius-full); transition: width .3s ease; width: 0%; }
.progress__label { display: block; margin-top: var(--space-2); font-size: var(--fs-sm); color: var(--ink-soft); }

/* ===== 13. Checklist táctil (.checklist) ===== */
.checklist { list-style: none; padding-left: 0; margin: var(--space-4) 0; }
.checklist li { margin-bottom: var(--space-2); }
.checklist label {
  display: flex;
  align-items: flex-start;
  gap: var(--space-3);
  min-height: var(--tap);
  padding: var(--space-2) var(--space-3);
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: var(--radius-sm);
  cursor: pointer;
}
.checklist input[type="checkbox"] { width: 24px; height: 24px; flex: 0 0 auto; accent-color: var(--accent); margin-top: 2px; }
.checklist input[type="checkbox"]:checked + span { text-decoration: line-through; color: var(--ink-soft); }

/* ===== 14. Etiquetas (.pill) ===== */
.pill {
  display: inline-flex;
  align-items: center;
  padding: 2px var(--space-3);
  border-radius: var(--radius-full);
  font-size: var(--fs-sm);
  font-weight: 600;
  background: var(--accent-soft);
  color: var(--accent-dark);
}
.pill--success { background: var(--success-soft); color: var(--success); }
.pill--warn { background: var(--warn-soft); color: var(--warn); }
.pill--danger { background: var(--danger-soft); color: var(--danger); }
.pill--info { background: var(--info-soft); color: var(--info); }

/* ===== 15. Grillas responsive ===== */
.grid-2, .grid-3 { display: grid; gap: var(--space-4); margin: var(--space-4) 0; grid-template-columns: 1fr; }

/* ===== 16. Gráficos SVG/CSS hechos a mano ===== */
/* Barras horizontales */
.chart-bar-row { display: flex; align-items: center; gap: var(--space-3); margin-bottom: var(--space-2); }
.chart-bar-row__label { flex: 0 0 9rem; font-size: var(--fs-sm); color: var(--ink-soft); }
.chart-bar-row__track { flex: 1 1 auto; height: 20px; background: var(--line); border-radius: var(--radius-full); overflow: hidden; }
.chart-bar-row__fill { height: 100%; background: var(--accent); border-radius: var(--radius-full); }
.chart-bar-row__value { flex: 0 0 auto; font-size: var(--fs-sm); font-weight: 700; min-width: 3.5rem; text-align: right; }

/* Embudo: cada .funnel-step define su ancho con --w inline, ej. style="--w:70%" */
.funnel { display: flex; flex-direction: column; align-items: center; gap: 2px; margin: var(--space-4) 0; }
.funnel-step {
  width: var(--w, 100%);
  max-width: 100%;
  padding: var(--space-3);
  text-align: center;
  color: #fff;
  font-size: var(--fs-sm);
  font-weight: 700;
  background: var(--accent);
  border-radius: var(--radius-sm);
}
.funnel-step:nth-child(2) { opacity: .85; }
.funnel-step:nth-child(3) { opacity: .7; }
.funnel-step:nth-child(4) { opacity: .55; }
.funnel-step:nth-child(5) { opacity: .4; }

/* Línea de tiempo vertical */
.timeline { position: relative; margin: var(--space-5) 0; padding-left: var(--space-6); border-left: 3px solid var(--line-strong); }
.timeline-item { position: relative; margin-bottom: var(--space-5); }
.timeline-item::before {
  content: "";
  position: absolute;
  left: calc(-1 * var(--space-6) - 7px);
  top: 4px;
  width: 14px;
  height: 14px;
  border-radius: 50%;
  background: var(--accent);
  border: 3px solid var(--paper);
}
.timeline-item__date { font-size: var(--fs-sm); font-weight: 700; color: var(--accent-dark); }
.timeline-item__title { font-family: var(--font-serif); font-size: var(--fs-lg); margin: var(--space-1) 0; }

/* ===== 17. Botones ===== */
.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: var(--space-2);
  min-height: var(--tap);
  padding: 0 var(--space-5);
  border: none;
  border-radius: var(--radius-sm);
  background: var(--accent);
  color: #fff;
  font-size: var(--fs-base);
  font-weight: 700;
  text-decoration: none;
  cursor: pointer;
}
.btn:hover { background: var(--accent-dark); }
.btn--ghost { background: transparent; border: 2px solid var(--line-strong); color: var(--ink); }
.btn--ghost:hover { border-color: var(--accent); color: var(--accent); }

/* ===== 18. Media queries (mobile-first: base = ~375px) ===== */
@media (min-width: 640px) {
  .kpi-grid { grid-template-columns: repeat(3, 1fr); }
  .grid-2 { grid-template-columns: repeat(2, 1fr); }
  .hero { padding: var(--space-8) var(--space-6); }
}
@media (min-width: 960px) {
  .kpi-grid { grid-template-columns: repeat(4, 1fr); }
  .grid-2 { grid-template-columns: repeat(2, 1fr); }
  .grid-3 { grid-template-columns: repeat(3, 1fr); }
}

/* ===== 19. Impresión ===== */
@media print {
  .docnav, .copyblock__btn, .btn { display: none !important; }
  body { background: #fff; color: #000; }
  .hero { background: #fff !important; color: #000 !important; }
  .hero h1, .hero p { color: #000 !important; }
  .card, .callout, .kpi, .copyblock { box-shadow: none; border: 1px solid #999; }
  a[href]::after { content: " (" attr(href) ")"; font-size: .8em; }
}
```

### Notas de uso de componentes

- **`.sec` numeradas automáticamente**: envolver cada sección principal en `<section class="sec"><h2>Título</h2>...</section>`. El número circular aparece solo, vía contador CSS — nunca escribir el número a mano en el `<h2>`.
- **Gráficos (`.chart-bar-row`, `.funnel-step`, `.timeline-item`)**: por defecto pintan con `--accent`. Si un gráfico puntual necesita codificar semántica propia (por ejemplo, el embudo Instagram → Tienda de `estrategia-nucleo.md`, que ya usa rosado para Instagram y verde para Tienda), es válido sobrescribir el color con `style="background:var(--info)"` o similar en ese elemento puntual — la clase base define la forma, no una semántica de color obligatoria.
- **`.grid-2` / `.grid-3`**: 1 columna en móvil siempre; 2 columnas desde 640px; 3 columnas (solo `.grid-3`) desde 960px.

---

## 3. Markup canónico de navegación

HTML exacto del `.docnav`, con los 6 links en español y en este orden. Va como primer elemento dentro de `<body>`, antes del `.hero`.

```html
<nav class="docnav" aria-label="Navegación del plan">
  <div class="docnav__inner">
    <a href="index.html" class="docnav__link">Plan</a>
    <a href="kit-arranque.html" class="docnav__link">Kit de arranque</a>
    <a href="guion-reels.html" class="docnav__link">Guiones de Reels</a>
    <a href="sop-dm.html" class="docnav__link">Manual de DM</a>
    <a href="recursos.html" class="docnav__link">Recursos</a>
    <a href="tablero.html" class="docnav__link">Tablero</a>
  </div>
</nav>
```

**Cómo marcar `.active`:** en cada página, el link correspondiente a esa página agrega la clase `active` y el atributo `aria-current="page"`. Ejemplo para `kit-arranque.html`:

```html
<a href="kit-arranque.html" class="docnav__link active" aria-current="page">Kit de arranque</a>
```

Los otros 5 links quedan exactamente como en el bloque canónico (sin `active` ni `aria-current`). Todos los `href` son relativos (sin `/` inicial ni dominio) para que el sitio funcione igual en GitHub Pages en cualquier subruta.

---

## 4. JS canónico del botón Copiar

Un solo listener por página, delegado en `document`. Se copia entero en cada página (dentro de un único `<script>` al final del `<body>`, junto con el resto del JS de esa página si corresponde).

```html
<script>
  // Copiar al portapapeles — delegación de eventos, un solo listener por página.
  document.addEventListener('click', function (e) {
    var btn = e.target.closest('[data-copy-target]');
    if (!btn) return;
    var el = document.getElementById(btn.getAttribute('data-copy-target'));
    if (!el) return;
    copiarTexto(el.innerText || el.textContent || '', btn);
  });

  function copiarTexto(texto, btn) {
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(texto).then(
        function () { mostrarCopiado(btn); },
        function () { copiarConFallback(texto, btn); }
      );
    } else {
      copiarConFallback(texto, btn);
    }
  }

  function copiarConFallback(texto, btn) {
    var ta = document.createElement('textarea');
    ta.value = texto;
    ta.setAttribute('readonly', '');
    ta.style.position = 'fixed';
    ta.style.top = '-1000px';
    document.body.appendChild(ta);
    ta.select();
    try { document.execCommand('copy'); } catch (err) { /* sin soporte, se ignora */ }
    document.body.removeChild(ta);
    mostrarCopiado(btn);
  }

  function mostrarCopiado(btn) {
    var original = btn.getAttribute('data-label') || btn.textContent;
    btn.setAttribute('data-label', original);
    btn.textContent = '✓ ¡Copiado!';
    btn.classList.add('is-copied');
    clearTimeout(btn._copyTimeout);
    btn._copyTimeout = setTimeout(function () {
      btn.textContent = original;
      btn.classList.remove('is-copied');
    }, 2000);
  }
</script>
```

**Markup del `.copyblock` que activa este JS** — el `id` del texto y el `data-copy-target` del botón deben coincidir, y ese `id` debe ser único en la página:

```html
<div class="copyblock">
  <button type="button" class="copyblock__btn" data-copy-target="copy-bio-1">Copiar</button>
  <div class="copyblock__text" id="copy-bio-1">Texto exacto a copiar va aquí, tal cual se debe pegar.</div>
</div>
```

---

## 5. Contrato de localStorage

Todas las claves usan el prefijo `pedraza-plan:`. Este contrato lo respetan `index.html` (escribe) y `tablero.html` (lee).

| Clave | Formato | Quién la usa |
|---|---|---|
| `pedraza-plan:task:<id>` | `"1"` si está marcada (se borra la clave si se desmarca) | `index.html` (checklist maestra) |
| `pedraza-plan:__progress` | JSON `{"done":N,"total":N,"pct":N}` | Escrita por `index.html`, leída por `tablero.html` |
| `pedraza-plan:sheet-url` | string (URL CSV del Google Sheet, formato gviz — ver sección 6) | `tablero.html` |

**Solo `index.html` tiene checkboxes con `data-task`** (es la checklist maestra del plan). `tablero.html` no declara checkboxes propios: solo lee `pedraza-plan:__progress` para mostrarlo como una tarjeta KPI adicional ("Avance del plan"), y debe manejar con gracia el caso en que la clave todavía no exista (nadie ha abierto `index.html` todavía en ese navegador).

**`<id>` de cada tarea**: kebab-case, único dentro de `index.html`, estable en el tiempo (no reusar un id para una tarea distinta aunque cambie el orden de la lista — si una tarea se elimina, no reciclar su id).

Nota importante para quien construya `index.html` y `tablero.html`: `localStorage` es por navegador y dispositivo, no se sincroniza entre el celular de un hermano y el computador del otro. Es una limitación conocida y aceptada para este entregable (no hay backend), no un bug — no hace falta resolverla, pero conviene no prometer en el copy de la página que el progreso "se comparte entre ambos".

### JS canónico de acceso a localStorage (prerrequisito de `index.html` y `tablero.html`)

Toda página que lea o escriba `localStorage` incluye primero este bloque — es un prerrequisito tanto del JS del checklist (más abajo, usado por `index.html`) como del JS del tablero (sección 6, usado por `tablero.html`, incluyendo el guardado de `pedraza-plan:sheet-url`). Se copia una sola vez por página, antes de cualquier otro script que llame a `pgGet`/`pgSet`/`pgRemove`.

```html
<script>
  // Acceso seguro a localStorage (no revienta en navegación privada u otros bloqueos).
  // Prerrequisito de: JS del checklist (index.html) y JS del tablero (tablero.html).
  function pgGet(key) { try { return localStorage.getItem(key); } catch (e) { return null; } }
  function pgSet(key, valor) { try { localStorage.setItem(key, valor); } catch (e) { /* sin soporte, se ignora */ } }
  function pgRemove(key) { try { localStorage.removeItem(key); } catch (e) { /* sin soporte, se ignora */ } }
</script>
```

### JS canónico del checklist (para `index.html`, requiere el bloque anterior)

```html
<script>
  document.addEventListener('DOMContentLoaded', function () {
    // Carga el estado guardado de cada checkbox de la checklist.
    document.querySelectorAll('[data-task]').forEach(function (cb) {
      cb.checked = pgGet('pedraza-plan:task:' + cb.getAttribute('data-task')) === '1';
    });
    actualizarProgreso();
  });

  // Delegación: un solo listener de cambio para toda la checklist.
  document.addEventListener('change', function (e) {
    var cb = e.target.closest('[data-task]');
    if (!cb) return;
    var key = 'pedraza-plan:task:' + cb.getAttribute('data-task');
    if (cb.checked) { pgSet(key, '1'); } else { pgRemove(key); }
    actualizarProgreso();
  });

  function actualizarProgreso() {
    var cajas = document.querySelectorAll('[data-task]');
    var total = cajas.length;
    var done = 0;
    cajas.forEach(function (cb) { if (cb.checked) done++; });
    var pct = total ? Math.round((done / total) * 100) : 0;

    pgSet('pedraza-plan:__progress', JSON.stringify({ done: done, total: total, pct: pct }));

    document.querySelectorAll('[data-progress-fill]').forEach(function (fill) {
      fill.style.width = pct + '%';
    });
    document.querySelectorAll('[data-progress-label]').forEach(function (label) {
      label.textContent = done + ' de ' + total + ' tareas (' + pct + '%)';
    });
  }
</script>
```

**Markup de un ítem de checklist** (cada `data-task` es único y kebab-case):

```html
<ul class="checklist">
  <li>
    <label>
      <input type="checkbox" data-task="publicar-bio-nueva">
      <span>Publicar la bio nueva en Instagram</span>
    </label>
  </li>
</ul>
```

**Markup de la barra de progreso** que este JS actualiza:

```html
<div class="progress">
  <div class="progress__track">
    <div class="progress__fill" data-progress-fill></div>
  </div>
  <span class="progress__label" data-progress-label>0 de 0 tareas (0%)</span>
</div>
```

---

## 6. Parser CSV del tablero (`tablero.html`)

### Formato esperado del Google Sheet

- **Primera fila:** encabezados. Deben incluir exactamente estas 13 columnas (la primera identifica la semana, las otras 12 son los KPIs de `estrategia-nucleo.md` sección 8, en este orden):

  `Semana, Alcance, Alcance no-seguidores, Reproducciones de Reels, Guardados, Compartidos, Comentarios, Seguidores nuevos, DMs iniciados, Clics al link de bio, Sesiones de la tienda desde IG, Pedidos, Ingresos`

- **Cada fila siguiente = una semana** de datos (una fila por semana, la más reciente puede ir arriba o abajo — `tablero.html` decide el orden al graficar, pero el parser no asume ninguno).
- Valores numéricos como texto plano (sin separador de miles, sin símbolo `$`); si una celda viene vacía, se trata como dato faltante, no como cero.

### Cómo compartir el Sheet

En Google Sheets: **Compartir → Cambiar a "Cualquiera con el enlace" → rol "Lector"**. Luego usar como `pedraza-plan:sheet-url` el link del endpoint **gviz** de esa hoja, no el de exportación directa:

```
https://docs.google.com/spreadsheets/d/ID_DE_LA_HOJA/gviz/tq?tqx=out:csv&sheet=NOMBRE_DE_LA_PESTAÑA
```

También acepta `&gid=ID_DE_LA_PESTAÑA` en vez de `&sheet=NOMBRE_DE_LA_PESTAÑA` si es más fácil de obtener.

- `ID_DE_LA_HOJA` se saca de la URL cuando el Sheet está abierto en el navegador (el tramo largo entre `/d/` y el siguiente `/`).
- `NOMBRE_DE_LA_PESTAÑA` es el nombre literal de la pestaña (tal como aparece en la solapa inferior del Sheet, ej. `Semanas`); si tiene espacios o tildes, van codificados en la URL (ej. `Semana%201`). Alternativa más simple: usar `gid`, el número que aparece al final de la URL después de `#gid=` cuando esa pestaña está abierta.

**Por qué gviz y no `/export?format=csv`:** el endpoint de exportación directa (`/export?format=csv&gid=...`) no manda cabeceras CORS, así que el navegador bloquea la respuesta cuando `tablero.html` la pide con `fetch()` desde fuera de `docs.google.com` — el request falla aunque el Sheet esté bien compartido. El endpoint `gviz/tq?tqx=out:csv` sí manda esas cabeceras y es el que debe quedar guardado en `pedraza-plan:sheet-url`. Si un usuario pega igual un link `/export?format=csv...`, `tablero.html` puede intentarlo (el `fetch` fallará limpio y caerá en el callout de "error de red" de más abajo), pero el formato recomendado y documentado para que funcione es siempre gviz.

Nota sobre el contenido que entrega gviz: `tqx=out:csv` devuelve **todas las celdas entre comillas dobles**, incluidas las numéricas (ej. `"1234"` en vez de `1234`). El parser canónico de abajo ya maneja comillas en cualquier celda, así que no requiere ningún ajuste — pero al mostrar los valores no hay que asumir que llegan "limpios" de comillas antes de pasar por `parseCSV`.

### Código canónico del parser

```html
<script>
  // Parser CSV mínimo: maneja comillas, comas dentro de comillas y saltos de línea dentro de comillas.
  function parseCSV(texto) {
    var filas = [];
    var fila = [];
    var campo = '';
    var entreComillas = false;

    for (var i = 0; i < texto.length; i++) {
      var c = texto[i];
      if (entreComillas) {
        if (c === '"') {
          if (texto[i + 1] === '"') { campo += '"'; i++; } // comilla escapada ""
          else { entreComillas = false; }
        } else {
          campo += c;
        }
      } else if (c === '"') {
        entreComillas = true;
      } else if (c === ',') {
        fila.push(campo); campo = '';
      } else if (c === '\r') {
        // se ignora, el salto de fila real lo maneja \n
      } else if (c === '\n') {
        fila.push(campo); campo = '';
        filas.push(fila); fila = [];
      } else {
        campo += c;
      }
    }
    if (campo.length > 0 || fila.length > 0) { fila.push(campo); filas.push(fila); }

    // descarta filas totalmente vacías (líneas en blanco al final del archivo)
    return filas.filter(function (f) { return f.length > 1 || f[0] !== ''; });
  }

  // Convierte filas crudas en objetos { NombreColumna: valor } usando la primera fila como encabezado.
  function csvAFilasKpi(filas) {
    if (!filas.length) return { headers: [], semanas: [] };
    var headers = filas[0].map(function (h) { return h.trim(); });
    var semanas = filas.slice(1)
      .filter(function (f) { return f.some(function (v) { return v.trim() !== ''; }); })
      .map(function (f) {
        var obj = {};
        headers.forEach(function (h, i) { obj[h] = (f[i] || '').trim(); });
        return obj;
      });
    return { headers: headers, semanas: semanas };
  }
</script>
```

### Carga con manejo de errores (patrón canónico de `cargarTablero()`)

Requiere el bloque de acceso a `localStorage` de la sección 5 (`pgGet`/`pgSet`/`pgRemove`) ya cargado antes de este script, más un contenedor `<div id="tablero-estado"></div>` en el HTML donde se inyectan los estados. `renderTablero(semanas)` es la función propia de `tablero.html` que dibuja KPIs/tabla/gráficos ya con los datos parseados — eso sí es específico de esa página, no del sistema de diseño.

`tablero.html` también necesita `pgSet` para guardar la URL que el usuario configure (no solo `pgGet` para leerla), por ejemplo desde un campo de configuración:

```html
<script>
  function guardarSheetUrl(url) {
    pgSet('pedraza-plan:sheet-url', url.trim());
    cargarTablero();
  }
</script>
```

```html
<script>
  var KPI_HEADERS = [
    'Semana', 'Alcance', 'Alcance no-seguidores', 'Reproducciones de Reels',
    'Guardados', 'Compartidos', 'Comentarios', 'Seguidores nuevos',
    'DMs iniciados', 'Clics al link de bio', 'Sesiones de la tienda desde IG',
    'Pedidos', 'Ingresos'
  ];

  async function cargarTablero() {
    var estado = document.getElementById('tablero-estado');
    var url = pgGet('pedraza-plan:sheet-url');

    if (!url) {
      estado.innerHTML =
        '<div class="callout callout--warn"><p><strong>Falta configurar el Google Sheet.</strong> ' +
        'Pega el link de exportación CSV en el campo de configuración de esta página para ver el tablero. ' +
        'Recuerda compartir el Sheet como "Cualquiera con el enlace: Lector".</p></div>';
      return;
    }

    estado.innerHTML = '<div class="callout callout--info"><p>Cargando datos del Sheet…</p></div>';

    var texto;
    try {
      var res = await fetch(url, { cache: 'no-store' });
      if (!res.ok) throw new Error('HTTP ' + res.status);
      texto = await res.text();
    } catch (err) {
      estado.innerHTML =
        '<div class="callout callout--danger"><p><strong>No se pudo cargar el Sheet.</strong> ' +
        'Revisa tu conexión y que el link esté compartido como "Cualquiera con el enlace: Lector". ' +
        '<button type="button" class="btn" onclick="cargarTablero()">Reintentar</button></p></div>';
      return;
    }

    var filas = parseCSV(texto);
    if (filas.length < 2) {
      estado.innerHTML =
        '<div class="callout callout--danger"><p><strong>El Sheet está vacío o no se pudo leer.</strong> ' +
        'Verifica que la primera fila tenga los encabezados y que haya al menos una semana de datos cargada.</p></div>';
      return;
    }

    var datos = csvAFilasKpi(filas);
    var faltantes = KPI_HEADERS.filter(function (h) { return datos.headers.indexOf(h) === -1; });

    if (faltantes.length) {
      estado.innerHTML =
        '<div class="callout callout--warn"><p><strong>Faltan columnas en el Sheet:</strong> ' +
        faltantes.join(', ') + '. Se muestra lo que sí está disponible.</p></div>';
    } else {
      estado.innerHTML = '';
    }

    renderTablero(datos.semanas); // función propia de tablero.html
  }
</script>
```

Los 3 estados de error quedan cubiertos: **sin URL configurada** (callout amarillo con instrucciones), **error de red** (callout rojo con botón "Reintentar"), **CSV mal formado** (callout rojo si no hay datos, callout amarillo si faltan columnas puntuales pero se puede mostrar algo igual).

---

## 7. Reglas de página y plantilla de esqueleto

Reglas fijas para las 6 páginas:

- `<html lang="es">`.
- `<meta charset="UTF-8">` antes que cualquier otro meta (necesario para que el favicon con emoji funcione bien).
- `<meta name="viewport" content="width=device-width, initial-scale=1">`.
- `<meta name="robots" content="noindex,nofollow">` — el sitio se comparte por link directo, no debe indexarse.
- Favicon: el mismo emoji 🦋 (mariposa, ya usado en la bio de referencia de `estrategia-nucleo.md`) vía SVG inline en un `data:` URI — cero requests externos. Tag exacto, igual en las 6 páginas:

  ```html
  <link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>🦋</text></svg>">
  ```

- Título exacto por página (formato `Nombre de la página — Plan Pedraza Ilustración`):

  | Archivo | Etiqueta en el nav | `<title>` exacto |
  |---|---|---|
  | `index.html` | Plan | `Plan y estrategia — Plan Pedraza Ilustración` |
  | `kit-arranque.html` | Kit de arranque | `Kit de arranque — Plan Pedraza Ilustración` |
  | `guion-reels.html` | Guiones de Reels | `Guiones de Reels — Plan Pedraza Ilustración` |
  | `sop-dm.html` | Manual de DM | `Manual de DM — Plan Pedraza Ilustración` |
  | `recursos.html` | Recursos | `Recursos — Plan Pedraza Ilustración` |
  | `tablero.html` | Tablero | `Tablero de KPIs — Plan Pedraza Ilustración` |

- Todo el CSS (sección 2) y todo el JS (secciones 4-6, según la página) van **inline** dentro del propio archivo HTML. Cero `<link>` a hojas externas, cero `<script src="https://...">`, cero fuentes ni imágenes remotas.
- Enlaces internos siempre relativos (`kit-arranque.html`, nunca `/kit-arranque.html` ni una URL completa).

### Plantilla de esqueleto (punto de partida para cada página)

```html
<!doctype html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex,nofollow">
<title>__TÍTULO_EXACTO_DE_LA_TABLA__</title>
<link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>🦋</text></svg>">
<style>
  /* === Pegar aquí el bloque CSS canónico completo de la sección 2 === */
</style>
</head>
<body>

<nav class="docnav" aria-label="Navegación del plan">
  <div class="docnav__inner">
    <a href="index.html" class="docnav__link">Plan</a>
    <a href="kit-arranque.html" class="docnav__link">Kit de arranque</a>
    <a href="guion-reels.html" class="docnav__link">Guiones de Reels</a>
    <a href="sop-dm.html" class="docnav__link">Manual de DM</a>
    <a href="recursos.html" class="docnav__link">Recursos</a>
    <a href="tablero.html" class="docnav__link">Tablero</a>
    <!-- Recordar: en la página actual, agregar class="active" aria-current="page" al link correspondiente -->
  </div>
</nav>

<header class="hero">
  <div class="hero__inner">
    <h1>Título de la página</h1>
    <p>Bajada breve de una o dos líneas.</p>
  </div>
</header>

<main class="wrap">
  <section class="sec">
    <h2>Título de la primera sección</h2>
    <p>Contenido…</p>
  </section>
</main>

<script>
  /* === Pegar aquí el JS del botón Copiar (sección 4) y, si aplica, el de la checklist (sección 5)
     o el del tablero (sección 6) === */
</script>
</body>
</html>
```

---

## 8. Checklist de calidad por página

Lo que revisa el orquestador antes de aceptar cada página:

- [ ] Se ve impecable a 375px de ancho (probar mentalmente o en un emulador angosto), sin scroll horizontal en el `<body>`.
- [ ] Todos los botones, checkboxes y links del nav tienen un área táctil de al menos 44px de alto.
- [ ] El HTML está balanceado (todo tag abierto se cierra), sin errores de anidamiento.
- [ ] Cero errores en la consola del navegador (JS sin excepciones al cargar ni al interactuar).
- [ ] El `.docnav` es idéntico —mismos 6 links, mismo orden, mismo texto— y solo el link de la página actual tiene `class="active"` y `aria-current="page"`.
- [ ] Cero URLs externas en todo el archivo: sin CDNs, sin Google Fonts, sin imágenes remotas, sin `fetch()` a otro dominio que no sea el Google Sheet configurado por el usuario en `tablero.html`.
- [ ] `<html lang="es">`, meta viewport, meta robots y favicon presentes tal cual la plantilla.
- [ ] `<title>` exacto según la tabla de la sección 7.
- [ ] Todo bloque de texto copiable (bio, guion, mensaje de DM, caption) está dentro de un `.copyblock` con botón funcional, y el texto es copy real, sin `[placeholders]`.
- [ ] Si la página usa `localStorage`, respeta el prefijo `pedraza-plan:` y las claves exactas del contrato (sección 5).
- [ ] Las secciones principales están envueltas en `.sec` con `<h2>` (numeración automática, no escrita a mano).
