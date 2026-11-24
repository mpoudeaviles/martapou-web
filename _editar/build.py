# -*- coding: utf-8 -*-
"""Genera la web estática de martapou.com a partir de pages.py."""
import os, re, shutil, html, stat, zipfile, hashlib
from pages import PAGES, HOME, VIDEOS
from pages_es import ES
try:  # contenido de los proyectos ocultos (solo para la copia privada)
    import pages_ocultas
    pages_ocultas.add(PAGES, ES)
except ImportError:
    pass

ARCHIVE = bool(os.environ.get("ARCHIVE"))   # True = versión completa con ilustración (solo para guardar)
HERE = os.path.dirname(os.path.abspath(__file__))
# la web se genera en la carpeta de arriba (la raíz del repositorio)
OUT = os.path.join(HERE, "..", "archivo-ilustracion") if ARCHIVE else os.path.join(HERE, "..")
# proyectos ocultos: no salen en la web (su contenido está en pages_ocultas.py, que no se publica)
ILLU = {"Wallart-for-MCB", "Sour-Candy", "Suspiria", "Alix-y-Jonah-art", "Design-for-Cataris-by-Marisol",
        "Mood-project", "Alix-y-Jonah"}
FREIGHT = "https://freight.cargo.site/t/original/i/"
DOMAIN = "martapou.com"
SITE_NAME = "Marta Pou de Avilés"
DESC = "Marta Pou de Avilés — interactive designer based in Barcelona. Interactive installations, light and creative technology."

downloads = {}   # local filename -> url

def img_local(ref):
    # ref = F/<hash>/<name>
    _, h, name = ref.split("/", 2)
    local = f"{h[:8]}-{name}"
    downloads[local] = FREIGHT + h + "/" + name
    # en la web se usan versiones optimizadas en JPG
    return re.sub(r"\.(png|jpe?g)$", ".jpg", local, flags=re.I)

NAV_INTERACTIVE = [
    ("Marisa", "Marisa"), ("no_res", "no_res"),
    ("A-Dialogue-with-Light-by-Antoni-Arola-copy", "A Dialogue With Light by Antoni Arola"),
    ("Fiat-Lux-Zaragoza-by-Antoni-Arola", "Fiat Lux by Antoni Arola"),
    ("What-Streaming-Reflects", "What Streaming Reflects"), ("Put", "PUT*"),
    ("Byte-sleeve", "Byte Sleeve"), ("Oscilloscope-game", "Oscilloscope Game"),
    ("Alix-y-Jonah", "Alix &amp; Jonah (Game)"),
]
NAV_ILLUSTRATION = [
    ("Wallart-for-MCB", "Wall art for MCB"), ("Sour-Candy", "Sour Candy"),
    ("Suspiria", "L’Ombre de l’Opera"), ("Alix-y-Jonah-art", "Alix &amp; Jonah (Art)"),
    ("Design-for-Cataris-by-Marisol", "Design for Catarsis by Marisol"),
    ("Mood-project", "Mood project"),
]

ICON_IG = '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5" fill="none" stroke="currentColor" stroke-width="2"/><circle cx="12" cy="12" r="4" fill="none" stroke="currentColor" stroke-width="2"/><circle cx="17.5" cy="6.5" r="1.3" fill="currentColor"/></svg>'
ICON_IN = '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="2" fill="none" stroke="currentColor" stroke-width="2"/><path d="M7.5 10v6.5M7.5 7.3v.2M11 16.5V10m0 3c0-2 1.2-3 2.6-3s2.4.9 2.4 3v3.5" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round"/></svg>'


def link(prefix, slug):
    return f"{prefix}{slug}/"


TXT = {
    "en": {"about": "About me", "interactive": "Projects", "illustration": "Illustration", "hi": "<b>Hi!</b> Nice to meet you",
           "intro": "I’m Marta, an interaction designer based in Barcelona.", "more": "Read more",
           "menu": "Menu", "close": "Close"},
    "es": {"about": "Sobre mí", "interactive": "Proyectos", "illustration": "Ilustración", "hi": "<b>¡Hola!</b> Encantada de conocerte",
           "intro": "Soy Marta, diseñadora de interacción en Barcelona.", "more": "Leer más",
           "menu": "Menú", "close": "Cerrar"},
}
NAV_ES = {"Alix-y-Jonah": "Alix &amp; Jonah (Juego)", "Wallart-for-MCB": "Mural para el MCB",
          "Alix-y-Jonah-art": "Alix &amp; Jonah (Arte)", "Design-for-Cataris-by-Marisol": "Diseño para Catarsis de Marisol",
          "Mood-project": "Proyecto Mood", "A-Dialogue-with-Light-by-Antoni-Arola-copy": "A Dialogue With Light de Antoni Arola",
          "Fiat-Lux-Zaragoza-by-Antoni-Arola": "Fiat Lux de Antoni Arola"}


TIPS = {
    "en": {"Marisa": "critical object", "no_res": "reactive installation",
           "A-Dialogue-with-Light-by-Antoni-Arola-copy": "light art installation",
           "Fiat-Lux-Zaragoza-by-Antoni-Arola": "light art installation",
           "What-Streaming-Reflects": "art intervention", "Put": "critical object",
           "Byte-sleeve": "wearable", "Oscilloscope-game": "escape room game",
           "Alix-y-Jonah": "interactive game"},
    "es": {"Marisa": "objeto crítico", "no_res": "instalación reactiva",
           "A-Dialogue-with-Light-by-Antoni-Arola-copy": "instalación de arte lumínico",
           "Fiat-Lux-Zaragoza-by-Antoni-Arola": "instalación de arte lumínico",
           "What-Streaming-Reflects": "intervención artística", "Put": "objeto crítico",
           "Byte-sleeve": "wearable", "Oscilloscope-game": "juego para escape room",
           "Alix-y-Jonah": "juego interactivo"},
}


def tip(lang, slug):
    t = TIPS[lang].get(slug)
    return f' data-tip="{t}"' if t else ""


def nav_html(prefix, current, lang="en", switch=""):
    t = TXT[lang]
    ILLU_BLOCK = ""
    def items(lst):
        out = []
        for slug, label in lst:
            if slug in ILLU and not ARCHIVE:
                continue
            if lang == "es": label = NAV_ES.get(slug, label)
            cls = ' class="active"' if slug == current else ""
            out.append(f'<li><a href="{link(prefix, slug)}"{cls}{tip(lang, slug)}>{label}</a></li>')
        return "\n".join(out)
    if ARCHIVE:
        ILLU_BLOCK = f"    <h1>{t['illustration']}</h1>\n    <ol>\n{items(NAV_ILLUSTRATION)}\n    </ol>\n"
    return f'''<nav class="side-nav" id="side-nav">
  <h2 class="site-title"><a href="{link(prefix, 'Info') if current == '' else (prefix or './')}"><span class="t1">Marta</span> <span class="t2">Pou de Avilés</span></a></h2>
  <button class="menu-toggle" aria-expanded="false" aria-controls="nav-lists" data-close="{t['close']}">{t['menu']}</button>
  <div class="nav-lists" id="nav-lists">
    <h1>{t['interactive']}</h1>
    <ol>
{items(NAV_INTERACTIVE)}
    </ol>
{ILLU_BLOCK}    <div class="nav-foot">
      <a href="{link(prefix, 'Info')}" class="about-link">
        <span class="hi">{t['hi']}</span>
        <span class="intro">{t['intro']}</span>
        <span class="more">{t['more']} <span class="arrow">→</span></span>
      </a>
      <div class="social">
        <a href="https://www.instagram.com/marta.pout/" target="_blank" rel="noopener" aria-label="Instagram">{ICON_IG}</a>
        <a href="https://www.linkedin.com/in/marta-pou-de-avil%C3%A9s-tarragona-5109921a4/" target="_blank" rel="noopener" aria-label="LinkedIn">{ICON_IN}</a>
      </div>
    </div>
  </div>
</nav>
<div class="lang-switch">{switch}</div>
<div class="m-bar">
  <a class="m-back" href="{prefix or './'}" aria-label="Home">←</a>
  <button class="m-index" aria-label="Index" aria-expanded="false">…</button>
  <a class="m-about" href="{link(prefix, 'Info')}">{t['about']}</a>
</div>
<div class="top-links">
  <a href="{link(prefix, 'Info')}">Info</a>
  <a href="https://www.instagram.com/marta.pout/" target="_blank" rel="noopener">Instagram</a>
</div>'''


def convert(content, prefix, lp=None):
    lp = prefix if lp is None else lp
    # YouTube
    # vídeos de YouTube y Vimeo -> reproductor propio (autoplay al verlo, sin sonido, botón de sonido)
    content = re.sub(r"YT:https://www\.youtube\.com/embed/([\w-]+)\S*",
                     lambda m: f'<div class="video" data-yt="{m.group(1)}"></div>', content)
    content = re.sub(r'<div class="video"><iframe src="https://player\.vimeo\.com/video/(\d+)(?:\?h=(\w+))?[^"]*"[^>]*></iframe></div>',
                     lambda m: f'<div class="video" data-vimeo="{m.group(1)}"' + (f' data-h="{m.group(2)}"' if m.group(2) else '') + '></div>', content)
    # internal links
    content = re.sub(r'href="PAGE:([^"]+)"', lambda m: f'href="{link(lp, m.group(1))}"', content)
    # images
    def img(m):
        local = img_local(m.group(1))
        return f'src="{prefix}images/{local}" loading="lazy" alt=""'
    content = re.sub(r'data-src="(F/[^"]+)"', img, content)
    content = re.sub(r'data-src="IMG:([^"]+)"', lambda m: f'src="{prefix}images/{m.group(1)}" loading="lazy" alt=""', content)
    # videos
    content = re.sub(r'src="VIDEO:([^"]+)"', lambda m: f'src="{prefix}media/{m.group(1)}"', content)
    return content


def asset_version():
    h = hashlib.md5()
    for f in ("style.css", "site.js"):
        h.update(open(os.path.join(os.path.dirname(__file__), "assets", f), "rb").read())
    return h.hexdigest()[:8]
V = asset_version()


def page_html(title, body, prefix, current, body_class="", lang="en", switch="", alt="", lp=None):
    full_title = SITE_NAME if not title else f"{title} - {SITE_NAME}"
    return f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(full_title, quote=False)}</title>
<meta name="description" content="{DESC}">
<meta property="og:title" content="{html.escape(full_title)}">
<meta property="og:description" content="{DESC}">
<meta property="og:type" content="website">
{alt}
<link rel="icon" href="{prefix}assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://www.youtube.com">
<link rel="preconnect" href="https://i.ytimg.com">
<link rel="preconnect" href="https://player.vimeo.com">
<link rel="preconnect" href="https://i.vimeocdn.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Instrument+Serif&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{prefix}assets/style.css?v={V}">
</head>
<body class="{body_class}">
{nav_html(lp if lp is not None else prefix, current, lang, switch)}
<main class="content">
{body}
</main>
<script src="{prefix}assets/site.js?v={V}"></script>
</body>
</html>
'''


def write(path, text):
    full = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(text)


def main():
    if ARCHIVE:
        if os.path.exists(OUT):
            shutil.rmtree(OUT)
        os.makedirs(OUT)
    else:
        # borrar páginas de proyectos ocultos que pudieran quedar publicadas
        for sl in ILLU:
            for d in (sl, os.path.join("es", sl)):
                if os.path.isdir(os.path.join(OUT, d)):
                    shutil.rmtree(os.path.join(OUT, d))

    en_html = {p["slug"]: p["html"] for p in PAGES}
    m = re.search(r'<div class="image-gallery".*?</div>', en_html.get("Mood-project", ""), re.S)
    mood_gallery = m.group(0) if m else ""
    view_all_es = en_html["View-all"].replace("<h1>View all</h1>", "<h1>Ver todo</h1>")

    def switch(lang, to_en, to_es):
        en = f'<a href="{to_en}"' + (' class="on"' if lang == "en" else '') + '>EN</a>'
        es = f'<a href="{to_es}"' + (' class="on"' if lang == "es" else '') + '>ES</a>'
        return en + " / " + es

    def alt(to_en, to_es):
        return (f'<link rel="alternate" hreflang="en" href="https://{DOMAIN}/{to_en}">\n'
                f'<link rel="alternate" hreflang="es" href="https://{DOMAIN}/{to_es}">')

    # páginas de proyecto: /<slug>/ (inglés) y /es/<slug>/ (castellano)
    def public(h):
        if ARCHIVE:
            return h
        # View all: quitar miniaturas de ilustración
        for sl in ILLU:
            h = re.sub(r'<a href="PAGE:' + re.escape(sl) + r'"[^>]*><img[^>]*></a>\n?', '', h)
        # Alix & Jonah: quitar la frase que enlaza a las ilustraciones
        h = re.sub(r" If you want to take a better look to the illustrations.*?</b>\.(&nbsp;)?", "", h)
        h = re.sub(r" If you want to take a better look at the illustrations.*?</b>\.(&nbsp;)?", "", h)
        h = re.sub(r" Si quieres verlas mejor, pincha.*?</b>\.", "", h)
        return h

    for p in PAGES:
        slug = p["slug"]
        if slug in ILLU and not ARCHIVE:
            continue
        if slug not in ES:
            continue
        cls = "page-info" if slug == "Info" else "page-project"
        a = alt(f"{slug}/", f"es/{slug}/")
        # EN
        body = '<div class="bodycopy">' + convert(public(p["html"]), "../") + "</div>"
        write(f"{slug}/index.html", page_html(p["title"], body, "../", slug, cls, "en",
              switch("en", "./", f"../es/{slug}/"), a))
        # ES
        es = ES[slug]
        h = public(es["html"].replace("MOOD_GALLERY", mood_gallery).replace("VIEW_ALL", view_all_es))
        body = '<div class="bodycopy">' + convert(h, "../../", "../") + "</div>"
        write(f"es/{slug}/index.html", page_html(es["title"], body, "../../", slug, cls, "es",
              switch("es", f"../../{slug}/", "./"), a, lp="../"))

    # portada (EN en /, ES en /es/)
    def ring(lang):
        words = (["MOVEMENT", "INTERACTION", "LIGHT", "SOUND"] if lang == "en"
                 else ["MOVIMIENTO", "INTERACCIÓN", "LUZ", "SONIDO"])
        spans = "".join(f'<tspan class="{"w" if i % 2 == 0 else "y"}">{w}</tspan><tspan class="w"> · </tspan>' for i, w in enumerate(words))
        r = 96
        circ = round(2 * 3.14159 * r) - 4
        fs = 25 if lang == "en" else 25
        return ('<div class="ring" aria-hidden="true"><svg viewBox="0 0 240 240">'
                f'<defs><path id="ringpath" d="M 120,120 m -{r},0 a {r},{r} 0 1,1 {2*r},0 a {r},{r} 0 1,1 -{2*r},0"/></defs>'
                f'<circle cx="120" cy="120" r="{r}" fill="none" stroke="#000" stroke-width="{fs + 15}"/>'
                f'<text dy="{round(fs * 0.36, 1)}" style="font-size:{fs}px"><textPath href="#ringpath" textLength="{circ}" lengthAdjust="spacing">{spans}</textPath></text>'
                '</svg></div>')

    def sticker(lang, asset):
        if lang == "en":
            return f'<img class="sticker" src="{asset}assets/sticker-en.png" alt="Click on any image to know more!">'
        return f'<img class="sticker" src="{asset}assets/sticker-es.svg" alt="¡Haz clic en cualquier imagen para saber más!">'

    def home(asset, lp, lang="en"):
        items = []
        for slug, w, h, ref in HOME:
            if slug in ILLU and not ARCHIVE:
                continue
            local = img_local(ref)
            items.append(f'<a href="{lp}{slug}/" class="image-link"{tip(lang, slug)}><img src="{asset}images/{local}" width="{w}" height="{h}" alt="" loading="lazy"></a>')
        return ('<div class="home-scroll" id="home-scroll">\n' + "\n".join(items) + "\n</div>\n"
                + ring(lang))
    a = alt("", "es/")
    write("index.html", page_html("", home("", "", "en"), "", "", "page-home", "en", switch("en", "./", "es/"), a))
    write("es/index.html", page_html("", home("../", "", "es"), "../", "", "page-home", "es", switch("es", "../", "./"), a, lp=""))

    # 404 (absolute paths so it works at any depth)
    nf = page_html("Not found", '<div class="bodycopy"><h1>Page not found</h1><p><a href="/">Back to home</a></p></div>', "/", "", "page-project")
    write("404.html", nf)

    # assets
    here = HERE
    os.makedirs(os.path.join(OUT, "assets"), exist_ok=True)
    for f in ("style.css", "site.js", "favicon.svg", "sticker-en.png", "sticker-es.svg", "cursor-a.png", "cursor-a@2x.png", "cursor-h.png", "cursor-h@2x.png"):
        shutil.copy(os.path.join(here, "assets", f), os.path.join(OUT, "assets", f))

    # redirección de la antigua URL de la portada de Cargo
    write("Home-Image-Scroll/index.html", '<!DOCTYPE html><meta charset="utf-8"><meta http-equiv="refresh" content="0; url=../"><link rel="canonical" href="../"><a href="../">Marta Pou de Avilés</a>')
    write("CNAME", DOMAIN + "\n")
    write(".nojekyll", "")
    print(f"Web generada: {2*(len(PAGES)+1)} páginas")


if __name__ == "__main__":
    main()
