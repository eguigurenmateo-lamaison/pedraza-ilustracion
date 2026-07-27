# Sistema de diseño — Sitio del plan Pedraza Ilustración

Especificación única para las 6 páginas del sitio (`index.html`, `kit-arranque.html`, `guion-reels.html`, `sop-dm.html`, `recursos.html`, `tablero.html`). La construyen 6 desarrolladores en paralelo, cada uno en su propio archivo — por eso **todos los bloques de código de este documento se copian tal cual, sin modificar**. Solo cambia el contenido específico de cada página (texto, tablas, gráficos), nunca la estructura de clases, variables ni scripts base.

Este documento es material de trabajo interno (vive en `docs/`, no se comparte con el cliente). El resultado final — las 6 páginas HTML — sí es el entregable compartible.

## Índice

1. Identidad visual (paleta, tipografía, variables CSS)
2. Bloque CSS canónico completo
3. Markup y JS canónicos de navegación (barra superior + panel completo)
4. JS canónico del botón Copiar
5. Contrato de localStorage y checklist
6. Parser CSV del tablero
7. Reglas de página y plantilla de esqueleto HTML
8. Checklist de calidad por página

---

## 1. Identidad visual

> **Sistema v2 (jul-2026).** Esta sección y la sección 2 (bloque CSS canónico) reemplazan por completo a la versión anterior del sistema en las páginas HTML del sitio. El contrato de clases no cambió — ningún nombre de clase, ningún elemento del marcado — solo el aspecto: espaciado, tipografía, superficies, radios y sombras. Cualquier página que pegue el bloque CSS de la sección 2 encima de su marcado existente queda actualizada sin tocar una sola línea de HTML.

### Dirección estética: limpia, curada y serena, tipo iOS

El pedido del cliente fue explícito: una estética muy cuidada al estilo Apple/iOS, con formas redondeadas, colores agradables y — el punto más importante — que cada elemento tenga espacio y protagonismo propio, sin competir con los de al lado. El sitio v1 se sentía denso (bordes duros, callouts de color saturado, tipografía mixta serif/sans). El sistema v2 resuelve esto con cinco movimientos, sin tocar los colores de marca:

1. **Más aire.** La escala de espaciado sube un peldaño completo y los saltos grandes (separación entre secciones, padding del hero) son fluidos con `clamp()`: generosos en escritorio (4-6rem), proporcionales en el celular.
2. **Fondo agrupado, tarjetas blancas.** El "papel cálido" se convierte en un gris cálido muy suave (fondo agrupado tipo iOS) y las tarjetas pasan a blanco puro — la separación entre superficies se lee por contraste tonal, no por bordes marcados.
3. **Sombras en capas, bordes hairline.** Se reemplaza la sombra única por 2-3 capas muy tenues (`--shadow-xs/sm`), y los bordes duros pasan a líneas hairline casi imperceptibles (`rgba` translúcido sobre tinta, no un gris fijo).
4. **Una sola voz tipográfica.** Se retira la pila serif editorial (Georgia) y todo — títulos, cuerpo, números de KPI, fechas de la línea de tiempo — pasa a la pila de sistema (`-apple-system` / SF Pro y equivalentes). La jerarquía ya no se construye alternando familia tipográfica, sino con peso alto (700-800) y letter-spacing negativo en los títulos, que es como Apple logra el look "una sola voz, muy cuidada". Detalle de compatibilidad: la variable `--font-serif` se conserva (para no romper ningún uso inline en las otras páginas del sitio) pero ahora apunta a la misma pila sans.
5. **Color con moderación.** Los callouts dejan de ser bloques de fondo saturado y pasan a superficies blancas sobrias con un detalle de color: una barra lateral fina y un ícono en una burbuja de color. El acento (rojo copihue) sigue reservado para la acción, y por eso aparece menos y destaca más.

### Paleta

Los colores de identidad de la marca **no cambian**: el verde naturaleza (`#3B5751`) y el rojo copihue (`#b0223f`) se mantienen exactamente en los mismos hex y con el mismo reparto de responsabilidades que en v1 — **el verde de marca cubre identidad y estructura** (fondo del nav, gradiente del hero, encabezados de tabla, círculo numerado de cada sección, relleno de la barra de progreso, checkboxes, puntos de la línea de tiempo) y **el rojo copihue queda reservado para la acción** (botones, botón Copiar, subrayado del link activo del nav, pills por defecto, embudo). Lo que cambia en v2 son los tonos neutros de apoyo — tinta, papel, superficie y líneas — para lograr el fondo agrupado y las tarjetas blanco puro del look iOS, más la forma (radios, sombras) descrita en la sección siguiente.

| Token | Valor | Uso |
|---|---|---|
| `--ink` | `#1c2420` | Texto principal (gris oscuro, no negro puro) |
| `--ink-soft` | `#4c5850` | Texto secundario, etiquetas |
| `--ink-faint` | `#7c887f` | Texto terciario, marcas de tiempo |
| `--paper` | `#f4f2ed` | Fondo de página — gris cálido suave, fondo "agrupado" tipo iOS (antes: papel cálido `#faf6ee`) |
| `--surface` | `#ffffff` | Fondo de tarjetas y bloques — blanco puro (antes: `#fffefb`) |
| `--line` | `rgba(28, 36, 32, .08)` | Bordes hairline, casi imperceptibles (antes: hex sólido `#e6ded0`) |
| `--line-strong` | `rgba(28, 36, 32, .16)` | Bordes de énfasis, separadores de sección, track de progreso/barras (antes: hex sólido `#d6c9b0`) |
| `--accent` | `#b0223f` | Rojo copihue — color de acción: botones, botón Copiar, link activo del nav, pills, embudo (sin cambios) |
| `--accent-dark` | `#7c1830` | Hover/gradiente del acento (sin cambios) |
| `--accent-soft` | `#f8dfe4` | Fondos tenues de acento (pills, badges, chip de ícono del callout) (sin cambios) |
| `--success` | `#2f6b4a` | Verde bosque — éxito, cifras positivas (sin cambios) |
| `--success-soft` | `#dcece1` | Fondo tenue de éxito (sin cambios) |
| `--warn` | `#a8720a` | Alerta 🟡 (sin cambios) |
| `--warn-soft` | `#f8ecd2` | Fondo tenue de alerta (sin cambios) |
| `--danger` | `#ae3d17` | Peligro / error — terracota (sin cambios) |
| `--danger-soft` | `#f7ddd0` | Fondo tenue de peligro (sin cambios) |
| `--brand-green` | `#3b5751` | Verde naturaleza del sitio web de la marca — identidad y estructura (sin cambios) |
| `--brand-green-dark` | `#2a403c` | Tono oscuro del verde de marca, gradiente del hero (sin cambios) |
| `--brand-green-soft` | `#e3eae8` | Fondo tenue del verde de marca; alias base de `--info-soft` (sin cambios) |
| `--info` | `#3b5751` (= `--brand-green`) | Información neutra — callouts y pills informativos |
| `--info-soft` | `#e3eae8` (= `--brand-green-soft`) | Fondo tenue de información |

### Tipografía

Pila de sistema única, cero fuentes web:

```css
--font-sans: -apple-system, BlinkMacSystemFont, "SF Pro Text", "SF Pro Display", "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
--font-serif: var(--font-sans); /* alias de compatibilidad — ver justificación arriba */
--font-mono: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, monospace;
```

**Por qué se abandona la serif editorial:** el sistema v1 usaba Georgia en los títulos para un aire de "guía de campo". El pedido del cliente para v2 es una estética limpia tipo iOS, y ese look se construye con una sola familia tipográfica bien jerarquizada (peso, tamaño, letter-spacing), no combinando dos. Mantener la serif habría competido con la limpieza que pide el rediseño. Los títulos ahora usan peso 700-800 y letter-spacing negativo (-0.01em a -0.03em, más cerrado cuanto más grande el texto) para lograr esa sensación "curada" sin cambiar de familia. Tamaños fluidos con `clamp()` en toda la escala (ver `--fs-*`), line-height 1.6 en cuerpo y 1.15 en títulos.

### Radios, sombras y espaciado

- **Radios:** generosos y consistentes — `--radius-sm` 12px (elementos chicos: botones ghost, chips), `--radius` 20px (tarjetas, callouts, copyblock, KPIs, tabla), `--radius-lg` 28px (disponible para superficies grandes puntuales), `--radius-full` cápsula completa (botones, pills, progreso, tracks de barra).
- **Sombras:** dos-tres capas muy tenues, nunca marcadas — `--shadow-xs` para detalles sutiles (badges, tabla), `--shadow-sm` para tarjetas y KPIs en reposo, `--shadow` (más profunda, dos capas) disponible para estados elevados puntuales. Los bordes duros del sistema anterior pasan a líneas hairline en `rgba` (`--line` / `--line-strong`), casi imperceptibles.
- **Espaciado:** escala de 8 pasos en `rem`. Los primeros 5 pasos (`--space-1` a `--space-5`) son valores fijos para controles y padding interno; los 3 pasos grandes (`--space-6` a `--space-8`, usados en separación entre secciones y padding del hero) son fluidos con `clamp()` — generosos en escritorio, proporcionales en el celular, sin necesidad de una media query aparte para "dar más aire" en pantallas grandes.
- **Movimiento:** transiciones discretas de 150-250ms (`--dur` + `--ease`) en hover/estados de botones, links del nav, checklist y barras — se desactivan automáticamente si el sistema tiene activado "reducir movimiento" (`prefers-reduced-motion`).

---

## 2. Bloque CSS canónico completo

Este bloque completo va dentro de un único `<style>...</style>` en el `<head>` de cada una de las 6 páginas. Se copia **entero y sin editar** — el contenido de cada página se ajusta con las clases ya definidas aquí, nunca escribiendo CSS nuevo suelto en cada archivo (si una página necesita algo muy puntual, un `style=""` inline puntual es aceptable; no crear una segunda hoja de estilos).

```css
/* ==========================================================================
   Sistema de diseño v2 — Plan Pedraza Ilustración
   Estética limpia, curada y serena, tipo iOS. Mismo contrato de clases
   que el sistema v1: solo cambia el aspecto (espacio, tipografía,
   superficies, radios, sombras), nunca la estructura de marcado.
   Bloque único y canónico. No editar por página: solo usar estas clases.
   ========================================================================== */

:root {
  color-scheme: light;

  /* --- tinta y superficies: fondo agrupado gris cálido, tarjetas blanco puro --- */
  --ink: #1c2420;
  --ink-soft: #4c5850;
  --ink-faint: #7c887f;
  --paper: #f4f2ed;
  --surface: #ffffff;
  --line: rgba(28, 36, 32, .08);
  --line-strong: rgba(28, 36, 32, .16);

  /* --- acento: rojo copihue (color de acción, se mantiene) --- */
  --accent: #b0223f;
  --accent-dark: #7c1830;
  --accent-soft: #f8dfe4;

  /* --- verde naturaleza del sitio web de la marca (identidad y estructura, se mantiene) --- */
  --brand-green: #3b5751;
  --brand-green-soft: #e3eae8;
  --brand-green-dark: #2a403c;

  /* --- apoyo semántico (valores de marca sin cambios) --- */
  --success: #2f6b4a;
  --success-soft: #dcece1;
  --warn: #a8720a;
  --warn-soft: #f8ecd2;
  --danger: #ae3d17;
  --danger-soft: #f7ddd0;
  --info: var(--brand-green);
  --info-soft: var(--brand-green-soft);

  /* --- forma: radios generosos y consistentes --- */
  --radius-xs: 8px;
  --radius-sm: 12px;
  --radius: 20px;
  --radius-lg: 28px;
  --radius-full: 999px;

  /* --- sombras suaves y en capas, nunca marcadas --- */
  --shadow-xs: 0 1px 2px rgba(24, 32, 28, .04);
  --shadow-sm: 0 1px 3px rgba(24, 32, 28, .05), 0 4px 10px rgba(24, 32, 28, .05);
  --shadow: 0 6px 16px rgba(24, 32, 28, .07), 0 16px 32px -12px rgba(24, 32, 28, .14);

  /* --- espaciado: escala amplia; los saltos grandes son fluidos (más aire en desktop, proporcional en móvil) --- */
  --space-1: .25rem;
  --space-2: .5rem;
  --space-3: .875rem;
  --space-4: 1.25rem;
  --space-5: 1.75rem;
  --space-6: clamp(2rem, 1.6rem + 1.6vw, 2.75rem);
  --space-7: clamp(2.75rem, 2rem + 3vw, 4.5rem);
  --space-8: clamp(3.5rem, 2.3rem + 5vw, 6rem);

  /* --- tipografía: una sola voz, pila de sistema (ver sección 1 del documento) --- */
  --font-sans: -apple-system, BlinkMacSystemFont, "SF Pro Text", "SF Pro Display", "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  --font-serif: var(--font-sans); /* alias de compatibilidad: el sistema v2 unifica todo en la pila sans, ver sección 1 */
  --font-mono: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, monospace;
  --fs-sm: clamp(.85rem, .81rem + .2vw, .92rem);
  --fs-base: clamp(1rem, .95rem + .25vw, 1.0625rem);
  --fs-lg: clamp(1.1rem, 1.02rem + .4vw, 1.25rem);
  --fs-h3: clamp(1.2rem, 1.1rem + .5vw, 1.4rem);
  --fs-h2: clamp(1.5rem, 1.3rem + 1vw, 1.9rem);
  --fs-h1: clamp(2rem, 1.6rem + 2.4vw, 3rem);

  /* --- área táctil mínima (regla mobile-first del proyecto) --- */
  --tap: 44px;

  /* --- movimiento discreto --- */
  --ease: cubic-bezier(.4, 0, .2, 1);
  --dur: 200ms;
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
  line-height: 1.6;
  color: var(--ink);
  background: var(--paper);
  -webkit-font-smoothing: antialiased;
  text-rendering: optimizeLegibility;
}
h1, h2, h3 { font-family: var(--font-sans); font-weight: 700; line-height: 1.15; letter-spacing: -.02em; color: var(--ink); }
h1 { font-size: var(--fs-h1); font-weight: 800; letter-spacing: -.03em; }
h2 { font-size: var(--fs-h2); }
h3 { font-size: var(--fs-h3); font-weight: 600; letter-spacing: -.01em; }
p { max-width: 68ch; color: var(--ink); }
strong { color: var(--ink); font-weight: 700; }
:focus-visible { outline: 3px solid var(--accent); outline-offset: 3px; }

/* ===== 3. Layout ===== */
.wrap { max-width: 960px; margin: 0 auto; padding: 0 var(--space-4) var(--space-8); }

/* ===== 4. Barra superior (.navbar) — translúcida, con fallback sólido ===== */
.navbar {
  position: sticky;
  top: 0;
  z-index: 50;
  background: var(--brand-green);
  border-bottom: 1px solid rgba(255, 255, 255, .08);
}
@supports ((backdrop-filter: blur(1px)) or (-webkit-backdrop-filter: blur(1px))) {
  .navbar {
    background: rgba(59, 87, 81, .72);
    -webkit-backdrop-filter: saturate(180%) blur(20px);
    backdrop-filter: saturate(180%) blur(20px);
  }
}
.navbar__inner {
  display: flex;
  align-items: center;
  gap: var(--space-2);
  max-width: 960px;
  margin: 0 auto;
  padding: var(--space-1) var(--space-3);
}
.navbar__home {
  flex: 0 0 auto;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: var(--tap);
  height: var(--tap);
  border-radius: var(--radius-full);
  font-size: 1.3rem;
  line-height: 1;
  text-decoration: none;
  color: #fff;
  transition: background var(--dur) var(--ease);
}
.navbar__home:hover, .navbar__home:active { background: rgba(255, 255, 255, .14); }
.navbar__title {
  flex: 1 1 auto;
  min-width: 0;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  color: #fff;
  font-size: var(--fs-sm);
  font-weight: 700;
  letter-spacing: -.01em;
}
.navbar__menu-btn {
  flex: 0 0 auto;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: var(--space-2);
  min-width: var(--tap);
  min-height: var(--tap);
  padding: 0 var(--space-3);
  border: none;
  border-radius: var(--radius-full);
  background: rgba(255, 255, 255, .14);
  color: #fff;
  cursor: pointer;
  transition: background var(--dur) var(--ease);
}
.navbar__menu-btn:hover { background: rgba(255, 255, 255, .22); }
.navbar__menu-icon { display: inline-flex; flex-direction: column; justify-content: center; gap: 4px; width: 18px; flex: 0 0 auto; }
.navbar__menu-icon span { display: block; height: 2px; width: 100%; background: #fff; border-radius: 2px; }
.navbar__menu-label { font-size: var(--fs-sm); font-weight: 600; white-space: nowrap; }
@media (max-width: 420px) { .navbar__menu-label { display: none; } }

/* ===== 4b. Panel de navegación completo (.navpanel) — 15 páginas en 4 grupos ===== */
html.nav-lock, body.nav-lock { overflow: hidden; }
.navpanel {
  position: fixed;
  inset: 0;
  z-index: 100;
  display: flex;
  align-items: flex-end;
  justify-content: center;
}
.navpanel[hidden] { display: none; }
.navpanel__backdrop {
  position: absolute;
  inset: 0;
  background: rgba(15, 20, 18, .5);
  opacity: 0;
  transition: opacity var(--dur) var(--ease);
}
.navpanel__sheet {
  position: relative;
  width: 100%;
  max-height: 92vh;
  background: var(--paper);
  border-radius: var(--radius-lg) var(--radius-lg) 0 0;
  box-shadow: var(--shadow);
  display: flex;
  flex-direction: column;
  transform: translateY(100%);
  transition: transform var(--dur) var(--ease);
}
.navpanel.is-open .navpanel__backdrop { opacity: 1; }
.navpanel.is-open .navpanel__sheet { transform: translateY(0); }
.navpanel__header {
  flex: 0 0 auto;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: var(--space-4) var(--space-4) var(--space-3);
  border-bottom: 1px solid var(--line);
}
.navpanel__headtitle { font-size: var(--fs-h3); font-weight: 800; letter-spacing: -.01em; color: var(--ink); }
.navpanel__close {
  flex: 0 0 auto;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: var(--tap);
  height: var(--tap);
  border: none;
  border-radius: var(--radius-full);
  background: var(--line-strong);
  color: var(--ink);
  font-size: 1.1rem;
  line-height: 1;
  cursor: pointer;
  transition: background var(--dur) var(--ease), color var(--dur) var(--ease);
}
.navpanel__close:hover { background: var(--accent-soft); color: var(--accent-dark); }
.navpanel__body {
  overflow-y: auto;
  -webkit-overflow-scrolling: touch;
  padding: var(--space-4) var(--space-4) var(--space-7);
}
.navpanel__group + .navpanel__group { margin-top: var(--space-5); }
.navpanel__group-title {
  margin: 0 0 var(--space-2);
  font-size: var(--fs-sm);
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: .06em;
  color: var(--ink-faint);
}
.navpanel__link {
  display: flex;
  align-items: center;
  gap: var(--space-3);
  min-height: calc(var(--tap) + 12px);
  padding: var(--space-3) var(--space-4);
  margin-bottom: var(--space-2);
  border-radius: var(--radius-sm);
  background: var(--surface);
  border: 1px solid var(--line);
  box-shadow: var(--shadow-xs);
  text-decoration: none;
  color: var(--ink);
  transition: border-color var(--dur) var(--ease), box-shadow var(--dur) var(--ease), background var(--dur) var(--ease);
}
.navpanel__link:hover { border-color: var(--line-strong); box-shadow: var(--shadow-sm); }
.navpanel__link:last-child { margin-bottom: 0; }
.navpanel__link-text { flex: 1 1 auto; min-width: 0; }
.navpanel__link-name { display: block; font-weight: 700; font-size: var(--fs-base); letter-spacing: -.01em; color: var(--ink); }
.navpanel__link-desc { display: block; margin-top: 2px; font-size: var(--fs-sm); color: var(--ink-soft); }
.navpanel__check {
  flex: 0 0 auto;
  width: 22px;
  height: 22px;
  border-radius: 50%;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  font-size: .8rem;
  color: #fff;
  background: var(--brand-green);
  opacity: 0;
  transform: scale(.6);
  transition: opacity var(--dur) var(--ease), transform var(--dur) var(--ease);
}
.navpanel__link--current { background: var(--brand-green-soft); border-color: transparent; }
.navpanel__link--current .navpanel__link-name { color: var(--brand-green-dark); }
.navpanel__link--current .navpanel__check { opacity: 1; transform: scale(1); }
@media (min-width: 640px) {
  .navpanel { align-items: center; padding: var(--space-5); }
  .navpanel__sheet {
    max-width: 560px;
    max-height: 84vh;
    border-radius: var(--radius-lg);
    transform: translateY(16px) scale(.98);
    opacity: 0;
    transition: transform var(--dur) var(--ease), opacity var(--dur) var(--ease);
  }
  .navpanel.is-open .navpanel__sheet { transform: translateY(0) scale(1); opacity: 1; }
}

/* ===== 5. Hero ===== */
.hero {
  padding: var(--space-8) var(--space-4);
  background:
    radial-gradient(120% 160% at 12% -20%, rgba(255, 255, 255, .14), transparent 55%),
    linear-gradient(160deg, var(--brand-green) 0%, var(--brand-green-dark) 100%);
  color: #fff;
}
.hero__inner { max-width: 960px; margin: 0 auto; }
.hero h1 { color: #fff; margin-bottom: var(--space-3); }
.hero p { color: rgba(255, 255, 255, .86); font-size: var(--fs-lg); font-weight: 400; max-width: 60ch; margin: 0; line-height: 1.55; }

/* ===== 6. Secciones numeradas (.sec) ===== */
main { counter-reset: sec; }
.sec { counter-increment: sec; margin-top: var(--space-7); }
.sec:first-of-type { margin-top: var(--space-6); }
.sec > h2 {
  display: flex;
  align-items: center;
  gap: var(--space-3);
  padding-bottom: var(--space-3);
  margin-bottom: var(--space-5);
  border-bottom: 1px solid var(--line-strong);
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
  background: var(--brand-green);
  color: #fff;
  font-family: var(--font-sans);
  font-size: .5em;
  font-weight: 700;
  box-shadow: var(--shadow-xs);
}

/* ===== 7. Callouts: superficies sobrias con un detalle de color ===== */
.callout {
  display: block;
  position: relative;
  padding: var(--space-5) var(--space-5) var(--space-5) calc(var(--space-5) + 2.1em + var(--space-4));
  border-radius: var(--radius);
  border: 1px solid var(--line);
  border-left: 4px solid var(--ink-faint);
  background: var(--surface);
  box-shadow: var(--shadow-xs);
  margin: var(--space-5) 0;
}
.callout::before {
  position: absolute;
  left: var(--space-5);
  top: var(--space-5);
  width: 2.1em;
  height: 2.1em;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  background: var(--paper);
  font-size: 1.1em;
  line-height: 1;
}
.callout p:last-child { margin-bottom: 0; }
.callout--info { border-left-color: var(--info); }
.callout--info::before { content: "💡"; background: var(--info-soft); }
.callout--success { border-left-color: var(--success); }
.callout--success::before { content: "✅"; background: var(--success-soft); }
.callout--warn { border-left-color: var(--warn); }
.callout--warn::before { content: "🟡"; background: var(--warn-soft); }
.callout--danger { border-left-color: var(--danger); }
.callout--danger::before { content: "🔴"; background: var(--danger-soft); }

/* ===== 8. Bloque copiable (.copyblock) ===== */
.copyblock {
  position: relative;
  margin: var(--space-5) 0;
  padding: calc(var(--tap) + var(--space-3)) var(--space-5) var(--space-5);
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: var(--radius);
  box-shadow: var(--shadow-sm);
}
.copyblock__text {
  font-family: var(--font-mono);
  font-size: var(--fs-sm);
  line-height: 1.6;
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
  border-radius: var(--radius-full);
  background: var(--accent);
  color: #fff;
  font-size: var(--fs-sm);
  font-weight: 700;
  cursor: pointer;
  transition: background var(--dur) var(--ease), transform var(--dur) var(--ease);
}
.copyblock__btn:hover { background: var(--accent-dark); }
.copyblock__btn:active { transform: scale(.96); }
.copyblock__btn.is-copied { background: var(--success); }

/* ===== 9. KPIs (.kpi) ===== */
.kpi-grid {
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  gap: var(--space-4);
  margin: var(--space-5) 0;
}
.kpi {
  padding: var(--space-5);
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: var(--radius);
  box-shadow: var(--shadow-sm);
}
.kpi__label { display: block; font-size: var(--fs-sm); font-weight: 600; color: var(--ink-soft); margin-bottom: var(--space-2); overflow-wrap: break-word; }
.kpi__value { display: block; font-family: var(--font-sans); font-size: clamp(1.35rem, 1.05rem + 1.4vw, 2.25rem); font-weight: 800; letter-spacing: -.02em; color: var(--ink); overflow-wrap: break-word; hyphens: none; }
.kpi__delta { display: inline-block; margin-top: var(--space-2); font-size: var(--fs-sm); font-weight: 700; padding: 3px var(--space-3); border-radius: var(--radius-full); }
.kpi__delta--up { color: var(--success); background: var(--success-soft); }
.kpi__delta--down { color: var(--danger); background: var(--danger-soft); }

/* ===== 10. Tarjeta genérica (.card) ===== */
.card {
  padding: var(--space-5);
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: var(--radius);
  box-shadow: var(--shadow-sm);
  margin: var(--space-4) 0;
}
.card h3 { margin-top: 0; }

/* ===== 11. Tablas responsive ===== */
.table-wrap { overflow-x: auto; margin: var(--space-5) 0; border: 1px solid var(--line); border-radius: var(--radius); box-shadow: var(--shadow-xs); }
.table-wrap table { min-width: 480px; }
.table-wrap th, .table-wrap td { padding: var(--space-4); text-align: left; border-bottom: 1px solid var(--line); font-size: var(--fs-sm); }
.table-wrap thead th { background: var(--brand-green); color: #fff; position: sticky; top: 0; font-weight: 700; }
.table-wrap tbody tr:last-child td { border-bottom: none; }
.table-wrap tbody tr:nth-child(even) { background: transparent; } /* sin cebrado: la separación es por hairline, no por color */

/* ===== 12. Barra de progreso (.progress) — píldora fina ===== */
.progress { margin: var(--space-4) 0; }
.progress__track { height: 10px; background: var(--line-strong); border-radius: var(--radius-full); overflow: hidden; }
.progress__fill { height: 100%; background: var(--brand-green); border-radius: var(--radius-full); transition: width .4s var(--ease); width: 0%; }
.progress__label { display: block; margin-top: var(--space-3); font-size: var(--fs-sm); color: var(--ink-soft); }

/* ===== 13. Checklist táctil (.checklist) ===== */
.checklist { list-style: none; padding-left: 0; margin: var(--space-4) 0; }
.checklist li { margin-bottom: var(--space-3); }
.checklist label {
  display: flex;
  align-items: flex-start;
  gap: var(--space-3);
  min-height: var(--tap);
  padding: var(--space-3) var(--space-4);
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: var(--radius-sm);
  box-shadow: var(--shadow-xs);
  cursor: pointer;
  transition: box-shadow var(--dur) var(--ease), border-color var(--dur) var(--ease);
}
.checklist label:hover { border-color: var(--line-strong); box-shadow: var(--shadow-sm); }
.checklist input[type="checkbox"] { width: 26px; height: 26px; flex: 0 0 auto; accent-color: var(--brand-green); margin-top: 2px; }
.checklist input[type="checkbox"]:checked + span { text-decoration: line-through; color: var(--ink-soft); }

/* ===== 14. Etiquetas (.pill) ===== */
.pill {
  display: inline-flex;
  align-items: center;
  padding: 4px var(--space-3);
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
.grid-2, .grid-3 { display: grid; gap: var(--space-5); margin: var(--space-5) 0; grid-template-columns: minmax(0, 1fr); }

/* ===== 16. Gráficos SVG/CSS hechos a mano ===== */
/* Barras horizontales */
.chart-bar-row { display: flex; align-items: center; gap: var(--space-3); margin-bottom: var(--space-3); }
.chart-bar-row__label { flex: 0 0 9rem; font-size: var(--fs-sm); color: var(--ink-soft); }
.chart-bar-row__track { flex: 1 1 auto; height: 16px; background: var(--line-strong); border-radius: var(--radius-full); overflow: hidden; }
.chart-bar-row__fill { height: 100%; background: var(--accent); border-radius: var(--radius-full); transition: width .5s var(--ease); }
.chart-bar-row__value { flex: 0 0 auto; font-size: var(--fs-sm); font-weight: 700; min-width: 3.5rem; text-align: right; }

/* Embudo: cada .funnel-step define su ancho con --w inline, ej. style="--w:70%" */
.funnel { display: flex; flex-direction: column; align-items: center; gap: var(--space-1); margin: var(--space-5) 0; }
.funnel-step {
  width: var(--w, 100%);
  max-width: 100%;
  padding: var(--space-4);
  text-align: center;
  color: #fff;
  font-size: var(--fs-sm);
  font-weight: 700;
  background: var(--accent);
  border-radius: var(--radius-sm);
  transition: opacity var(--dur) var(--ease);
}
.funnel-step:nth-child(2) { opacity: .85; }
.funnel-step:nth-child(3) { opacity: .7; }
.funnel-step:nth-child(4) { opacity: .55; }
.funnel-step:nth-child(5) { opacity: .4; }

/* Línea de tiempo vertical: línea hairline y puntos pequeños */
.timeline { position: relative; margin: var(--space-6) 0; padding-left: var(--space-6); border-left: 1px solid var(--line-strong); }
.timeline-item { position: relative; margin-bottom: var(--space-5); }
.timeline-item::before {
  content: "";
  position: absolute;
  left: calc(-1 * var(--space-6) - 6px);
  top: 4px;
  width: 12px;
  height: 12px;
  border-radius: 50%;
  background: var(--brand-green);
  border: 3px solid var(--paper);
  box-shadow: var(--shadow-xs);
}
.timeline-item__date { font-size: var(--fs-sm); font-weight: 700; color: var(--accent-dark); }
.timeline-item__title { font-family: var(--font-sans); font-weight: 700; font-size: var(--fs-lg); letter-spacing: -.01em; margin: var(--space-1) 0; }

/* ===== 17. Botones: cápsula, con estados sutiles ===== */
.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: var(--space-2);
  min-height: var(--tap);
  padding: 0 var(--space-5);
  border: none;
  border-radius: var(--radius-full);
  background: var(--accent);
  color: #fff;
  font-size: var(--fs-base);
  font-weight: 700;
  text-decoration: none;
  cursor: pointer;
  box-shadow: var(--shadow-xs);
  transition: background var(--dur) var(--ease), transform var(--dur) var(--ease), box-shadow var(--dur) var(--ease);
}
.btn:hover { background: var(--accent-dark); box-shadow: var(--shadow-sm); }
.btn:active { transform: scale(.97); }
.btn--ghost { background: transparent; border: 2px solid var(--line-strong); color: var(--ink); box-shadow: none; }
.btn--ghost:hover { border-color: var(--accent); color: var(--accent); background: var(--accent-soft); }

/* ===== 18. Media queries (mobile-first: base = ~375px) ===== */
@media (min-width: 480px) {
  .kpi-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); }
}
@media (min-width: 640px) {
  .kpi-grid { grid-template-columns: repeat(3, minmax(0, 1fr)); }
  .grid-2 { grid-template-columns: repeat(2, minmax(0, 1fr)); }
  .hero { padding: var(--space-8) var(--space-6); }
}
@media (min-width: 960px) {
  .kpi-grid { grid-template-columns: repeat(4, minmax(0, 1fr)); }
  .grid-2 { grid-template-columns: repeat(2, minmax(0, 1fr)); }
  .grid-3 { grid-template-columns: repeat(3, minmax(0, 1fr)); }
}

/* ===== 19. Movimiento discreto: respeta preferencia de menos movimiento ===== */
@media (prefers-reduced-motion: reduce) {
  html { scroll-behavior: auto; }
  *, *::before, *::after {
    animation-duration: .001ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: .001ms !important;
    scroll-behavior: auto !important;
  }
}

/* ===== 20. Impresión ===== */
@media print {
  .navbar, .navpanel, .copyblock__btn, .btn { display: none !important; }
  body { background: #fff; color: #000; }
  .hero { background: #fff !important; color: #000 !important; }
  .hero h1, .hero p { color: #000 !important; }
  .card, .callout, .kpi, .copyblock { box-shadow: none; border: 1px solid #999; }
  .callout { border-left: 4px solid #999; }
  a[href]::after { content: " (" attr(href) ")"; font-size: .8em; }
}
```

### Notas de uso de componentes

- **`.sec` numeradas automáticamente**: envolver cada sección principal en `<section class="sec"><h2>Título</h2>...</section>`. El número circular aparece solo, vía contador CSS — nunca escribir el número a mano en el `<h2>`.
- **Gráficos (`.chart-bar-row`, `.funnel-step`)**: por defecto pintan con `--accent` (rojo copihue). `.timeline-item::before` (los puntos de la línea de tiempo) es la excepción: pinta con `--brand-green` (verde de marca), como parte del reparto de identidad/estructura. Si un gráfico puntual necesita codificar semántica propia (por ejemplo, el embudo Instagram → Tienda de `estrategia-nucleo.md`, que ya usa rosado para Instagram y verde para Tienda), es válido sobrescribir el color con `style="background:var(--info)"` o similar en ese elemento puntual — la clase base define la forma, no una semántica de color obligatoria.
- **`.grid-2` / `.grid-3`**: 1 columna en móvil siempre; 2 columnas desde 640px; 3 columnas (solo `.grid-3`) desde 960px.

---

## 3. Markup y JS canónicos de navegación (barra superior + panel completo)

Sistema v2 (jul-2026) también reemplaza la navegación: el `.docnav` de una sola fila de 6 links no alcanza para las 15 páginas del sitio. El componente nuevo tiene dos piezas — una **barra superior fija** (`.navbar`) siempre visible, y un **panel completo** (`.navpanel`) que se abre desde ella y agrupa las 15 páginas en 4 grupos (Seguimiento, La estrategia, Plan de acción, Herramientas del día a día). Va como primer elemento dentro de `<body>`, antes del `.hero`.

### Mecanismo para marcar la página actual: un solo atributo

Todo el marcado de abajo (la barra + el panel completo, con sus 15 links) es **idéntico, byte a byte, en las 15 páginas**. Lo único que cambia de una página a otra es un solo atributo en la etiqueta `<body>`:

```html
<body data-nav-actual="cro">
```

El valor es el id de la página (ver tabla de ids más abajo — coincide con el nombre de archivo sin `.html`). El JS canónico (más abajo) lee ese único atributo al cargar la página y, con él, resuelve automáticamente las dos cosas que antes había que marcar a mano en cada página:

1. **El nombre de la página actual en la barra superior** (`<span data-nav-title>`, vacío/genérico en el HTML estático) — el JS lo llena buscando el id en la lista `NAV_PAGES` que vive en el propio script.
2. **Qué link del panel lleva la marca de "estás aquí"** — el JS busca, dentro del panel, el link con `data-nav-key` igual al id, y le agrega la clase `navpanel__link--current` más `aria-current="page"`. Ese link sigue siendo un `<a href>` real: no es un enlace muerto, solo se ve destacado (fondo suave + un check).

Este mecanismo — un solo atributo en `<body>`, cero ediciones dentro del nav — es intencionalmente el más simple y a prueba de errores para propagar a las 15 páginas: se copia el bloque de HTML tal cual, se copia el bloque de JS tal cual, y solo se cambia el valor de `data-nav-actual`. No hay ningún otro lugar del marcado de navegación que edite a mano por página.

**Tabla de ids** (valor exacto de `data-nav-actual` en cada página):

| Grupo | Página | id (`data-nav-actual`) |
|---|---|---|
| Seguimiento | `estado.html` | `estado` |
| Seguimiento | `bitacora.html` | `bitacora` |
| La estrategia | `index.html` | `index` |
| Plan de acción | `plan-90-dias.html` | `plan-90-dias` |
| Plan de acción | `stock-navidad.html` | `stock-navidad` |
| Plan de acción | `ofertas.html` | `ofertas` |
| Plan de acción | `email.html` | `email` |
| Plan de acción | `cro.html` | `cro` |
| Plan de acción | `ads.html` | `ads` |
| Plan de acción | `digitales.html` | `digitales` |
| Herramientas del día a día | `kit-arranque.html` | `kit-arranque` |
| Herramientas del día a día | `guion-reels.html` | `guion-reels` |
| Herramientas del día a día | `sop-dm.html` | `sop-dm` |
| Herramientas del día a día | `recursos.html` | `recursos` |
| Herramientas del día a día | `tablero.html` | `tablero` |

### Por qué el "botón casa" lleva a `estado.html`

El ícono 🦋 de la izquierda de la barra (el "botón casa") apunta a `estado.html`, no a `index.html`. Razón: `index.html` sigue siendo, por razones técnicas de GitHub Pages, el archivo que carga en la raíz del sitio — eso no cambia. Pero como "casa" de navegación (a dónde volver desde cualquier página), `estado.html` — "en qué punto vamos hoy" — cumple mejor ese rol: es la página pensada para volver a mirar cada semana el estado del plan, no para releer la estrategia completa de nuevo cada vez. Por eso también el grupo "Seguimiento" (con `estado.html` primero) encabeza el panel, antes que "La estrategia".

### HTML exacto (barra + panel completo)

Se copia entero, sin editar, en cada una de las 15 páginas — solo cambia `data-nav-actual` en `<body>`:

```html
<body data-nav-actual="__ID_DE_LA_PÁGINA__">

<nav class="navbar" aria-label="Barra de navegación">
  <div class="navbar__inner">
    <a href="estado.html" class="navbar__home" aria-label="Ir al inicio: Estado del plan">🦋</a>
    <span class="navbar__title" data-nav-title>Plan Pedraza Ilustración</span>
    <button type="button" class="navbar__menu-btn" data-nav-open aria-expanded="false" aria-controls="nav-panel">
      <span class="navbar__menu-icon" aria-hidden="true"><span></span><span></span><span></span></span>
      <span class="navbar__menu-label">Menú</span>
    </button>
  </div>
</nav>

<div class="navpanel" id="nav-panel" role="dialog" aria-modal="true" aria-label="Menú de navegación" hidden>
  <div class="navpanel__backdrop" data-nav-close></div>
  <div class="navpanel__sheet">
    <div class="navpanel__header">
      <span class="navpanel__headtitle">Menú</span>
      <button type="button" class="navpanel__close" data-nav-close aria-label="Cerrar menú">✕</button>
    </div>
    <nav class="navpanel__body" aria-label="Todas las páginas del plan">

      <div class="navpanel__group">
        <h3 class="navpanel__group-title">Seguimiento</h3>
        <a href="estado.html" class="navpanel__link" data-nav-key="estado">
          <span class="navpanel__link-text">
            <span class="navpanel__link-name">Estado del plan</span>
            <span class="navpanel__link-desc">En qué punto vamos hoy</span>
          </span>
          <span class="navpanel__check" aria-hidden="true">✓</span>
        </a>
        <a href="bitacora.html" class="navpanel__link" data-nav-key="bitacora">
          <span class="navpanel__link-text">
            <span class="navpanel__link-name">Bitácora</span>
            <span class="navpanel__link-desc">Reuniones, pendientes y entregables</span>
          </span>
          <span class="navpanel__check" aria-hidden="true">✓</span>
        </a>
      </div>

      <div class="navpanel__group">
        <h3 class="navpanel__group-title">La estrategia</h3>
        <a href="index.html" class="navpanel__link" data-nav-key="index">
          <span class="navpanel__link-text">
            <span class="navpanel__link-name">Plan y estrategia</span>
            <span class="navpanel__link-desc">El mapa completo</span>
          </span>
          <span class="navpanel__check" aria-hidden="true">✓</span>
        </a>
      </div>

      <div class="navpanel__group">
        <h3 class="navpanel__group-title">Plan de acción</h3>
        <a href="plan-90-dias.html" class="navpanel__link" data-nav-key="plan-90-dias">
          <span class="navpanel__link-text">
            <span class="navpanel__link-name">Plan de 90 días</span>
            <span class="navpanel__link-desc">Roles, objetivos y checklist</span>
          </span>
          <span class="navpanel__check" aria-hidden="true">✓</span>
        </a>
        <a href="stock-navidad.html" class="navpanel__link" data-nav-key="stock-navidad">
          <span class="navpanel__link-text">
            <span class="navpanel__link-name">Stock para Navidad</span>
            <span class="navpanel__link-desc">Cuánto pedir y cuándo</span>
          </span>
          <span class="navpanel__check" aria-hidden="true">✓</span>
        </a>
        <a href="ofertas.html" class="navpanel__link" data-nav-key="ofertas">
          <span class="navpanel__link-text">
            <span class="navpanel__link-name">Ofertas y pop-ups</span>
            <span class="navpanel__link-desc">Subir el ticket promedio</span>
          </span>
          <span class="navpanel__check" aria-hidden="true">✓</span>
        </a>
        <a href="email.html" class="navpanel__link" data-nav-key="email">
          <span class="navpanel__link-text">
            <span class="navpanel__link-name">Correo y campañas</span>
            <span class="navpanel__link-desc">Del 9% al 20-25%</span>
          </span>
          <span class="navpanel__check" aria-hidden="true">✓</span>
        </a>
        <a href="cro.html" class="navpanel__link" data-nav-key="cro">
          <span class="navpanel__link-text">
            <span class="navpanel__link-name">Conversión</span>
            <span class="navpanel__link-desc">Auditoría de la tienda</span>
          </span>
          <span class="navpanel__check" aria-hidden="true">✓</span>
        </a>
        <a href="ads.html" class="navpanel__link" data-nav-key="ads">
          <span class="navpanel__link-text">
            <span class="navpanel__link-name">Google y Meta Ads</span>
            <span class="navpanel__link-desc">Auditoría de las cuentas</span>
          </span>
          <span class="navpanel__check" aria-hidden="true">✓</span>
        </a>
        <a href="digitales.html" class="navpanel__link" data-nav-key="digitales">
          <span class="navpanel__link-text">
            <span class="navpanel__link-name">Productos digitales</span>
            <span class="navpanel__link-desc">Margen sin stock</span>
          </span>
          <span class="navpanel__check" aria-hidden="true">✓</span>
        </a>
      </div>

      <div class="navpanel__group">
        <h3 class="navpanel__group-title">Herramientas del día a día</h3>
        <a href="kit-arranque.html" class="navpanel__link" data-nav-key="kit-arranque">
          <span class="navpanel__link-text">
            <span class="navpanel__link-name">Kit de arranque</span>
            <span class="navpanel__link-desc">Lo primero que se hace</span>
          </span>
          <span class="navpanel__check" aria-hidden="true">✓</span>
        </a>
        <a href="guion-reels.html" class="navpanel__link" data-nav-key="guion-reels">
          <span class="navpanel__link-text">
            <span class="navpanel__link-name">Guiones de Reels</span>
            <span class="navpanel__link-desc">Qué grabar y cómo</span>
          </span>
          <span class="navpanel__check" aria-hidden="true">✓</span>
        </a>
        <a href="sop-dm.html" class="navpanel__link" data-nav-key="sop-dm">
          <span class="navpanel__link-text">
            <span class="navpanel__link-name">Mensajes y DM</span>
            <span class="navpanel__link-desc">Qué responder</span>
          </span>
          <span class="navpanel__check" aria-hidden="true">✓</span>
        </a>
        <a href="recursos.html" class="navpanel__link" data-nav-key="recursos">
          <span class="navpanel__link-text">
            <span class="navpanel__link-name">Recursos</span>
            <span class="navpanel__link-desc">Herramientas y enlaces</span>
          </span>
          <span class="navpanel__check" aria-hidden="true">✓</span>
        </a>
        <a href="tablero.html" class="navpanel__link" data-nav-key="tablero">
          <span class="navpanel__link-text">
            <span class="navpanel__link-name">Tablero</span>
            <span class="navpanel__link-desc">Métricas semanales</span>
          </span>
          <span class="navpanel__check" aria-hidden="true">✓</span>
        </a>
      </div>

    </nav>
  </div>
</div>
```

### JS exacto (control del panel)

Se copia entero, en un único `<script>` al final del `<body>` — junto al resto del JS de cada página, después del bloque de acceso a `localStorage` si la página lo usa. Todos los nombres de función y variable llevan el prefijo `nav` para no chocar con otros scripts de la página (el del botón Copiar, el de la checklist, etc.):

```html
<script>
  // Navegación global: barra superior + panel completo (15 páginas, 4 grupos).
  // Prefijo "nav" en todo para no chocar con otros scripts de la página.
  var NAV_PAGES = [
    { grupo: 'Seguimiento', id: 'estado', nombre: 'Estado del plan' },
    { grupo: 'Seguimiento', id: 'bitacora', nombre: 'Bitácora' },
    { grupo: 'La estrategia', id: 'index', nombre: 'Plan y estrategia' },
    { grupo: 'Plan de acción', id: 'plan-90-dias', nombre: 'Plan de 90 días' },
    { grupo: 'Plan de acción', id: 'stock-navidad', nombre: 'Stock para Navidad' },
    { grupo: 'Plan de acción', id: 'ofertas', nombre: 'Ofertas y pop-ups' },
    { grupo: 'Plan de acción', id: 'email', nombre: 'Correo y campañas' },
    { grupo: 'Plan de acción', id: 'cro', nombre: 'Conversión' },
    { grupo: 'Plan de acción', id: 'ads', nombre: 'Google y Meta Ads' },
    { grupo: 'Plan de acción', id: 'digitales', nombre: 'Productos digitales' },
    { grupo: 'Herramientas del día a día', id: 'kit-arranque', nombre: 'Kit de arranque' },
    { grupo: 'Herramientas del día a día', id: 'guion-reels', nombre: 'Guiones de Reels' },
    { grupo: 'Herramientas del día a día', id: 'sop-dm', nombre: 'Mensajes y DM' },
    { grupo: 'Herramientas del día a día', id: 'recursos', nombre: 'Recursos' },
    { grupo: 'Herramientas del día a día', id: 'tablero', nombre: 'Tablero' }
  ];

  var navPanelEl, navMenuBtn;

  function navInit() {
    navPanelEl = document.getElementById('nav-panel');
    navMenuBtn = document.querySelector('[data-nav-open]');
    if (!navPanelEl || !navMenuBtn) return;

    var actual = document.body.getAttribute('data-nav-actual') || '';
    var titleEl = document.querySelector('[data-nav-title]');
    var pagina = null;
    for (var i = 0; i < NAV_PAGES.length; i++) {
      if (NAV_PAGES[i].id === actual) { pagina = NAV_PAGES[i]; break; }
    }
    if (titleEl && pagina) { titleEl.textContent = pagina.nombre; }

    var linkActual = navPanelEl.querySelector('[data-nav-key="' + actual + '"]');
    if (linkActual) {
      linkActual.classList.add('navpanel__link--current');
      linkActual.setAttribute('aria-current', 'page');
    }

    navMenuBtn.addEventListener('click', navAbrirPanel);
    navPanelEl.querySelectorAll('[data-nav-close]').forEach(function (el) {
      el.addEventListener('click', navCerrarPanel);
    });
    navPanelEl.querySelectorAll('.navpanel__link').forEach(function (a) {
      a.addEventListener('click', navCerrarPanel);
    });

    document.addEventListener('keydown', function (e) {
      if (!navPanelEl.classList.contains('is-open')) return;
      if (e.key === 'Escape') { navCerrarPanel(); }
      if (e.key === 'Tab') { navAtraparFoco(e); }
    });
  }

  function navAbrirPanel() {
    navPanelEl.hidden = false;
    document.documentElement.classList.add('nav-lock');
    document.body.classList.add('nav-lock');
    navMenuBtn.setAttribute('aria-expanded', 'true');
    requestAnimationFrame(function () {
      navPanelEl.classList.add('is-open');
      var closeBtn = navPanelEl.querySelector('.navpanel__close');
      if (closeBtn) closeBtn.focus();
    });
  }

  function navCerrarPanel() {
    if (!navPanelEl.classList.contains('is-open')) return;
    navPanelEl.classList.remove('is-open');
    document.documentElement.classList.remove('nav-lock');
    document.body.classList.remove('nav-lock');
    navMenuBtn.setAttribute('aria-expanded', 'false');
    navMenuBtn.focus();
    var ocultarAlTerminar = function () {
      navPanelEl.hidden = true;
      navPanelEl.removeEventListener('transitionend', ocultarAlTerminar);
    };
    navPanelEl.addEventListener('transitionend', ocultarAlTerminar);
    setTimeout(ocultarAlTerminar, 300); // respaldo si no hay transición (prefers-reduced-motion)
  }

  function navAtraparFoco(e) {
    var focusables = navPanelEl.querySelectorAll('button, a[href]');
    if (!focusables.length) return;
    var primero = focusables[0];
    var ultimo = focusables[focusables.length - 1];
    if (e.shiftKey && document.activeElement === primero) { e.preventDefault(); ultimo.focus(); }
    else if (!e.shiftKey && document.activeElement === ultimo) { e.preventDefault(); primero.focus(); }
  }

  document.addEventListener('DOMContentLoaded', navInit);
</script>
```

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
<body data-nav-actual="__ID_DE_LA_PÁGINA__">

<!-- === Pegar aquí el HTML exacto de la sección 3 (barra .navbar + panel .navpanel completo) === -->
<!-- Lo único que cambia por página es el valor de data-nav-actual en <body>, arriba. -->

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
  /* === Pegar aquí, en este orden: el JS de navegación (sección 3), el JS del botón Copiar
     (sección 4) y, si aplica, el de la checklist o el del tablero (sección 5-6) === */
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
- [ ] La barra `.navbar` y el panel `.navpanel` son idénticos —mismos 15 links, mismos 4 grupos, mismo orden, mismo texto— en toda página. Lo único que cambia es el atributo `data-nav-actual` en `<body>` (sección 3); el JS se encarga de marcar el nombre en la barra y el link activo del panel.
- [ ] Cero URLs externas en todo el archivo: sin CDNs, sin Google Fonts, sin imágenes remotas, sin `fetch()` a otro dominio que no sea el Google Sheet configurado por el usuario en `tablero.html`.
- [ ] `<html lang="es">`, meta viewport, meta robots y favicon presentes tal cual la plantilla.
- [ ] `<title>` exacto según la tabla de la sección 7.
- [ ] Todo bloque de texto copiable (bio, guion, mensaje de DM, caption) está dentro de un `.copyblock` con botón funcional, y el texto es copy real, sin `[placeholders]`.
- [ ] Si la página usa `localStorage`, respeta el prefijo `pedraza-plan:` y las claves exactas del contrato (sección 5).
- [ ] Las secciones principales están envueltas en `.sec` con `<h2>` (numeración automática, no escrita a mano).
