# martapou.com: instrucciones para Claude

Web/portfolio de **Marta Pou de Avilés** (diseñadora de interacción, Barcelona).
Publicada con **GitHub Pages** desde la rama `main` de este repositorio, con el dominio
**martapou.com** (archivo `CNAME`). Cada push a `main` se publica solo en 1–2 minutos.

Marta prefiere explicaciones sencillas, en castellano, y recibir el trabajo hecho y subido
(no fragmentos de código). Antes de subir, revisa el resultado (capturas en ordenador ~1280px
y en móvil ~390px).

## Cómo está hecha

La web es HTML estático **generado** por un script. No edites a mano los `index.html`:
se sobrescriben en la siguiente generación.

```
_editar/
  build.py         → generador: menú, plantilla, idiomas, portada, resúmenes, aro…
  pages.py         → contenido de cada página en INGLÉS
  pages_es.py      → contenido de cada página en CASTELLANO
  assets/          → style.css, site.js, cursores, favicon (fuente de /assets)
  pages_ocultas.py → (NO está en GitHub, lo guarda Marta) proyectos ocultos
images/            → todas las imágenes (JPG optimizados, máx. 2000 px)
media/             → vídeos propios (fiat-lux-maqueta.mp4)
<Proyecto>/index.html, es/<Proyecto>/index.html, index.html, es/index.html → GENERADOS
```

Para regenerar la web después de cualquier cambio:

```bash
python3 _editar/build.py
```

Luego `git add -A && git commit && git push`.

## Contenido

- En `pages.py` / `pages_es.py`, cada página es `page(slug, título, html)`.
  - Imágenes: `<img width="W" height="H" data-src="IMG:nombre.jpg">` (archivo en `images/`).
    También existe la forma antigua `data-src="F/<hash>/<nombre>"` (imágenes que venían de Cargo).
  - Slideshow: `<div class="image-gallery" data-transition="fade|slide">…imgs…</div>`.
  - Vídeo de YouTube: una línea `YT:https://www.youtube.com/embed/ID`.
    Vimeo: `<div class="video"><iframe src="https://player.vimeo.com/video/ID?h=HASH"></iframe></div>`.
    El script los convierte en el reproductor propio (autoplay sin sonido al estar entero en
    pantalla, sin rótulos de YouTube/Vimeo, botones de pausa y sonido al pasar el ratón).
  - Enlace a otra página de la web: `href="PAGE:slug"`.
  - Columnas: `<div grid-row><div grid-col>…</div><div grid-col>…</div></div>`.
- Menú de proyectos: listas `NAV_INTERACTIVE` (y su traducción `NAV_ES`) en `build.py`.
- Resumen amarillo al pasar el ratón: diccionario `TIPS` en `build.py` (en / es).
- Portada (columna de fotos con scroll infinito): lista `HOME` al final de `pages.py`.
- Proyectos ocultos: conjunto `ILLU` en `build.py`. Para volver a publicar uno, quítalo de
  `ILLU` (necesita `pages_ocultas.py`, que Marta tiene en su copia privada).
- Info: la página publicada es `Info`. `Info-a` … `Info-f` son propuestas de diseño
  pendientes de elegir (no enlazadas desde el menú).

## Diseño (no romper sin preguntar)

- Fondo negro, texto blanco, lila `#a76ded`, amarillo `#f7e61c`, naranja `#ff4a00` para el
  proyecto activo. Títulos en Instrument Serif; texto en Helvetica Neue.
- Ordenador: columna izquierda fija (nombre "Marta / Pou de Avilés" que ocupa todo el ancho,
  Projects, bloque "Hi! Nice to meet you + Read more" abajo alineado con EN / ES).
- Portada: fotos a sangre por la derecha con scroll automático infinito que no se para,
  aro giratorio "MOVEMENT · INTERACTION · LIGHT · SOUND", EN / ES con mezcla para verse
  sobre fotos claras.
- Móvil: barra inferior (portada: … índice · About me · EN/ES; páginas: ← · About me · EN/ES),
  nombre fijo arriba en la portada, páginas de proyecto sin cabecera.
- Cursor amarillo (PNG) y manita amarilla en enlaces.
- Tras cambiar `style.css` o `site.js`, el generador añade `?v=<hash>` a las rutas, así los
  navegadores no usan versiones antiguas. Si cambias un cursor u otra imagen de `assets/`,
  cámbiale el nombre al archivo.

## Dominio

DNS en Namecheap: 4 registros A para `@` (185.199.108.153, 185.199.109.153,
185.199.110.153, 185.199.111.153) y CNAME `www` → `mpoudeaviles.github.io`.
