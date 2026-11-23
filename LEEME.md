# martapou.com en GitHub Pages (gratis)

Esta carpeta es tu portfolio entero, sin Cargo: HTML + CSS + un poco de JS.
La estructura de direcciones es la misma que antes (`martapou.com/Marisa`, `martapou.com/Info`…),
así que los enlaces que ya tengas compartidos siguen funcionando.

```
index.html            → portada en inglés (columna de imágenes que baja sola)
Marisa/index.html     → una carpeta por proyecto (inglés)
Info/index.html
es/                   → la misma web en castellano (es/Marisa/, es/Info/…)
assets/style.css      → colores, tipografías, tamaños
assets/site.js        → slideshows, menú móvil, scroll de la portada
images/  media/       → imágenes y vídeo (se llenan con el paso 1)
CNAME                 → le dice a GitHub que la web es martapou.com
```

---

## 1. Descargar las imágenes (antes de cancelar Cargo)

1. Haz **clic derecho → Abrir** sobre `descargar-imagenes.command` (la primera vez macOS
   pide confirmar porque el archivo viene de internet).
2. Se abre el Terminal, descarga ~150 imágenes y el vídeo de Fiat Lux, y reduce las
   más grandes a 2400 px para que la web cargue rápido. Tarda unos minutos.
3. Si sale algún fallo, ábrelo otra vez: solo baja lo que falte.

Para ver la web en tu ordenador antes de subirla, abre `index.html` con el navegador.

## 2. Subirla a GitHub

1. Crea una cuenta en <https://github.com> (si no tienes).
2. Crea un repositorio nuevo **público** llamado, por ejemplo, `martapou-web`
   (botón **New** arriba a la izquierda). No marques nada más.
3. En el repositorio vacío, pulsa **uploading an existing file** y arrastra **todo el
   contenido** de esta carpeta (no la carpeta en sí: lo de dentro).
   - GitHub web sube hasta 100 archivos por tanda: si no caben, sube primero todo menos
     `images`, y luego la carpeta `images` en una o dos tandas.
   - Alternativa más cómoda: la app **GitHub Desktop**, que sube la carpeta de una vez.
4. Pulsa **Commit changes**.
5. Ve a **Settings → Pages**. En *Source* elige **Deploy from a branch**,
   rama **main**, carpeta **/ (root)** → **Save**.
6. En la misma página, en *Custom domain* escribe `martapou.com` → **Save**.

En un par de minutos la web estará en `https://TU-USUARIO.github.io/martapou-web/`
(ahí puede verse sin estilos hasta que conectes el dominio; es normal).

## 3. Apuntar tu dominio a GitHub

Entra en el panel de quien te cobra el dominio (GoDaddy, Namecheap, Dinahosting…),
sección **DNS**, y:

1. **Borra** los registros que apuntan a Cargo (A o CNAME de `@` y `www`).
2. Crea **4 registros A** para `@` (el dominio raíz):
   ```
   185.199.108.153
   185.199.109.153
   185.199.110.153
   185.199.111.153
   ```
3. Crea un registro **CNAME** para `www` → `TU-USUARIO.github.io`
4. Espera (normalmente minutos; como mucho 24 h). Vuelve a **Settings → Pages** y
   activa **Enforce HTTPS** cuando GitHub lo permita.

Cuando `martapou.com` ya cargue la versión nueva, ya puedes cancelar Cargo.

## 4. Editar la web en el futuro

- **Textos**: recuerda que cada proyecto tiene dos versiones: `Marisa/index.html` (inglés)
  y `es/Marisa/index.html` (castellano). Abre el `index.html` de la carpeta del proyecto (con TextEdit o VS Code)
  y cambia el texto. En GitHub también puedes editar directamente con el lápiz ✏️.
- **Imagen nueva**: súbela a `images/` y añade `<img src="../images/nombre.jpg" alt="">`.
- **Colores / tipografía**: arriba del todo en `assets/style.css`.
- Cada cambio que subas a GitHub se publica solo en 1–2 minutos.

### Tipografía
Cargo usaba *Sprat Condensed*, que es de pago y no se puede sacar de Cargo.
Aquí se usa **Instrument Serif** (gratuita, de Google Fonts), muy parecida.
Si compras la licencia de Sprat, pon los archivos en `assets/fonts/` y descomenta
el bloque del principio de `style.css`.
