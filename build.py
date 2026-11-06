#!/usr/bin/env python3
"""
MARTIUS TATTOO STUDIO — generatore del sito statico.

Modifica i DATI DELLO STUDIO qui sotto e lancia:
    python3 build.py
Verranno rigenerate tutte le pagine .html nella stessa cartella.
"""
from pathlib import Path
from urllib.parse import quote_plus

# =====================================================================
# DATI DELLO STUDIO  (i valori segnati SEGNAPOSTO vanno sostituiti)
# =====================================================================
STUDIO = "Martius"
CITY = "Città di Castello"
ADDRESS_1 = "Centro Storico"                    # SEGNAPOSTO: via e numero civico
ADDRESS_2 = "06012 Città di Castello (PG)"
MAP_QUERY = "Città di Castello PG"              # SEGNAPOSTO: metti l'indirizzo completo
PHONE = "+39 333 860 3900"
WHATSAPP = "393338603900"                       # solo cifre, con 39
EMAIL = "info@martiustattoo.it"                 # SEGNAPOSTO
HOURS_SHORT = "Mar – Ven 14:30 – 20:00"
HOURS_TIME = "Sab 10:30 – 19:00"
INSTAGRAM = "https://www.instagram.com/martius_tattoo_studio/"
FACEBOOK = "#"                                  # SEGNAPOSTO
TIKTOK = "#"                                    # SEGNAPOSTO

# Artisti: (nome, stili, tag, foto, bio, instagram)
ARTISTS = [
    ("MARTIUS", "Owner | Tattoo Artist", ["Owner", "Tattoo", "Progetti custom"], "img/martius-owner.jpg",
     "Owner e resident artist, fondatrice dello studio. Segue ogni progetto dalla consulenza al disegno finale, per un tatuaggio unico e fatto su misura.",
     "https://www.instagram.com/martius_tattooart/"),
    ("LORENZO", "Lorenzo Giornelli | Tattoo Artist", ["Tattoo", "Custom", "Flash"], "img/lorenzo-giornelli.jpg",
     "Tatuatore del team Martius: porta la tua idea e la trasformerà in un disegno pensato per te.",
     "https://www.instagram.com/lorenzogiornellitattoo/"),
    ("RORO", "Body Art | Piercing", ["Body Art", "Piercing", "Gioielli"], "img/piercing-in-studio.jpg",
     "Body art e piercing: foratura con ago sterile monouso e gioielli di qualità per una guarigione sicura.",
     "https://www.instagram.com/roro_bodyart/"),
]

# Foto dello studio (cartella img/)
IMG_HERO = "img/martius-al-lavoro.jpg"
IMG_TATTOO = "img/leone-spalla.jpg"
IMG_PIERCING = "img/piercing-smiley.jpg"
IMG_STUDIO = "img/piercing-in-studio.jpg"
IMG_EVENT = "img/schiena-samurai-2.jpg"
GALLERY = [
    ("img/schiena-samurai.jpg", "black-grey realistico", "Schiena completa: samurai e Poseidone"),
    ("img/leone-spalla.jpg", "black-grey realistico", "Leone realistico sulla spalla"),
    ("img/angelo-realistico.jpg", "black-grey realistico", "Angelo e rosa realistici sull'avambraccio"),
    ("img/piercing-smiley.jpg", "piercing", "Piercing smiley"),
    ("img/martius-al-lavoro.jpg", "studio", "Martius al lavoro in studio"),
    ("img/leone-spalla-2.jpg", "black-grey realistico", "Leone realistico, vista laterale"),
    ("img/piercing-in-studio.jpg", "piercing studio", "Piercing al labbro in studio"),
    ("img/lorenzo-giornelli.jpg", "studio", "Lorenzo Giornelli al lavoro"),
    ("img/hannya-colore.jpg", "colore", "Maschera hannya a colori con fiori di ciliegio"),
    ("img/lupo-realistico.jpg", "black-grey realistico", "Lupo realistico sull'avambraccio"),
    ("img/piercing-orecchio.jpg", "piercing", "Piercing multipli all'orecchio"),
    ("img/tigre-clessidra.jpg", "colore", "Tigre e clessidra a colori"),
    ("img/manica-rosso-nero.jpg", "colore", "Manica rosso e nero"),
    ("img/fine-line-orecchio.jpg", "fine-line piercing", "Fine line floreale sull'orecchio con piercing"),
    ("img/piercing-orecchio-lavoro.jpg", "piercing studio", "Piercing all'orecchio in studio"),
    ("img/hannya-colore-2.jpg", "colore", "Maschera hannya, dettaglio"),
]

# Immagini HERO (a tutto schermo, foto libere Unsplash in stile scuro/caldo).
# Per usare una vostra foto scrivi "img/nomefile.jpg".
HERO = {
    "home": "img/hero-home.jpg",       # mano con guanto nero che tatua
    "artisti": "img/hero-artisti.jpg",    # tatuatore al lavoro
    "cover": "img/hero-cover.jpg",      # schiena tatuata, luce calda
    "piercing": "img/hero-piercing.jpg",   # gioielli dorati in ombra
    "flash": "img/hero-flash.jpg",         # floreale black & grey
    "eventi": "img/hero-eventi.jpg",     # luci al neon
    "aftercare": "img/hero-aftercare.jpg",  # tatuaggio floreale sulla spalla
    "contatti": "img/hero-contatti.jpg",   # interno studio, luci calde
}

# =====================================================================

OUT = Path(__file__).parent


def img(pid, w=1200):
    # Foto locali: metti il file in img/ e scrivi qui "img/nomefile.jpg"
    if pid.startswith("img/"):
        return pid
    return f"https://images.unsplash.com/photo-{pid}?auto=format&fit=crop&w={w}&q=75"


MAP_EMBED = f"https://maps.google.com/maps?q={quote_plus(MAP_QUERY)}&z=15&output=embed"
MAP_DIR = f"https://www.google.com/maps/dir/?api=1&destination={quote_plus(MAP_QUERY)}"
TEL = "tel:" + PHONE.replace(" ", "")

MENU = [
    ("index.html", "Home"),
    ("artisti.html", "Artisti"),
    ("cover-up.html", "Cover-up e Restauro"),
    ("piercing.html", "Piercing e Gioielli"),
    ("flash.html", "Flash settimanali da 50€"),
    ("eventi.html", "Eventi Flash e Piercing da 20€"),
    ("aftercare.html", "Cura post-tatuaggio"),
    ("contatti.html", "Contatti"),
]

# ------------------------------ Icone ------------------------------
I = {
    "pin": '<svg viewBox="0 0 24 24"><path d="M12 2a7 7 0 0 0-7 7c0 5.2 7 13 7 13s7-7.8 7-13a7 7 0 0 0-7-7zm0 9.5A2.5 2.5 0 1 1 12 6a2.5 2.5 0 0 1 0 5.5z"/></svg>',
    "clock": '<svg viewBox="0 0 24 24"><path d="M12 2a10 10 0 1 0 0 20 10 10 0 0 0 0-20zm1 10.6 3.5 2.1-.8 1.3L11 13V7h2z"/></svg>',
    "shield": '<svg viewBox="0 0 24 24"><path d="M12 2 4 5v6c0 5 3.4 9.7 8 11 4.6-1.3 8-6 8-11V5zm-1.2 14.2-3.5-3.5 1.4-1.4 2.1 2.1 4.9-4.9 1.4 1.4z"/></svg>',
    "phone": '<svg viewBox="0 0 24 24"><path d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.25 11.4 11.4 0 0 0 3.6.57 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1c0 1.25.2 2.45.57 3.57a1 1 0 0 1-.25 1z"/></svg>',
    "mail": '<svg viewBox="0 0 24 24"><path d="M20 4H4a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V6a2 2 0 0 0-2-2zm0 4-8 5-8-5V6l8 5 8-5z"/></svg>',
    "ig": '<svg viewBox="0 0 24 24"><path d="M12 7a5 5 0 1 0 0 10 5 5 0 0 0 0-10zm0 8.2a3.2 3.2 0 1 1 0-6.4 3.2 3.2 0 0 1 0 6.4zM17.3 5.5a1.2 1.2 0 1 0 0 2.4 1.2 1.2 0 0 0 0-2.4zM12 2c-2.7 0-3 0-4.1.06C4.3 2.2 2.2 4.3 2.06 7.9 2 9 2 9.3 2 12s0 3 .06 4.1c.16 3.6 2.24 5.7 5.84 5.84C9 22 9.3 22 12 22s3 0 4.1-.06c3.6-.16 5.7-2.24 5.84-5.84C22 15 22 14.7 22 12s0-3-.06-4.1C21.8 4.3 19.7 2.2 16.1 2.06 15 2 14.7 2 12 2zm0 1.8c2.67 0 2.98 0 4.04.06 2.7.12 3.97 1.4 4.1 4.1.05 1.05.06 1.37.06 4.04s0 2.98-.06 4.04c-.13 2.7-1.4 3.97-4.1 4.1-1.06.05-1.37.06-4.04.06s-2.98 0-4.04-.06c-2.7-.13-3.97-1.4-4.1-4.1C3.8 14.98 3.8 14.67 3.8 12s0-2.98.06-4.04c.13-2.7 1.4-3.97 4.1-4.1C9.02 3.8 9.33 3.8 12 3.8z"/></svg>',
    "fb": '<svg viewBox="0 0 24 24"><path d="M14 8V6.2c0-.8.2-1.2 1.4-1.2H17V2h-2.6C11.3 2 10 3.5 10 6v2H8v3h2v11h4V11h2.6l.4-3z"/></svg>',
    "tt": '<svg viewBox="0 0 24 24"><path d="M16.6 2h-3.3v13.4a2.9 2.9 0 1 1-2-2.75V9.3a6.2 6.2 0 1 0 5.3 6.1V8.6a7.6 7.6 0 0 0 4.4 1.4V6.7a4.4 4.4 0 0 1-4.4-4.7z"/></svg>',
    "wa": '<svg viewBox="0 0 24 24"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm5.3 14.1c-.2.6-1.3 1.2-1.8 1.2-.5.1-1 .1-3.3-.8-2.8-1.2-4.6-4-4.7-4.2-.1-.2-1.1-1.5-1.1-2.9s.7-2 1-2.3c.2-.3.5-.3.7-.3h.5c.2 0 .4 0 .6.5l.9 2.1c.1.2.1.4 0 .5l-.3.5-.4.5c-.1.1-.3.3-.1.6.2.3.8 1.3 1.7 2.1 1.2 1 2.1 1.4 2.4 1.5.3.1.5.1.6-.1l.9-1.1c.2-.3.4-.2.7-.1l2 1c.3.1.5.2.5.3.1.2.1.6-.1 1.1z"/></svg>',
}


# Disegni flash (SVG semplici, originali)
FLASH = [
    ("Cuore", '<path class="fill-red" d="M50 85C20 62 10 45 10 32 10 18 22 10 33 10c9 0 15 6 17 12 2-6 8-12 17-12 11 0 23 8 23 22 0 13-10 30-40 53z"/>'),
    ("Stella", '<polygon class="fill-gold" points="50,8 61,38 93,38 67,57 77,89 50,70 23,89 33,57 7,38 39,38"/>'),
    ("Luna", '<path class="fill-gold" d="M62 10a40 40 0 1 0 28 60A32 32 0 1 1 62 10z"/>'),
    ("Fulmine", '<polygon class="fill-gold" points="58,5 20,55 46,55 38,95 80,40 54,40 64,5"/>'),
    ("Pugnale", '<polygon points="50,95 42,42 58,42"/><rect class="fill-gold" x="30" y="35" width="40" height="7" rx="2"/><rect x="45" y="14" width="10" height="21"/><circle class="fill-red" cx="50" cy="9" r="5"/>'),
    ("Occhio", '<path d="M8 50Q50 10 92 50 50 90 8 50z"/><circle class="fill-gold" cx="50" cy="50" r="14"/><circle cx="50" cy="50" r="5" style="fill:#111"/><path d="M30 28l-5-9M50 22V12M70 28l5-9"/>'),
    ("Àncora", '<circle cx="50" cy="14" r="7"/><path d="M50 21v67M32 34h36M18 62q4 26 32 26t32-26M12 66l6-6 6 6M76 66l6-6 6 6"/>'),
    ("Sole", '<circle class="fill-gold" cx="50" cy="50" r="18"/><path d="M50 6v16M50 78v16M6 50h16M78 50h16M19 19l11 11M70 70l11 11M81 19 70 30M30 70 19 81"/>'),
    ("Diamante", '<polygon points="30,20 70,20 88,40 50,88 12,40"/><path d="M12 40h76M30 20l10 20 10 48 10-48 10-20"/>'),
    ("Fiamma", '<path class="fill-red" d="M50 92c-25 0-32-22-25-37 5-10 15-15 13-33 17 8 24 23 20 36 6-4 8-10 8-16 12 13 14 28 6 40-6 8-14 10-22 10z"/>'),
    ("Ciliegie", '<circle class="fill-red" cx="34" cy="72" r="14"/><circle class="fill-red" cx="66" cy="74" r="14"/><path d="M34 58q8-30 26-44 2 26 6 46M60 14q14-4 24 6-12 6-24-6"/>'),
    ("Picche", '<path d="M50 10C30 35 12 45 12 60c0 14 16 20 30 10l-6 20h28l-6-20c14 10 30 4 30-10 0-15-18-25-38-50z" style="fill:#111"/>'),
]


def flash_svg(i):
    return f'<svg viewBox="0 0 100 100" aria-hidden="true">{FLASH[i][1]}</svg>'


# ------------------------------ Layout ------------------------------
def header(active):
    on = ' class="active" aria-current="page"'
    links = "\n".join(
        f'        <li><a href="{h}"{on if h == active else ""}>{t}</a></li>'
        for h, t in MENU
    )
    return f"""<header class="site-header">
  <div class="nav-wrap">
    <a href="index.html" class="logo" aria-label="{STUDIO} Tattoo Studio - Home">
      <img class="logo-img" src="img/logo-martius.png" alt="Logo {STUDIO}" width="171" height="253">
      <span class="logo-text">{STUDIO.upper()}<small>TATTOO STUDIO</small></span>
    </a>
    <button class="burger" aria-label="Apri menu" aria-expanded="false"><span></span></button>
    <nav class="main-nav" aria-label="Menu principale">
      <ul>
{links}
      </ul>
    </nav>
  </div>
</header>"""


def visit_section(title_white="VIENI DA", title_gold=STUDIO.upper()):
    return f"""<section class="section" id="visita">
  <div class="container visit">
    <div class="reveal">
      <h2>{title_white}<br><span class="gold">{title_gold}</span></h2>
      <ul class="contact-list">
        <li>{I['pin']}<span>{ADDRESS_1}, {ADDRESS_2}</span></li>
        <li>{I['phone']}<a href="{TEL}">{PHONE}</a></li>
        <li>{I['mail']}<a href="mailto:{EMAIL}">{EMAIL}</a></li>
        <li>{I['clock']}<span>{HOURS_SHORT} · {HOURS_TIME} — su appuntamento</span></li>
      </ul>
      <a href="contatti.html#prenota" class="btn btn-gold">PRENOTA IL TUO APPUNTAMENTO →</a><br>
      <a href="{MAP_DIR}" target="_blank" rel="noopener" class="directions">{I['pin']} Indicazioni stradali →</a>
      <div class="socials">
        <a href="{INSTAGRAM}" target="_blank" rel="noopener" aria-label="Instagram">{I['ig']}</a>
        <a href="https://wa.me/{WHATSAPP}" target="_blank" rel="noopener" aria-label="WhatsApp">{I['wa']}</a>
        <a href="{FACEBOOK}" aria-label="Facebook">{I['fb']}</a>
        <a href="{TIKTOK}" aria-label="TikTok">{I['tt']}</a>
      </div>
    </div>
    <div class="map reveal">
      <iframe src="{MAP_EMBED}" loading="lazy" title="Mappa {STUDIO} Tattoo Studio, {CITY}" referrerpolicy="no-referrer-when-downgrade"></iframe>
    </div>
  </div>
</section>"""


def footer():
    links = "".join(f'<li><a href="{h}">{t}</a></li>' for h, t in MENU[1:5])
    links2 = "".join(f'<li><a href="{h}">{t}</a></li>' for h, t in MENU[5:])
    return f"""<footer class="site-footer">
  <div class="container footer-grid">
    <div>
      <a href="index.html" class="logo"><img class="logo-img" src="img/logo-martius.png" alt="Logo {STUDIO}" width="171" height="253"><span class="logo-text">{STUDIO.upper()}<small>TATTOO STUDIO</small></span></a>
      <p class="sub">Tatuaggi personalizzati, cover-up e piercing professionali a {CITY}.</p>
    </div>
    <div><h4>STUDIO</h4><ul><li>{ADDRESS_1}</li><li>{ADDRESS_2}</li><li>{HOURS_SHORT} · {HOURS_TIME}</li></ul></div>
    <div><h4>SERVIZI</h4><ul>{links}</ul></div>
    <div><h4>INFO</h4><ul>{links2}<li><a href="{TEL}">{PHONE}</a></li><li><a href="mailto:{EMAIL}">{EMAIL}</a></li></ul></div>
  </div>
  <div class="footer-bottom">© <span class="year">2026</span> {STUDIO} Tattoo Studio · {CITY} (PG) · Tutti i diritti riservati</div>
</footer>"""


def page(filename, title, desc, body):
    html = f"""<!DOCTYPE html>
<html lang="it">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{img(IMG_HERO, 1200)}">
<link rel="icon" type="image/png" href="img/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Montserrat:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/style.css">
</head>
<body>
{header(filename)}
<main>
{body}
</main>
{footer()}
<script src="js/main.js"></script>
</body>
</html>
"""
    (OUT / filename).write_text(html, encoding="utf-8")
    print("scritto", filename)


def page_hero(eyebrow, white, gold, lead, image, buttons=True):
    btns = """<div class="hero-actions">
      <a href="contatti.html#prenota" class="btn btn-gold">PRENOTA ORA →</a>
      <a href="index.html#lavori" class="btn btn-outline">GUARDA I LAVORI</a>
    </div>""" if buttons else ""
    return f"""<section class="hero page-hero" style="background-image:url('{img(image, 1800)}')">
  <div class="container">
    <span class="eyebrow">{eyebrow}</span>
    <h1>{white}<br><span class="gold">{gold}</span></h1>
    <p class="lead">{lead}</p>
    {btns}
  </div>
</section>"""


def cta(text="PRONTO PER IL TUO PROSSIMO TATUAGGIO?"):
    return f"""<section class="cta-band section tight">
  <div class="container">
    <h2>{text}</h2>
    <a href="contatti.html#prenota" class="btn btn-gold">PRENOTA ORA →</a>
  </div>
</section>"""


def gallery_html():
    figs = "\n".join(
        f'    <figure data-cat="{c}" data-full="{img(p, 1400)}" aria-label="{a}" role="button" tabindex="0" '
        f'style="background-image:url(\'{img(p, 600)}\')"></figure>'
        for p, c, a in GALLERY
    )
    return f"""<section class="section" id="lavori">
  <div class="container">
    <div class="gallery-head">
      <h2 class="reveal">ULTIMI <span class="gold">LAVORI</span></h2>
      <div class="filters" data-target="#gallery">
        <button class="active" data-filter="all">TUTTI</button>
        <button data-filter="realistico">REALISTICO</button>
        <button data-filter="black-grey">BLACK &amp; GREY</button>
        <button data-filter="colore">COLORE</button>
        <button data-filter="fine-line">FINE LINE</button>
        <button data-filter="piercing">PIERCING</button>
        <button data-filter="studio">IN STUDIO</button>
      </div>
    </div>
    <div class="gallery" id="gallery">
{figs}
    </div>
    <p class="center sub" style="margin-top:34px">Altri lavori ogni giorno su <a class="gold" href="{INSTAGRAM}" target="_blank" rel="noopener">@martius_tattoo_studio</a></p>
  </div>
</section>"""


# =====================================================================
# HOME
# =====================================================================
artist_cards = "\n".join(
    f"""      <a href="artisti.html#{n.lower()}" class="artist-card" style="background-image:url('{img(p, 600)}')">
        <div><h3>{n}</h3><span class="styles">{s}</span><br><span class="link-gold">GUARDA I LAVORI →</span></div>
      </a>"""
    for n, s, _, p, _, _ in ARTISTS
)
flash_icons = "".join(flash_svg(i) for i in range(8))

home = f"""<section class="hero" style="background-image:url('{img(HERO["home"], 2000)}')">
  <div class="container">
    <span class="eyebrow">{CITY} · Umbria</span>
    <h1>LA TUA STORIA.<br><span class="gold">IL TUO SEGNO.</span></h1>
    <p class="tagline">{STUDIO} Tattoo Studio — arte sulla pelle, dal 1° disegno all'ultima linea.</p>
    <p class="lead">Tatuaggi personalizzati, piercing professionali, cover-up e restauri nel cuore dell'Alta Valle del Tevere. Arte. Igiene. Fiducia.</p>
    <div class="hero-actions">
      <a href="contatti.html#prenota" class="btn btn-gold">PRENOTA ORA →</a>
      <a href="#lavori" class="btn btn-outline">GUARDA I LAVORI</a>
    </div>
    <div class="hero-info">
      <div>{I['pin']}<span>{ADDRESS_1},<br>{ADDRESS_2}</span></div>
      <div>{I['clock']}<span>{HOURS_SHORT}<br>{HOURS_TIME}</span></div>
      <div>{I['shield']}<span>Sterile. Sicuro.<br>Professionale.</span></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head center reveal">
      <span class="eyebrow">I nostri servizi</span>
      <h2>TATUAGGI. PIERCING. EVENTI.</h2>
      <p class="lead">Lavori di qualità, artisti esperti. C'è qualcosa per tutti.</p>
    </div>
    <div class="grid-4">
      <a href="artisti.html" class="service-card reveal" style="background-image:url('{img(IMG_TATTOO, 700)}')">
        <div><h3>TATUAGGI PERSONALIZZATI</h3><p>Disegni originali, tutti gli stili. Su consulenza.</p><span class="link-gold">SCOPRI DI PIÙ →</span></div>
      </a>
      <a href="piercing.html" class="service-card reveal" style="background-image:url('{img(IMG_PIERCING, 700)}')">
        <div><h3>PIERCING E GIOIELLI</h3><p>Piercing professionali. Gioielli in titanio e oro.</p><span class="link-gold">SCOPRI DI PIÙ →</span></div>
      </a>
      <a href="flash.html" class="service-card flash-bg reveal">
        <div class="flash-icons">{flash_icons}</div>
        <div><h3>FLASH DA 50€</h3><p>Nuovi disegni ogni settimana.</p><span class="link-gold">SCOPRI DI PIÙ →</span></div>
      </a>
      <a href="eventi.html" class="service-card event-bg reveal">
        <div class="event-badge">20€<small>FLASH &amp; PIERCING</small></div>
        <div><h3>EVENTI DA 20€</h3><p>Giornate speciali. Posti limitati.</p><span class="link-gold">SCOPRI DI PIÙ →</span></div>
      </a>
    </div>
  </div>
</section>

<section class="section">
  <div class="container grid-2">
    <div class="split-img reveal" style="background-image:url('{img("img/schiena-samurai.jpg", 900)}')"></div>
    <div class="split-text reveal">
      <span class="eyebrow">Diamo nuova vita</span>
      <h2 class="big-title">COVER-UP<br><span class="gold">E RESTAURO</span></h2>
      <p class="tagline">Copriamo. Ripariamo. Trasformiamo.</p>
      <p>Linee sbiadite, colori spenti, un nome che non vuoi più vedere: valutiamo insieme il tatuaggio esistente e progettiamo una copertura o un restauro su misura per ridargli carattere.</p>
      <a href="cover-up.html" class="btn btn-gold">SCOPRI COVER-UP E RESTAURO</a>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head center reveal">
      <span class="eyebrow">I nostri artisti</span>
      <h2>TALENTO. ESPERIENZA. PASSIONE.</h2>
    </div>
    <div class="artists-track">
{artist_cards}
    </div>
    <div class="track-controls">
      <button data-scroll="-1" aria-label="Precedente">←</button>
      <button data-scroll="1" aria-label="Successivo">→</button>
    </div>
  </div>
</section>

{gallery_html()}

<section class="section">
  <div class="container">
    <div class="section-head center reveal">
      <span class="eyebrow">Perché scegliere {STUDIO}</span>
      <h2>FATTO BENE. <span class="gold">FATTO PER TE.</span></h2>
    </div>
    <div class="grid-3">
      <div class="card reveal">
        <svg class="icon" viewBox="0 0 24 24"><path d="M12 20h9M16.5 3.5a2.1 2.1 0 0 1 3 3L7 19l-4 1 1-4z"/></svg>
        <h3>PROGETTO SU MISURA</h3>
        <p>Ogni tatuaggio nasce da una consulenza gratuita: ascoltiamo la tua idea e la disegniamo solo per te.</p>
      </div>
      <div class="card reveal">
        <svg class="icon" viewBox="0 0 24 24"><path d="M12 2 4 5v6c0 5 3.4 9.7 8 11 4.6-1.3 8-6 8-11V5z"/><path d="m9 12 2 2 4-4"/></svg>
        <h3>IGIENE CERTIFICATA</h3>
        <p>Materiale sterile e monouso, superfici sanificate e procedure conformi alle norme igienico-sanitarie.</p>
      </div>
      <div class="card reveal">
        <svg class="icon" viewBox="0 0 24 24"><path d="M20.8 4.6a5.5 5.5 0 0 0-7.8 0L12 5.7l-1-1a5.5 5.5 0 0 0-7.8 7.7l1 1L12 21l7.8-7.6 1-1a5.5 5.5 0 0 0 0-7.8z"/></svg>
        <h3>SEGUITI ANCHE DOPO</h3>
        <p>Istruzioni scritte per la cura e un ritocco di controllo: restiamo al tuo fianco fino alla guarigione.</p>
      </div>
    </div>
  </div>
</section>

{visit_section()}"""

page("index.html", f"{STUDIO} Tattoo Studio | Tatuaggi e Piercing a {CITY}",
     f"{STUDIO} Tattoo Studio a {CITY} (PG): tatuaggi personalizzati, piercing, cover-up, flash ed eventi. Prenota la tua consulenza.",
     home)

# =====================================================================
# ARTISTI
# =====================================================================
rows = "\n".join(
    f"""    <div class="artist-row reveal" id="{n.lower()}">
      <div class="split-img" style="background-image:url('{img(p, 800)}')"></div>
      <div>
        <span class="eyebrow">{s}</span>
        <h2>{n}</h2>
        <div class="tags">{''.join(f'<span>{t}</span>' for t in tags)}</div>
        <p class="lead">{bio}</p>
        <div class="hero-actions" style="margin-top:28px">
          <a href="contatti.html?artista={n}#prenota" class="btn btn-gold">PRENOTA CON {n} →</a>
          <a href="{ig}" target="_blank" rel="noopener" class="btn btn-outline">PORTFOLIO @{ig.rstrip('/').split('/')[-1]}</a>
        </div>
      </div>
    </div>"""
    for n, s, tags, p, bio, ig in ARTISTS
)
page("artisti.html", f"Artisti | {STUDIO} Tattoo Studio {CITY}",
     f"Conosci gli artisti e il piercer di {STUDIO} Tattoo Studio a {CITY}: tatuaggi, body art e piercing.",
     page_hero("I nostri artisti", "TALENTO.", "ESPERIENZA. PASSIONE.",
               "Ogni artista ha il suo stile: scegli quello più vicino alla tua idea, oppure chiedici un consiglio.", HERO["artisti"])
     + f'\n<section class="section"><div class="container">\n{rows}\n</div></section>\n'
     + gallery_html() + "\n" + cta())

# =====================================================================
# COVER-UP E RESTAURO
# =====================================================================
cover = page_hero("Cover-up e restauro", "COPRIAMO.", "RIPARIAMO. TRASFORMIAMO.",
                  "Un tatuaggio vecchio, sbiadito o che non ti rappresenta più può diventare qualcosa di cui andare fieri.",
                  HERO["cover"]) + f"""
<section class="section">
  <div class="container">
    <div class="section-head center reveal">
      <span class="eyebrow">Cosa facciamo</span>
      <h2>OGNI TATUAGGIO MERITA <span class="gold">UNA SECONDA VITA</span></h2>
    </div>
    <div class="grid-4">
      <div class="card reveal"><div class="num">01</div><h3>COVER-UP</h3><p>Un nuovo disegno studiato per nascondere completamente il vecchio tatuaggio.</p></div>
      <div class="card reveal"><div class="num">02</div><h3>RAVVIVARE IL COLORE</h3><p>Ridiamo intensità ai colori spenti dal tempo e dal sole.</p></div>
      <div class="card reveal"><div class="num">03</div><h3>LINEE NITIDE</h3><p>Ripassiamo e correggiamo linee sbavate o irregolari.</p></div>
      <div class="card reveal"><div class="num">04</div><h3>RESTAURO COMPLETO</h3><p>Ridisegniamo il pezzo mantenendo il suo significato originale.</p></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container grid-2">
    <div class="split-text reveal">
      <span class="eyebrow">Come funziona</span>
      <h2>IL PERCORSO</h2>
      <ol class="steps" style="margin-top:26px">
        <li><strong>Consulenza gratuita</strong>Vieni in studio o mandaci una foto chiara del tatuaggio da coprire.</li>
        <li><strong>Valutazione</strong>Analizziamo dimensioni, colori e densità dell'inchiostro esistente.</li>
        <li><strong>Progetto</strong>Disegniamo una proposta su misura e la sistemiamo insieme fino a quando è perfetta.</li>
        <li><strong>Seduta</strong>Realizziamo il lavoro, in una o più sedute a seconda della complessità.</li>
      </ol>
    </div>
    <div class="split-img reveal" style="background-image:url('{img(IMG_TATTOO, 900)}')"></div>
  </div>
</section>
{cta("HAI UN TATUAGGIO DA SISTEMARE?")}
{visit_section()}"""
page("cover-up.html", f"Cover-up e Restauro Tatuaggi | {STUDIO} {CITY}",
     f"Cover-up, restauro e ravvivamento di vecchi tatuaggi a {CITY}. Consulenza gratuita da {STUDIO} Tattoo Studio.", cover)

# =====================================================================
# PIERCING E GIOIELLI
# =====================================================================
PIERCINGS = [
    ("Lobo", "Orecchio"), ("Helix", "Orecchio"), ("Trago", "Orecchio"), ("Conch", "Orecchio"),
    ("Rook", "Orecchio"), ("Daith", "Orecchio"), ("Industrial", "Orecchio"), ("Flat", "Orecchio"),
    ("Narice", "Naso"), ("Septum", "Naso"), ("Labret", "Labbro"), ("Medusa", "Labbro"),
    ("Lingua", "Bocca"), ("Sopracciglio", "Viso"), ("Ombelico", "Corpo"), ("Capezzolo", "Corpo"),
]
piercing_figs = "\n".join(
    f'      <figure data-cat="{c}" data-full="{img(p)}" aria-label="{a}" role="button" tabindex="0" '
    f'style="background-image:url(\'{img(p)}\')"></figure>'
    for p, c, a in GALLERY if "piercing" in c.split()
)
plist = "".join(f"<div>{n}<small>{z}</small></div>" for n, z in PIERCINGS)
pierc = page_hero("Piercing e gioielli", "PIERCING", "PROFESSIONALI.",
                  "Foratura con ago sterile monouso e gioielli di alta qualità, scelti per una guarigione sicura.",
                  HERO["piercing"]) + f"""
<section class="section">
  <div class="container">
    <div class="section-head center reveal">
      <span class="eyebrow">Cosa facciamo</span>
      <h2>I NOSTRI <span class="gold">PIERCING</span></h2>
      <p class="lead">Questi sono i più richiesti: per piercing particolari chiedi pure in studio.</p>
    </div>
    <div class="piercing-list reveal">{plist}</div>
  </div>
</section>

<section class="section" style="padding-top:0">
  <div class="container">
    <h2 class="reveal" style="margin-bottom:34px">I NOSTRI <span class="gold">LAVORI</span></h2>
    <div class="gallery">
{piercing_figs}
    </div>
  </div>
</section>

<section class="section">
  <div class="container grid-3">
    <div class="card reveal">
      <svg class="icon" viewBox="0 0 24 24"><path d="M6 3h12l4 6-10 12L2 9z"/><path d="M2 9h20M12 21 8 9l4-6 4 6z"/></svg>
      <h3>GIOIELLI</h3>
      <ul><li>Titanio implant grade (ASTM F136)</li><li>Oro 14k e 18k</li><li>Labret, anelli, barbell, clicker</li><li>Sostituzione e downsize del gioiello</li></ul>
    </div>
    <div class="card reveal">
      <svg class="icon" viewBox="0 0 24 24"><path d="M12 2 4 5v6c0 5 3.4 9.7 8 11 4.6-1.3 8-6 8-11V5z"/><path d="m9 12 2 2 4-4"/></svg>
      <h3>SICUREZZA</h3>
      <ul><li>Aghi sterili monouso, mai pistole</li><li>Guanti e materiale monouso</li><li>Sterilizzazione in autoclave</li><li>Postazione sanificata dopo ogni cliente</li></ul>
    </div>
    <div class="card reveal">
      <svg class="icon" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><path d="M12 7v5l3 2"/></svg>
      <h3>PRIMA DI VENIRE</h3>
      <ul><li>Porta un documento d'identità</li><li>Minorenni: con un genitore e consenso firmato</li><li>Mangia qualcosa prima della seduta</li><li>Prenota o passa in orario di apertura</li></ul>
    </div>
  </div>
</section>

<section class="section">
  <div class="container grid-2">
    <div class="split-img reveal" style="background-image:url('{img("img/piercing-in-studio.jpg", 900)}')"></div>
    <div class="split-text reveal">
      <span class="eyebrow">Cura del piercing</span>
      <h2>GUARIGIONE <span class="gold">SENZA PENSIERI</span></h2>
      <p>Pulisci 2 volte al giorno con soluzione fisiologica sterile, non toccare il gioiello con le mani sporche e non girarlo. Evita piscina, mare e sauna nelle prime settimane.</p>
      <a href="aftercare.html#piercing" class="btn btn-gold">ISTRUZIONI COMPLETE</a>
    </div>
  </div>
</section>
{cta("VUOI UN NUOVO PIERCING?")}
{visit_section()}"""
page("piercing.html", f"Piercing e Gioielli | {STUDIO} {CITY}",
     f"Piercing professionali a {CITY}: orecchio, naso, labbro, ombelico. Gioielli in titanio implant grade e oro.", pierc)

# =====================================================================
# FLASH 50€
# =====================================================================
fgrid = "\n".join(
    f'      <div class="flash-item reveal"><span>{i+1:02d} · {n.upper()}</span>{flash_svg(i)}<em>DA 50€</em></div>'
    for i, (n, _) in enumerate(FLASH)
)
flash = page_hero("Flash della settimana", "FLASH", "DA 50€.",
                  "Ogni settimana nuovi disegni pronti da tatuare. Scegli il tuo, prenota e vieni: semplice e veloce.",
                  HERO["flash"]) + f"""
<section class="section">
  <div class="container">
    <div class="section-head center reveal">
      <span class="eyebrow">Questa settimana</span>
      <h2>SCEGLI IL TUO <span class="gold">FLASH</span></h2>
      <p class="lead">Ogni disegno si tatua una sola volta. Le tavole complete vengono pubblicate ogni lunedì su Instagram.</p>
    </div>
    <div class="flash-grid">
{fgrid}
    </div>
  </div>
</section>

<section class="section tight">
  <div class="container grid-3">
    <div class="card reveal"><div class="num">01</div><h3>SCEGLI</h3><p>Guarda la tavola della settimana in studio o su Instagram.</p></div>
    <div class="card reveal"><div class="num">02</div><h3>PRENOTA</h3><p>Scrivici il numero del disegno: lo blocchiamo per te.</p></div>
    <div class="card reveal"><div class="num">03</div><h3>TATUA</h3><p>Prezzo a partire da 50€ in base a dimensioni e posizione.</p></div>
  </div>
</section>
{cta("HAI SCELTO IL TUO FLASH?")}
{visit_section()}"""
page("flash.html", f"Flash Tattoo da 50€ | {STUDIO} {CITY}",
     f"Flash tattoo settimanali a partire da 50€ a {CITY}. Nuovi disegni ogni settimana da {STUDIO} Tattoo Studio.", flash)

# =====================================================================
# EVENTI 20€
# =====================================================================
EVENTS = [
    ("13", "Venerdì 13", "FRIDAY 13TH FLASH DAY", "La tradizione dei tatuatori: tavola speciale di mini flash a prezzo fisso, per tutto il giorno, senza appuntamento."),
    ("20€", "Da", "FLASH &amp; PIERCING DAY", "Mini tatuaggi flash e piercing al lobo o all'helix con gioiello base in titanio, a partire da 20€."),
    ("★", "Speciale", "OPEN DAY MARTIUS", "Porte aperte in studio: conosci gli artisti, porta la tua idea e prenota la consulenza con uno sconto riservato."),
]
ev = "\n".join(
    f"""    <div class="card event-card reveal">
      <div class="event-date"><b>{b}</b><span>{s}</span></div>
      <div><h3>{t}</h3><p>{d}</p><p class="sub">Prossima data: annunciata su Instagram</p></div>
      <a href="{INSTAGRAM}" target="_blank" rel="noopener" class="btn btn-outline">SEGUI GLI AGGIORNAMENTI</a>
    </div>"""
    for b, s, t, d in EVENTS
)
events = page_hero("Eventi speciali", "FLASH E PIERCING", "DA 20€.",
                   "Giornate a tema, posti limitati e prezzi speciali. Segui Instagram per non perdere le prossime date.",
                   HERO["eventi"]) + f"""
<section class="section">
  <div class="container">
    <div class="section-head center reveal">
      <span class="eyebrow">Calendario</span>
      <h2>PROSSIMI <span class="gold">EVENTI</span></h2>
    </div>
    <div style="display:grid;gap:20px">
{ev}
    </div>
    <div class="notice reveal">
      <strong class="gold">COME FUNZIONA:</strong> durante gli eventi si lavora in ordine di arrivo fino a esaurimento posti.
      Porta un documento d'identità. I minorenni possono fare solo piercing, accompagnati da un genitore.
    </div>
  </div>
</section>
{cta("NON PERDERE IL PROSSIMO EVENTO")}
{visit_section()}"""
page("eventi.html", f"Eventi Flash e Piercing da 20€ | {STUDIO} {CITY}",
     f"Eventi flash tattoo e piercing a partire da 20€ a {CITY}: Friday 13th, Flash Day e Open Day da {STUDIO}.", events)

# =====================================================================
# AFTERCARE
# =====================================================================
# Foto della pagina aftercare (sostituibili con "img/nomefile.jpg")
IMG_AC_HERO = "img/schiena-samurai.jpg"
IMG_AC_TATTOO = "img/angelo-realistico.jpg"
IMG_AC_PIERCING = "img/piercing-smiley.jpg"
IMG_AC_WARN = "img/piercing-in-studio.jpg"


def ic(paths):
    return f'<svg class="ac-ic" viewBox="0 0 24 24" aria-hidden="true">{paths}</svg>'


def no_ic(inner):
    return ('<svg class="ac-ic big" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="10.5"/>'
            f'<g transform="translate(6 6) scale(.5)" style="stroke-width:2.6">{inner}</g><path d="M4.6 4.6l14.8 14.8"/></svg>')


HAND = '<path d="M8 13V6a1.5 1.5 0 0 1 3 0v5M11 11V4.5a1.5 1.5 0 0 1 3 0V11M14 11V6a1.5 1.5 0 0 1 3 0v8c0 4-2.5 7-6 7-3 0-4.5-2-6-5l-1.5-3a1.5 1.5 0 0 1 2.6-1.5L8 13"/>'
SPRAY = '<path d="M9 8h6v13H9zM10 8V5h4v3M14 5h3M19 3v.01M19 6v.01M21 4.5v.01"/>'
CLOCK = '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>'
AC = {
    "wash": '<path d="M8 3c-1.5 2-2.5 3.3-2.5 4.5a2.5 2.5 0 0 0 5 0C10.5 6.3 9.5 5 8 3zM15 5c-1 1.4-1.8 2.3-1.8 3.2a1.8 1.8 0 0 0 3.6 0c0-.9-.8-1.8-1.8-3.2z"/><path d="M3 18c3 0 4-2 7-2h4c1 0 1 1.5 0 1.5h-3M3 21h10l7-4c1-.6.4-2-.7-1.6L14 17.5"/>',
    "tube": '<path d="M9 2h6v3H9zM8 5h8l-1 15a2 2 0 0 1-2 2h-2a2 2 0 0 1-2-2z"/><path d="M10 10h4"/>',
    "clock": CLOCK,
    "shield": '<path d="M12 3 5 6v5c0 4.5 3 8.3 7 10 4-1.7 7-5.5 7-10V6z"/><path d="m9 12 2 2 4-4"/>',
    "gem": '<path d="M6 3h12l4 6-10 12L2 9z"/><path d="M2 9h20M12 21 8 9l4-6 4 6z"/>',
    "hand": HAND, "spray": SPRAY,
    "bottle": '<path d="M10 2h4v4l2 3v12a1 1 0 0 1-1 1H9a1 1 0 0 1-1-1V9l2-3z"/><path d="M8 13h8"/>',
    "swim": '<circle cx="16" cy="5" r="2"/><path d="M4 12l5-3 4 3 3-2M2 17c2 0 2-1.5 4-1.5S8 17 10 17s2-1.5 4-1.5 2 1.5 4 1.5M2 21c2 0 2-1.5 4-1.5S8 21 10 21s2-1.5 4-1.5 2 1.5 4 1.5"/>',
    "sun": '<circle cx="12" cy="12" r="4"/><path d="M12 2v3M12 19v3M2 12h3M19 12h3M5 5l2 2M17 17l2 2M19 5l-2 2M7 17l-2 2"/>',
    "shirt": '<path d="M8 3 3 6l2 4 2-1v12h10V9l2 1 2-4-5-3c0 2-1.5 3-4 3S8 5 8 3z"/>',
    "ear": '<path d="M7 9a5 5 0 0 1 10 0c0 3-3 4-3 7a3 3 0 0 1-6 0"/><path d="M10 9a2 2 0 0 1 4 0c0 1.5-2 2-2 3"/><circle cx="10" cy="19.5" r="1"/>',
    "cartilage": '<path d="M7 9a5 5 0 0 1 10 0c0 3-3 4-3 7a3 3 0 0 1-6 0"/><path d="M10 9a2 2 0 0 1 4 0c0 1.5-2 2-2 3"/><circle cx="15.5" cy="5" r="1.5"/>',
    "nose": '<path d="M12 3c0 6-4 10-4 13a3 3 0 0 0 3 3h3a2 2 0 0 0 0-4"/><circle cx="8.5" cy="18.5" r="1.3"/>',
    "lips": '<path d="M3 12c3-4 6-4 9-2 3-2 6-2 9 2-3 5-15 5-18 0z"/><path d="M3 12h18"/>',
    "brow": '<path d="M3 14c5-5 12-6 18-3"/><circle cx="15" cy="7" r="1.2"/><circle cx="17" cy="11.5" r="1.2"/>',
    "navel": '<path d="M12 3v3"/><circle cx="12" cy="7.6" r="1.6"/><path d="M9 14c0-3 1.5-3.5 3-3.5s3 .5 3 3.5-1.5 5-3 5-3-2-3-5z"/><circle cx="12" cy="21" r="1.2"/>',
}

TATTOO_STEPS = [
    ("wash", "TIENILO PULITO", "Lava delicatamente con acqua tiepida e sapone neutro senza profumo, 2–3 volte al giorno."),
    ("tube", "IDRATA", "Applica uno strato sottile della crema o pomata per tatuaggi che ti abbiamo consigliato."),
    ("clock", "LASCIALO GUARIRE", "Lascia che guarisca in modo naturale: desquamazione, prurito e piccole crosticine sono normali."),
    ("shield", "PROTEGGILO", "Tienilo lontano dal sole diretto, evita bagni prolungati (piscina, idromassaggio, vasca) e indossa abiti larghi."),
]
AVOID = [
    ("hand", "Non grattare<br>e non staccare le croste"),
    ("bottle", "Niente alcol<br>sul tatuaggio"),
    ("swim", "Niente bagni<br>(idromassaggio, piscina, mare)"),
    ("sun", "Niente sole diretto<br>né lampade abbronzanti"),
    ("shirt", "Niente abiti stretti<br>o ruvidi"),
    ("spray", "Niente creme profumate<br>o prodotti aggressivi"),
]
PIERCING_STEPS = [
    ("spray", "PULISCI OGNI GIORNO", "Usa soluzione fisiologica sterile 2–3 volte al giorno: spruzzala o imbevi una garza pulita e pulisci con delicatezza."),
    ("hand", "GIÙ LE MANI", "Non toccare, girare o muovere il gioiello, se non durante la pulizia."),
    ("gem", "NON TOGLIERE IL GIOIELLO", "Lascia il gioiello originale per tutto il periodo di guarigione consigliato."),
    ("clock", "ABBI PAZIENZA", "I tempi variano in base al tipo di piercing. Segui le indicazioni del piercer per il miglior risultato."),
]
HEALING = [
    ("ear", "Lobo", "6–8 settimane"), ("cartilage", "Cartilagine", "3–12 mesi"), ("nose", "Naso", "2–4 mesi"),
    ("lips", "Labbro", "6–8 settimane"), ("brow", "Sopracciglio", "6–8 settimane"), ("navel", "Ombelico", "6–12 mesi"),
]
WARNINGS = [
    "Arrossamento, gonfiore o dolore eccessivi",
    "Secrezioni dense, gialle o verdi",
    "Febbre o sintomi simil-influenzali",
    "Gioiello che affonda nella pelle",
    "Qualsiasi cambiamento insolito o dubbio",
]


def ac_head(white, gold):
    return f'<div class="ac-head reveal"><h2>{white} <span class="gold">{gold}</span></h2><span class="ac-line"></span></div>'


def ac_steps(steps, photo):
    cards = "".join(
        f'<div class="ac-step"><div class="ac-step-top"><span class="ac-num">{i}</span>{ic(AC[k])}</div>'
        f'<h4>{t}</h4><p>{d}</p></div>'
        for i, (k, t, d) in enumerate(steps, 1)
    )
    return f'<div class="ac-row reveal"><div class="ac-photo" style="background-image:url(\'{img(photo, 600)}\')"></div>{cards}</div>'


avoid_html = "".join(f'<div>{no_ic(AC[k])}<p>{t}</p></div>' for k, t in AVOID)
heal_html = "".join(f'<div>{ic(AC[k])}<b>{n}</b><span>{d}</span></div>' for k, n, d in HEALING)
warn_html = "".join(f'<li><span class="ac-check">✓</span>{w}</li>' for w in WARNINGS)

after = page_hero(f"{STUDIO.upper()} TATTOO STUDIO.", "AFTER CARE", "ISTRUZIONI",
                  "Un tatuaggio o un piercing guarisce bene solo se lo tratti bene. Segui queste indicazioni per mantenerlo pulito, sano e bello nel tempo.",
                  HERO["aftercare"], buttons=False) + f"""
<section class="ac-section">
  <div class="container">
    {ac_head("TATTOO", "AFTERCARE")}
    <p class="ac-sub">Segui questi passaggi per mantenere il tuo nuovo tatuaggio pulito, sano e al massimo della sua bellezza.</p>
    {ac_steps(TATTOO_STEPS, IMG_AC_TATTOO)}
  </div>
</section>

<section class="ac-avoid">
  <div class="container">
    <h2 class="reveal">COSA <span class="gold">EVITARE</span></h2>
    <div class="avoid-grid reveal">{avoid_html}</div>
  </div>
</section>

<section class="ac-section" id="piercing">
  <div class="container">
    {ac_head("PIERCING", "AFTERCARE")}
    <p class="ac-sub">Tieni pulito il piercing, evita irritazioni e segui questi passaggi per una guarigione corretta.</p>
    {ac_steps(PIERCING_STEPS, IMG_AC_PIERCING)}
  </div>
</section>

<section class="ac-bottom">
  <div class="ac-warn-bg" style="background-image:url('{img(IMG_AC_WARN, 1200)}')"></div>
  <div class="container ac-split">
    <div class="reveal">
      <h3 class="ac-small-head">TEMPI DI GUARIGIONE <span class="gold">PIÙ COMUNI</span></h3>
      <div class="heal-grid">{heal_html}</div>
    </div>
    <div class="ac-warn reveal">
      <h3><span class="ac-tri">{ic('<path d="M12 3 2 21h20z"/><path d="M12 10v5M12 18v.01"/>')}</span>ATTENZIONE AI <span class="red">SEGNALI D'ALLARME</span></h3>
      <ul>{warn_html}</ul>
      <p>Noti uno di questi segnali? <strong>Contattaci subito</strong> o rivolgiti a un medico.</p>
    </div>
  </div>
</section>

<section class="section center">
  <div class="container">
    <span class="eyebrow">Hai domande?</span>
    <h2>CONTATTA IL <span class="gold">NOSTRO TEAM</span></h2>
    <p class="lead" style="margin:18px auto 34px">Se hai dubbi sulla guarigione o qualcosa non ti convince, scrivici: siamo qui per aiutarti.</p>
    <div class="hero-actions" style="justify-content:center">
      <a href="contatti.html#prenota" class="btn btn-gold">PRENOTA ORA</a>
      <a href="https://wa.me/{WHATSAPP}" target="_blank" rel="noopener" class="btn btn-outline">SCRIVICI SU WHATSAPP</a>
    </div>
  </div>
</section>"""
page("aftercare.html", f"Cura post-tatuaggio e piercing | {STUDIO} {CITY}",
     "Istruzioni per la cura del tatuaggio e del piercing: cosa fare nei primi giorni per una guarigione perfetta.", after)

# =====================================================================
# CONTATTI
# =====================================================================
artist_opts = "".join(f"<option>{n.title()}</option>" for n, *_ in ARTISTS)
contact = page_hero("Contatti", "PRENOTA LA TUA", "CONSULENZA.",
                    f"Scrivici la tua idea: ti rispondiamo entro 24–48 ore. Ci trovi a {CITY}.",
                    HERO["contatti"], buttons=False) + f"""
<section class="section" id="prenota">
  <div class="container grid-2" style="align-items:start">
    <div class="reveal">
      <span class="eyebrow">Richiesta appuntamento</span>
      <h2>RACCONTACI <span class="gold">LA TUA IDEA</span></h2>
      <p class="sub" style="margin-bottom:30px">Compila il modulo: si aprirà la tua email già pronta da inviare. Puoi allegare foto di riferimento.</p>
      <form id="booking-form" class="form" data-email="{EMAIL}">
        <div><label for="nome">Nome e cognome</label><input id="nome" name="nome" required></div>
        <div><label for="telefono">Telefono</label><input id="telefono" name="telefono" type="tel" required></div>
        <div class="full"><label for="email">Email</label><input id="email" name="email" type="email" required></div>
        <div><label for="servizio">Servizio</label>
          <select id="servizio" name="servizio">
            <option>Tatuaggio personalizzato</option><option>Piercing</option><option>Cover-up / Restauro</option>
            <option>Flash da 50€</option><option>Evento da 20€</option><option>Altro</option>
          </select></div>
        <div><label for="artista">Artista</label>
          <select id="artista" name="artista"><option>Nessuna preferenza</option>{artist_opts}</select></div>
        <div class="full"><label for="zona">Zona del corpo e dimensioni</label><input id="zona" name="zona" placeholder="Es. avambraccio, circa 10 cm"></div>
        <div class="full"><label for="messaggio">La tua idea</label><textarea id="messaggio" name="messaggio" required></textarea></div>
        <label class="check full"><input type="checkbox" required> Ho letto l'informativa e acconsento al trattamento dei dati per essere ricontattato.</label>
        <div class="full"><button class="btn btn-gold" type="submit">INVIA RICHIESTA →</button></div>
      </form>
    </div>
    <div class="reveal">
      <div class="card">
        <h3>CONTATTI DIRETTI</h3>
        <ul class="contact-list" style="margin-top:14px">
          <li>{I['pin']}<span>{ADDRESS_1}, {ADDRESS_2}</span></li>
          <li>{I['phone']}<a href="{TEL}">{PHONE}</a></li>
          <li>{I['wa']}<a href="https://wa.me/{WHATSAPP}" target="_blank" rel="noopener">Scrivici su WhatsApp</a></li>
          <li>{I['mail']}<a href="mailto:{EMAIL}">{EMAIL}</a></li>
          <li>{I['ig']}<a href="{INSTAGRAM}" target="_blank" rel="noopener">@martius_tattoo_studio</a></li>
        </ul>
      </div>
      <div class="card" style="margin-top:20px">
        <h3>ORARI</h3>
        <ul style="margin-top:10px">
          <li>Lunedì — chiuso</li>
          <li>Martedì – Venerdì — 14:30 – 20:00</li>
          <li>Sabato — 10:30 – 19:00</li>
          <li>Domenica — chiuso</li>
          <li>Solo su appuntamento, eventi esclusi</li>
        </ul>
      </div>
    </div>
  </div>
</section>
{visit_section("COME", "TROVARCI")}
<script>
  // Preseleziona l'artista se arriva da "Prenota con ..."
  const a = new URLSearchParams(location.search).get("artista");
  if (a) {{ const s = document.getElementById("artista"); [...s.options].forEach(o => {{ if (o.text.toUpperCase() === a.toUpperCase()) o.selected = true; }}); }}
</script>"""
page("contatti.html", f"Contatti e Prenotazioni | {STUDIO} Tattoo Studio {CITY}",
     f"Prenota tatuaggi e piercing da {STUDIO} Tattoo Studio a {CITY}: modulo, telefono, WhatsApp, email e mappa.", contact)
