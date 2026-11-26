#!/usr/bin/env python3
"""Générateur du site Ateliers W (site statique publié par Render depuis public/).

Usage : python3 build.py

- Pages fixes (accueil, contact, méthode, légal) : définies dans ce fichier.
- Guides comparatifs : content.py (liste GUIDES).
- Journal (blog) : blog.py (liste POSTS).
- Liens sortants / affiliés : dictionnaire LINKS ci-dessous. Dans les textes,
  écrire {{lien:Clé}} ou {{lien:Clé|texte du lien}} ; le bon rel et le suivi
  Umami sont ajoutés automatiquement.

Règles : aucun nom de personne, jamais de prix / avis / tests inventés,
sources officielles uniquement.
"""
import hashlib, html, json, os, re, shutil
from datetime import date

from content import GUIDES
from blog import POSTS

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "public")
SITE = "https://ateliers-w.com"
BRAND = "Ateliers W"
EMAIL = "contactateliersw@gmail.com"  # passera à contact@ateliers-w.com quand la redirection IONOS sera active

# Mentions légales : rempli dès que les informations sont fournies (aucun nom de personne).
LEGAL = {
    "forme": "",      # ex. "SAS au capital de 1 000 €"
    "siret": "",      # ex. "123 456 789 00012"
    "rcs": "",        # ex. "RCS Paris"
    "siege": "",      # adresse du siège
    "tva": "",
}

# Mesure d'audience Umami Cloud (EU). Vide = pas de script.
UMAMI_ID = ""
UMAMI_SRC = "https://cloud.umami.is/script.js"

# Newsletter (formulaire Brevo). Vide = bloc masqué.
NEWSLETTER_ACTION = ""

# Réseaux sociaux de la marque (vide = icône masquée).
SOCIAL = {
    "instagram": "https://www.instagram.com/les_ateliersw/",
    "facebook": "",
    "linkedin": "",
}

# Liens sortants. "aff": True => lien affilié (rel sponsored + mention).
LINKS = {
    "Service-Public copropriété": {"url": "https://www.service-public.gouv.fr/particuliers/vosdroits/F31513", "aff": False},
    "ANIL": {"url": "https://www.anil.org/", "aff": False},
    "Cosentino": {"url": "https://www.cosentino.com/fr-fr/", "aff": False},
}

TODAY = date.today().isoformat()


# ---------------------------------------------------------------- utilitaires
def esc(s):
    return html.escape(s, quote=True)


def css_version():
    with open(os.path.join(OUT, "css", "style.css"), "rb") as f:
        return hashlib.md5(f.read()).hexdigest()[:8]


def link_html(key, text=None):
    l = LINKS[key]
    text = text or key
    if l["aff"]:
        return (f'<a href="{esc(l["url"])}" rel="sponsored nofollow noopener" target="_blank" '
                f'data-umami-event="affiliate-click" data-umami-event-product="{esc(key)}">{text}</a>')
    return (f'<a href="{esc(l["url"])}" rel="noopener" target="_blank" '
            f'data-umami-event="outbound-click" data-umami-event-product="{esc(key)}">{text}</a>')


def expand(s):
    def rep(m):
        key, _, text = m.group(1).partition("|")
        return link_html(key.strip(), text.strip() or None)
    return re.sub(r"\{\{lien:([^}]+)\}\}", rep, s)


def has_aff(*texts):
    blob = " ".join(texts)
    for m in re.finditer(r"\{\{lien:([^}|]+)", blob):
        if LINKS[m.group(1).strip()]["aff"]:
            return True
    return False


def fr_date(iso):
    mois = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août",
            "septembre", "octobre", "novembre", "décembre"]
    y, m, d = iso.split("-")
    return f"{int(d)} {mois[int(m) - 1]} {y}"


ICONS = {
    "instagram": '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5" fill="none" stroke="currentColor" stroke-width="1.8"/><circle cx="12" cy="12" r="4.2" fill="none" stroke="currentColor" stroke-width="1.8"/><circle cx="17.4" cy="6.6" r="1.2" fill="currentColor"/></svg>',
    "facebook": '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M13.5 21v-7.5h2.6l.4-3h-3V8.6c0-.9.3-1.5 1.5-1.5h1.6V4.4c-.3 0-1.2-.1-2.3-.1-2.3 0-3.8 1.4-3.8 3.9v2.3H7.9v3h2.6V21h3z"/></svg>',
    "linkedin": '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M5 8.5h3V19H5zM6.5 4a1.7 1.7 0 110 3.4 1.7 1.7 0 010-3.4zM10 8.5h2.9v1.4h.1c.4-.8 1.4-1.6 2.9-1.6 3.1 0 3.6 2 3.6 4.6V19h-3v-5.3c0-1.3 0-2.9-1.8-2.9s-2 1.4-2 2.8V19h-3z"/></svg>',
}
SOCIAL_LABEL = {"instagram": "Instagram", "facebook": "Facebook", "linkedin": "LinkedIn"}


def social_icons(cls):
    items = [f'<a href="{esc(u)}" rel="noopener" target="_blank" aria-label="{BRAND} sur {SOCIAL_LABEL[k]}" '
             f'data-umami-event="social-click" data-umami-event-network="{k}">{ICONS[k]}</a>'
             for k, u in SOCIAL.items() if u]
    return f'<div class="{cls}">{"".join(items)}</div>' if items else ""


def org_jsonld():
    data = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": ["Organization", "HomeAndConstructionBusiness"],
                "@id": SITE + "/#org",
                "name": BRAND,
                "url": SITE + "/",
                "logo": SITE + "/img/logo.png",
                "image": SITE + "/img/service-renovation.jpg",
                "email": EMAIL,
                "description": "Entreprise française d'artisans : rénovation, home staging, design d'intérieur et communication immobilière à Paris.",
                "areaServed": {"@type": "City", "name": "Paris"},
                "address": {"@type": "PostalAddress", "addressLocality": "Paris", "addressCountry": "FR"},
                "sameAs": [u for u in SOCIAL.values() if u],
                "knowsAbout": ["Rénovation", "Home staging", "Design d'intérieur", "Communication immobilière"],
            },
            {
                "@type": "WebSite",
                "@id": SITE + "/#website",
                "name": BRAND,
                "url": SITE + "/",
                "inLanguage": "fr-FR",
                "publisher": {"@id": SITE + "/#org"},
            },
        ],
    }
    return data


def breadcrumb(items):
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": n, "item": SITE + u}
            for i, (n, u) in enumerate(items)
        ],
    }


def faq_jsonld(faq):
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer", "text": re.sub(r"<[^>]+>", "", expand(a))}}
            for q, a in faq
        ],
    }


# ---------------------------------------------------------------- gabarit
NAV = [("/#expertises", "Services"), ("/#realisations", "Réalisations"), ("/guides/", "Guides"),
       ("/journal/", "Journal"), ("/notre-methode.html", "Notre méthode")]


def head(title, description, path, jsonld=(), og_type="website", image="/img/service-renovation.jpg", extra=""):
    v = css_version()
    lds = "".join(f'\n<script type="application/ld+json">{json.dumps(d, ensure_ascii=False)}</script>' for d in jsonld)
    umami = (f'\n<script defer src="{UMAMI_SRC}" data-website-id="{UMAMI_ID}"></script>' if UMAMI_ID else "")
    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(description)}">
<meta name="robots" content="index, follow, max-image-preview:large">
<link rel="canonical" href="{SITE}{path}">
<link rel="icon" type="image/x-icon" href="/img/logo.ico">
<link rel="apple-touch-icon" href="/img/logo.png">
<meta name="theme-color" content="#f7f6f2">
<meta property="og:site_name" content="{BRAND}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(description)}">
<meta property="og:type" content="{og_type}">
<meta property="og:locale" content="fr_FR">
<meta property="og:url" content="{SITE}{path}">
<meta property="og:image" content="{SITE}{image}">
<meta name="twitter:card" content="summary_large_image">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/css/style.css?v={v}">{lds}{umami}{extra}
</head>
"""


def header(hero=False):
    cls = "entete" if hero else "entete entete--plein"
    links = "".join(f'<a href="{u}">{t}</a>' for u, t in NAV)
    return f"""<body>
<div class="bandeau-ok" role="status" hidden>Merci ! Votre inscription est confirmée. À bientôt dans votre boîte mail.</div>
<header class="{cls}">
  <div class="wrap">
    <a class="logo" href="/">{BRAND}</a>
    <nav class="nav-haut" aria-label="Navigation principale">{links}</nav>
    <div class="entete__droite">{social_icons("reseaux-icones")}<a class="btn btn--petit" href="/contact.html" data-umami-event="devis-click" data-umami-event-place="header">Devis</a></div>
  </div>
</header>
"""


def newsletter_block(place):
    if not NEWSLETTER_ACTION:
        return ""
    return f"""
<section class="newsletter" aria-labelledby="nl-{place}">
  <div class="wrap newsletter__grille">
    <div>
      <h2 id="nl-{place}">La lettre de l'atelier</h2>
      <p>Une fois par semaine : un conseil rénovation ou home staging, une idée déco, nos nouveaux guides. Pas de spam, désinscription en un clic.</p>
    </div>
    <form class="newsletter__form" method="POST" action="{esc(NEWSLETTER_ACTION)}" data-umami-event="newsletter-submit" data-umami-event-place="{place}">
      <label for="nl-email-{place}">Votre e-mail</label>
      <div class="newsletter__ligne">
        <input id="nl-email-{place}" type="email" name="EMAIL" required autocomplete="email" placeholder="vous@exemple.fr">
        <button class="btn" type="submit">Je m'inscris</button>
      </div>
      <input class="hp" type="text" name="email_address_check" value="" tabindex="-1" autocomplete="off" aria-hidden="true">
      <input type="hidden" name="locale" value="fr">
      <p class="newsletter__mention">En vous inscrivant, vous acceptez de recevoir nos e-mails. Vous confirmerez votre adresse par un lien (double validation). Voir notre <a href="/confidentialite.html">politique de confidentialité</a>.</p>
    </form>
  </div>
</section>"""


def footer():
    expl = "".join(f'<a href="{u}">{t}</a>' for u, t in NAV + [("/contact.html", "Contact")])
    return f"""
<footer class="pied">
  <div class="wrap footer-container">
    <div class="footer-top">
      <div class="footer-brand">
        <a href="/" class="footer-logo">{BRAND}</a>
        <p>Rénover. Imaginer. Valoriser.</p>
        {social_icons("reseaux-icones reseaux-icones--pied")}
      </div>
      <span class="footer-location">PARIS, FRANCE</span>
    </div>
    <div class="footer-middle">
      <div class="footer-column">
        <h3>Explorer</h3>
        {expl}
      </div>
      <div class="footer-column">
        <h3>Contact</h3>
        <a href="/contact.html" data-umami-event="devis-click" data-umami-event-place="footer">Demandez un devis</a>
        <a href="mailto:{EMAIL}">{EMAIL}</a>
        <p>Paris, France</p>
      </div>
    </div>
    <div class="footer-bottom">
      <div class="footer-legal">
        <a href="/mentions-legales.html">Mentions légales</a>
        <a href="/confidentialite.html">Confidentialité</a>
        <a href="/liens-affilies.html">Liens affiliés</a>
        <a href="/accessibilite.html">Accessibilité</a>
        <a href="/conditions.html">Conditions d'utilisation</a>
      </div>
      <p>© {date.today().year} {BRAND} — Tous droits réservés</p>
    </div>
  </div>
</footer>
<script src="/js/main.js?v={css_version()}"></script>
</body>
</html>
"""


def write(path, content):
    full = os.path.join(OUT, path.lstrip("/"))
    if full.endswith("/"):
        full += "index.html"
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)


PAGES = []  # (path, lastmod, priority)


def page(path, title, description, body, jsonld=(), hero=False, lastmod=TODAY, priority="0.6", **kw):
    write(path if not path.endswith("/") else path + "index.html",
          head(title, description, path, jsonld, **kw) + header(hero) + body + footer())
    PAGES.append((path, lastmod, priority))


def cta_devis(place, texte="Un projet de rénovation, de home staging ou de décoration ? Décrivez-le, nous vous répondons avec un devis."):
    return f"""
<aside class="cta-devis">
  <p>{texte}</p>
  <a class="btn" href="/contact.html" data-umami-event="devis-click" data-umami-event-place="{place}">Demandez un devis</a>
</aside>"""


def aff_notice(on):
    return ('<p class="mention-aff">Contient des liens affiliés. <a href="/liens-affilies.html">En savoir plus</a></p>'
            if on else "")


# ---------------------------------------------------------------- accueil
GALERIE = [
    "https://static.wixstatic.com/media/990b2f_b3f0397ceaa146f08fc655c63d8d6603~mv2.jpg",
    "/img/realisation-5.jpg",
    "https://static.wixstatic.com/media/990b2f_ea37cf52fc39498bb3cf0bdcae50b721~mv2.jpg",
    "/img/realisation-4.jpg",
    "/img/realisation-1.jpg",
    "/img/realisation-6.jpg",
    "https://static.wixstatic.com/media/990b2f_31e0ada49a0147ae87de59a973983700~mv2.jpg",
    "https://static.wixstatic.com/media/990b2f_23b0f11b4dc5460e9c68d32c4ffc8220~mv2.jpg",
    "/img/realisation-7.jpg",
    "https://static.wixstatic.com/media/990b2f_0b2b945fd7ca47ee9049ea4e5103f7b1~mv2.jpg",
    "https://static.wixstatic.com/media/990b2f_7c2c22f2d1694f1fa17cb2c14c24a5f0~mv2.jpg",
    "https://static.wixstatic.com/media/990b2f_98778ebacb434d918b8e889cfd9cf00b~mv2.jpg",
]


def build_home():
    recents = POSTS[:3]
    cartes = "".join(
        f'<a class="carte" href="/journal/{p["slug"]}.html"><span class="carte__cat">{esc(p["category"])}</span>'
        f'<h3>{esc(p["h1"])}</h3><p>{esc(p["description"])}</p><span class="carte__date">{fr_date(p["date"])}</span></a>'
        for p in recents)
    guides = "".join(
        f'<a class="carte" href="/guides/{g["slug"]}.html"><span class="carte__cat">Guide</span>'
        f'<h3>{esc(g["h1"])}</h3><p>{esc(g["description"])}</p></a>'
        for g in GUIDES[:3])
    gal = "".join(
        f'<img{" class=\"nouvelle-ligne\"" if i % 3 == 0 and i else ""} src="{u}" alt="Réalisation {BRAND} : rénovation et aménagement intérieur" loading="lazy">'
        for i, u in enumerate(GALERIE))
    body = f"""
<section class="hero">
  <div class="hero__contenu">
    <p>De la conception à la pose, sans intermédiaire</p>
    <h1>Ateliers W <span class="hero__sous-titre">Rénovation, home staging et design d'intérieur à Paris</span></h1>
    <p class="hero__metiers">Rénovation · Home staging · Design d'intérieur · Communication immobilière</p>
    <a class="btn" href="/contact.html" data-umami-event="devis-click" data-umami-event-place="hero">Demandez un devis</a>
  </div>
</section>

<section class="intro">
  <div class="wrap">
    <p class="intro__citation">« Rénover, mettre en scène, valoriser : un seul atelier, du chantier jusqu'à l'annonce. »</p>
    <p class="intro__texte">{BRAND} vous accompagne dans vos projets de valorisation immobilière : rénover un bien, le mettre en scène pour la vente, repenser son décor ou aider les acheteurs à s'y projeter grâce à de belles images.</p>
  </div>
</section>

<section class="section expertises" id="expertises">
  <div class="wrap">
    <h2>Nos services</h2>
    <div class="expertises__grille">
      <a class="tuile" href="/contact.html" data-umami-event="devis-click" data-umami-event-place="service-renovation">
        <img src="/img/service-renovation.jpg" alt="Cuisine rénovée avec îlot" loading="lazy">
        <h3>Rénovation</h3><p>Du gros œuvre aux finitions, intérieur et extérieur</p></a>
      <a class="tuile" href="/contact.html" data-umami-event="devis-click" data-umami-event-place="service-home-staging">
        <img src="/img/service-home-staging.jpg" alt="Salon mis en scène pour une vente" loading="lazy">
        <h3>Home staging<br>&amp; mise en scène</h3><p>Valoriser un bien pour le vendre vite et bien</p></a>
      <a class="tuile" href="/contact.html" data-umami-event="devis-click" data-umami-event-place="service-design">
        <img src="/img/service-design-interieur.jpg" alt="Chambre au décor soigné" loading="lazy">
        <h3>Design<br>d'intérieur</h3><p>Couleurs, matières, plan et ambiance</p></a>
      <a class="tuile" href="/contact.html" data-umami-event="devis-click" data-umami-event-place="service-communication">
        <img src="/img/service-communication-immobiliere.jpg" alt="Séjour et cuisine ouverte photographiés pour une annonce" loading="lazy">
        <h3>Communication<br>immobilière</h3><p>Photos, annonce et visuels avant / après</p></a>
    </div>
  </div>
</section>

<section class="section entreprise" id="entreprise">
  <div class="wrap">
    <h2>Notre entreprise</h2>
    <div class="entreprise__grille">
      <img src="https://static.wixstatic.com/media/990b2f_128f53b0d23041e7aa7f744d688919c4~mv2.jpg" alt="{BRAND}, la rencontre des idées et du savoir-faire" loading="lazy">
      <div>
        <h3>La rencontre des idées et du savoir-faire</h3>
        <p>Entreprise française d'artisans, nous sommes spécialisés dans la construction, la rénovation et la transformation d'espaces intérieurs et extérieurs.<br>
        Nos services sur mesure s'adaptent à vos envies et donnent vie à vos idées, du plan à la réalisation.</p>
        <p class="entreprise__plus">Rénovation, home staging, design d'intérieur et communication immobilière : tout est réuni sous un même toit.</p>
        <a class="btn" href="/contact.html" data-umami-event="devis-click" data-umami-event-place="entreprise">Demandez un devis</a>
        <a class="lien-fleche" href="/notre-methode.html">Notre méthode →</a>
      </div>
    </div>
  </div>
</section>

<section class="section" id="realisations">
  <div class="wrap">
    <h2>Nos réalisations</h2>
    <div class="galerie">{gal}</div>
  </div>
</section>

<section class="section conseils">
  <div class="wrap">
    <h2>Conseils &amp; guides</h2>
    <div class="cartes">{guides}{cartes}</div>
    <p class="centre"><a class="lien-fleche" href="/journal/">Tout le Journal →</a> <a class="lien-fleche" href="/guides/">Tous les guides →</a></p>
  </div>
</section>
{newsletter_block("accueil")}
"""
    ld = [org_jsonld()]
    page("/", f"{BRAND} | Rénovation, Home Staging & Design d'intérieur à Paris",
         f"{BRAND}, entreprise de rénovation, home staging, design d'intérieur et communication immobilière à Paris. De la conception à la pose, sans intermédiaire.",
         body, ld, hero=True, priority="1.0")


# ---------------------------------------------------------------- contact
def build_contact():
    body = f"""
<main class="section contact contact-page">
  <div class="wrap">
    <h1 class="titre-page titre-page--clair">Demandez un devis</h1>
    <p class="contact__intro">Rénovation, home staging, design d'intérieur ou photos pour une annonce : décrivez votre projet (adresse ou arrondissement, surface, délais). Nous revenons vers vous rapidement.</p>
    <form action="https://formspree.io/f/xljglkry" method="POST" class="form-devis">
      <div><label for="nom">Nom</label><input id="nom" name="nom" type="text" required autocomplete="name"></div>
      <div><label for="email">E-mail*</label><input id="email" name="email" type="email" required autocomplete="email"></div>
      <div><label for="tel">Téléphone</label><input id="tel" name="telephone" type="tel" autocomplete="tel"></div>
      <div><label for="service">Service</label>
        <select id="service" name="service">
          <option>Rénovation</option><option>Home staging</option><option>Design d'intérieur</option>
          <option>Communication immobilière</option><option>Autre / plusieurs</option>
        </select></div>
      <div><label for="message">Votre projet</label><textarea id="message" name="message" required></textarea></div>
      <input class="hp" type="text" name="_gotcha" tabindex="-1" autocomplete="off" aria-hidden="true">
      <p class="contact__rgpd">Vos informations servent uniquement à répondre à votre demande. <a href="/confidentialite.html">Confidentialité</a></p>
      <div><button class="btn" type="submit">Envoyer</button></div>
      <p class="retour" role="status" aria-live="polite"></p>
    </form>
    <p class="contact__mail">Vous préférez l'e-mail ? <a href="mailto:{EMAIL}">{EMAIL}</a></p>
  </div>
</main>"""
    page("/contact.html", f"Demandez un devis | {BRAND}",
         "Demandez un devis à Ateliers W pour votre rénovation, home staging, design d'intérieur ou communication immobilière à Paris.",
         body, [breadcrumb([("Accueil", "/"), ("Devis", "/contact.html")])], priority="0.8")


# ---------------------------------------------------------------- pages simples
def simple(path, title, description, h1, content, crumb, priority="0.3"):
    body = f"""
<main class="section page-texte">
  <div class="wrap texte">
    <nav class="fil" aria-label="Fil d'Ariane"><a href="/">Accueil</a> › {esc(crumb)}</nav>
    <h1 class="titre-page">{h1}</h1>
    {content}
  </div>
</main>"""
    page(path, title, description, body, [breadcrumb([("Accueil", "/"), (crumb, path)])], priority=priority)


def build_static_pages():
    simple("/notre-methode.html", f"Notre méthode | {BRAND}",
           "Comment Ateliers W mène un projet : visite, conception, chantier sans intermédiaire, mise en scène et images. Et comment nous écrivons nos guides.",
           "Notre méthode", f"""
<p class="chapeau">{BRAND} est une entreprise française d'artisans basée à Paris. Nous réunissons sous un même toit la rénovation, le home staging, le design d'intérieur et la communication immobilière.</p>
<h2>Un seul interlocuteur, du plan à la pose</h2>
<ol class="etapes">
  <li><strong>Écoute et visite.</strong> Nous comprenons votre objectif : habiter mieux, louer, ou vendre vite et bien.</li>
  <li><strong>Conception.</strong> Plan, matériaux, couleurs et ambiance, avec un devis détaillé poste par poste.</li>
  <li><strong>Réalisation sans intermédiaire.</strong> Nos artisans réalisent les travaux, du gros œuvre aux finitions.</li>
  <li><strong>Mise en scène et images.</strong> Pour une vente ou une location : home staging, photos et visuels avant / après.</li>
</ol>
<h2>Comment nous écrivons nos guides et notre Journal</h2>
<ul>
  <li>Nous répondons à de vraies questions que se posent les propriétaires, acheteurs et vendeurs.</li>
  <li>Les règles (copropriété, urbanisme, aides) viennent de sources officielles, citées en bas de chaque article : Service-Public, ANIL, ministères, fabricants.</li>
  <li>Nous n'inventons ni prix, ni chiffres, ni avis clients. Quand un prix dépend du chantier, nous le disons.</li>
  <li>Certains liens vers des produits peuvent être des liens affiliés : ils sont signalés et ne changent jamais nos conseils. <a href="/liens-affilies.html">En savoir plus</a>.</li>
</ul>
{cta_devis("methode")}
""", "Notre méthode", priority="0.6")

    lg = LEGAL
    ident = "".join(f"<li>{lab} : {esc(v)}</li>" for lab, v in [
        ("Forme juridique", lg["forme"]), ("SIRET", lg["siret"]), ("Immatriculation", lg["rcs"]),
        ("Siège social", lg["siege"]), ("TVA intracommunautaire", lg["tva"])] if v)
    simple("/mentions-legales.html", f"Mentions légales | {BRAND}", "Mentions légales du site ateliers-w.com.",
           "Mentions légales", f"""
<h2>Éditeur du site</h2>
<ul>
  <li>{BRAND}, entreprise de rénovation, home staging, design d'intérieur et communication immobilière.</li>
  {ident}
  <li>Contact : <a href="mailto:{EMAIL}">{EMAIL}</a></li>
  <li>Directeur de la publication : le représentant légal de {BRAND}.</li>
</ul>
<h2>Hébergement</h2>
<p>Render Services, Inc., San Francisco, Californie, États-Unis — <a href="https://render.com" rel="noopener">render.com</a>.</p>
<h2>Propriété intellectuelle</h2>
<p>Les textes, photographies et visuels de ce site sont la propriété de {BRAND}, sauf mention contraire. Toute reproduction sans autorisation est interdite.</p>
<h2>Liens</h2>
<p>Le site contient des liens vers des sites tiers, dont certains liens affiliés signalés (voir <a href="/liens-affilies.html">Liens affiliés</a>). {BRAND} n'est pas responsable du contenu de ces sites.</p>
""", "Mentions légales")

    simple("/confidentialite.html", f"Politique de confidentialité | {BRAND}",
           "Comment Ateliers W traite vos données : demandes de devis, newsletter, mesure d'audience sans cookie.",
           "Politique de confidentialité", f"""
<p>Dernière mise à jour : {fr_date(TODAY)}.</p>
<h2>Responsable du traitement</h2>
<p>{BRAND} — <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
<h2>Demandes de devis</h2>
<p>Le formulaire de devis recueille votre nom, votre e-mail, votre téléphone (facultatif) et la description de votre projet. Ces données servent uniquement à vous répondre et à établir un devis (base légale : mesures précontractuelles). Elles sont transmises par le service Formspree, puis conservées au maximum 3 ans après notre dernier échange.</p>
<h2>Newsletter</h2>
<p>Si vous vous inscrivez à « La lettre de l'atelier », nous conservons votre adresse e-mail pour vous envoyer la lettre (base légale : votre consentement). L'inscription se fait en double validation : vous confirmez par un lien reçu par e-mail. Chaque e-mail contient un lien de désinscription ; votre adresse est alors supprimée de la liste d'envoi. L'envoi est assuré par Brevo (Sendinblue SAS, France), dont les serveurs sont situés dans l'Union européenne.</p>
<h2>Mesure d'audience</h2>
<p>Nous utilisons Umami Cloud (hébergement dans l'Union européenne) pour compter les visites et les clics de façon anonyme et agrégée. Umami ne dépose aucun cookie et ne collecte aucune donnée permettant de vous identifier ; aucun bandeau de consentement n'est donc nécessaire.</p>
<h2>Liens affiliés</h2>
<p>Lorsque vous cliquez sur un lien affilié, le site partenaire peut déposer ses propres cookies, selon sa propre politique de confidentialité.</p>
<h2>Vos droits</h2>
<p>Vous pouvez accéder à vos données, les rectifier, les supprimer, vous opposer à leur traitement ou retirer votre consentement en écrivant à <a href="mailto:{EMAIL}">{EMAIL}</a>. Vous pouvez aussi saisir la CNIL (<a href="https://www.cnil.fr" rel="noopener">cnil.fr</a>).</p>
""", "Confidentialité")

    simple("/liens-affilies.html", f"Liens affiliés | {BRAND}",
           "Transparence : comment Ateliers W utilise les liens affiliés dans ses guides et articles.",
           "Liens affiliés", f"""
<p>Certains liens de nos guides et articles sont des liens affiliés : si vous achetez via ces liens, {BRAND} peut percevoir une commission, sans surcoût pour vous.</p>
<ul>
  <li>Ces liens sont signalés par la mention « Contient des liens affiliés » en haut de la page.</li>
  <li>Ils ne changent jamais nos conseils : nous recommandons des matériaux et produits pour leurs qualités, y compris quand il n'existe aucun lien affilié.</li>
  <li>Nous n'inventons ni prix, ni avis, ni tests. Les informations viennent des fabricants et de sources officielles, citées en bas de chaque page.</li>
</ul>
<p>Notre activité principale reste nos chantiers : rénovation, home staging, design d'intérieur et communication immobilière.</p>
""", "Liens affiliés")

    simple("/accessibilite.html", f"Accessibilité | {BRAND}", "Déclaration d'accessibilité du site ateliers-w.com.",
           "Accessibilité", f"""
<p>Nous voulons que ce site soit utilisable par tous : textes contrastés, images décrites, navigation au clavier, pages lisibles sur mobile.</p>
<p>Si vous rencontrez une difficulté pour accéder à un contenu, écrivez-nous à <a href="mailto:{EMAIL}">{EMAIL}</a> : nous vous répondrons et corrigerons le problème.</p>
""", "Accessibilité")

    simple("/conditions.html", f"Conditions d'utilisation | {BRAND}", "Conditions d'utilisation du site ateliers-w.com.",
           "Conditions d'utilisation du site", f"""
<p>Ce site présente les services de {BRAND} et publie des guides et articles d'information. Ces contenus sont généraux : ils ne remplacent ni un devis, ni l'avis d'un professionnel du droit pour un cas particulier.</p>
<p>Les prestations de {BRAND} (travaux, home staging, design, photographie) font l'objet d'un devis écrit. Les conditions de paiement, d'acompte, de délai et d'annulation sont précisées dans chaque devis signé.</p>
<p>Questions : <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
""", "Conditions d'utilisation")


# ---------------------------------------------------------------- guides
def sources_html(src):
    if not src:
        return ""
    li = "".join(f'<li><a href="{esc(u)}" rel="noopener" target="_blank">{esc(t)}</a></li>' for t, u in src)
    return f'<section class="sources"><h2>Sources</h2><ul>{li}</ul></section>'


def faq_html(faq):
    items = "".join(f"<details><summary>{esc(q)}</summary><div>{expand(a)}</div></details>" for q, a in faq)
    return f'<section class="faq"><h2>Questions fréquentes</h2>{items}</section>'


def build_guides():
    for g in GUIDES:
        texts = [g["intro"], g["verdict"], g["how_to_choose"]] + [o["body"] for o in g["options"]] + [a for _, a in g["faq"]]
        tableau = "".join(
            f'<tr><th scope="row">{esc(o["name"])}</th><td>{esc(o["best_for"])}</td><td>{esc(o["watch"])}</td></tr>'
            for o in g["options"])
        opts = "".join(f"""
<section class="option" id="{o['id']}">
  <h2>{esc(o['name'])}</h2>
  <p class="option__pour"><strong>Idéal pour :</strong> {esc(o['best_for'])}</p>
  {expand(o['body'])}
  <div class="pc"><div><h3>Points forts</h3><ul>{''.join(f'<li>{esc(x)}</li>' for x in o['pros'])}</ul></div>
  <div><h3>Points de vigilance</h3><ul>{''.join(f'<li>{esc(x)}</li>' for x in o['cons'])}</ul></div></div>
</section>""" for o in g["options"])
        related = [p for p in POSTS if p.get("guide") == g["slug"]]
        rel = ("<section class='lies'><h2>À lire aussi</h2><ul>" + "".join(
            f'<li><a href="/journal/{p["slug"]}.html">{esc(p["h1"])}</a></li>' for p in related) + "</ul></section>") if related else ""
        body = f"""
<main class="section page-texte">
  <article class="wrap texte">
    <nav class="fil" aria-label="Fil d'Ariane"><a href="/">Accueil</a> › <a href="/guides/">Guides</a> › {esc(g['h1'])}</nav>
    <h1 class="titre-page">{esc(g['h1'])}</h1>
    <p class="meta">Mis à jour le {fr_date(g.get('updated', g['date']))} · {g['read']} min de lecture</p>
    {aff_notice(has_aff(*texts))}
    {expand(g['intro'])}
    <div class="verdict"><h2>En bref</h2>{expand(g['verdict'])}</div>
    <div class="tableau"><table><thead><tr><th>Option</th><th>Idéal pour</th><th>À surveiller</th></tr></thead><tbody>{tableau}</tbody></table></div>
    {opts}
    <section><h2>Comment choisir</h2>{expand(g['how_to_choose'])}</section>
    {faq_html(g['faq'])}
    {cta_devis("guide-" + g['slug'], g.get('cta', None) or "Vous rénovez votre cuisine, votre salle de bains ou tout un appartement à Paris ? Nous concevons et posons, sans intermédiaire.")}
    {rel}
    {sources_html(g.get('sources'))}
  </article>
</main>
{newsletter_block("guide")}"""
        path = f"/guides/{g['slug']}.html"
        ld = [
            {"@context": "https://schema.org", "@type": "Article", "headline": g["h1"], "description": g["description"],
             "datePublished": g["date"], "dateModified": g.get("updated", g["date"]), "inLanguage": "fr-FR",
             "author": {"@type": "Organization", "name": BRAND, "url": SITE + "/"},
             "publisher": {"@id": SITE + "/#org"}, "mainEntityOfPage": SITE + path,
             "image": SITE + g.get("image", "/img/service-renovation.jpg")},
            breadcrumb([("Accueil", "/"), ("Guides", "/guides/"), (g["h1"], path)]),
            faq_jsonld(g["faq"]),
        ]
        page(path, g["title"], g["description"], body, ld, lastmod=g.get("updated", g["date"]), priority="0.8",
             og_type="article", image=g.get("image", "/img/service-renovation.jpg"))

    cartes = "".join(
        f'<a class="carte" href="/guides/{g["slug"]}.html"><span class="carte__cat">Guide comparatif</span>'
        f'<h2>{esc(g["h1"])}</h2><p>{esc(g["description"])}</p></a>' for g in GUIDES)
    body = f"""
<main class="section page-texte">
  <div class="wrap">
    <nav class="fil" aria-label="Fil d'Ariane"><a href="/">Accueil</a> › Guides</nav>
    <h1 class="titre-page">Guides comparatifs</h1>
    <p class="chapeau">Matériaux, finitions, aménagements : nos comparatifs pour choisir en connaissance de cause avant vos travaux. Pour les questions pratiques, voir aussi <a href="/journal/">le Journal</a>.</p>
    <div class="cartes">{cartes}</div>
  </div>
</main>
{newsletter_block("guides")}"""
    page("/guides/", f"Guides comparatifs rénovation et décoration | {BRAND}",
         "Comparatifs de matériaux, finitions et aménagements pour bien choisir avant vos travaux de rénovation à Paris.",
         body, [breadcrumb([("Accueil", "/"), ("Guides", "/guides/")])], priority="0.7")


# ---------------------------------------------------------------- journal
def build_blog():
    guides_by_slug = {g["slug"]: g for g in GUIDES}
    for i, p in enumerate(POSTS):
        texts = [p["answer"], p["body"]] + [a for _, a in p["faq"]]
        g = guides_by_slug.get(p.get("guide"))
        guide_box = (f'<aside class="encart-guide"><span>Guide lié</span><a href="/guides/{g["slug"]}.html">{esc(g["h1"])} →</a></aside>' if g else "")
        autres = [q for q in POSTS if q["slug"] != p["slug"]][:3]
        lies = ("<section class='lies'><h2>À lire aussi</h2><ul>" + "".join(
            f'<li><a href="/journal/{q["slug"]}.html">{esc(q["h1"])}</a></li>' for q in autres) + "</ul></section>") if autres else ""
        body = f"""
<main class="section page-texte">
  <article class="wrap texte">
    <nav class="fil" aria-label="Fil d'Ariane"><a href="/">Accueil</a> › <a href="/journal/">Journal</a> › {esc(p['category'])}</nav>
    <h1 class="titre-page">{esc(p['h1'])}</h1>
    <p class="meta">{fr_date(p['date'])} · {esc(p['category'])} · {p['read']} min de lecture</p>
    {aff_notice(has_aff(*texts))}
    <div class="reponse"><strong>La réponse courte</strong>{expand(p['answer'])}</div>
    {expand(p['body'])}
    {guide_box}
    {faq_html(p['faq'])}
    {cta_devis("journal-" + p['slug'])}
    {lies}
    {sources_html(p.get('sources'))}
  </article>
</main>
{newsletter_block("journal")}"""
        path = f"/journal/{p['slug']}.html"
        ld = [
            {"@context": "https://schema.org", "@type": "BlogPosting", "headline": p["h1"], "description": p["description"],
             "datePublished": p["date"], "dateModified": p.get("updated", p["date"]), "inLanguage": "fr-FR",
             "articleSection": p["category"],
             "author": {"@type": "Organization", "name": BRAND, "url": SITE + "/"},
             "publisher": {"@id": SITE + "/#org"}, "mainEntityOfPage": SITE + path,
             "image": SITE + p.get("image", "/img/service-renovation.jpg")},
            breadcrumb([("Accueil", "/"), ("Journal", "/journal/"), (p["h1"], path)]),
            faq_jsonld(p["faq"]),
        ]
        page(path, p["title"], p["description"], body, ld, lastmod=p.get("updated", p["date"]), priority="0.7",
             og_type="article", image=p.get("image", "/img/service-renovation.jpg"))

    cartes = "".join(
        f'<a class="carte" href="/journal/{p["slug"]}.html"><span class="carte__cat">{esc(p["category"])}</span>'
        f'<h2>{esc(p["h1"])}</h2><p>{esc(p["description"])}</p><span class="carte__date">{fr_date(p["date"])}</span></a>'
        for p in POSTS)
    body = f"""
<main class="section page-texte">
  <div class="wrap">
    <nav class="fil" aria-label="Fil d'Ariane"><a href="/">Accueil</a> › Journal</nav>
    <h1 class="titre-page">Le Journal de l'atelier</h1>
    <p class="chapeau">Rénovation, copropriété, home staging, décoration : des réponses claires aux questions que l'on se pose avant de faire des travaux ou de vendre. Pour comparer les matériaux, voir <a href="/guides/">nos guides</a>.</p>
    <div class="cartes">{cartes}</div>
  </div>
</main>
{newsletter_block("journal-index")}"""
    page("/journal/", f"Journal : conseils rénovation, home staging et déco | {BRAND}",
         "Le Journal d'Ateliers W : conseils pratiques sur la rénovation, la copropriété, le home staging et la décoration à Paris.",
         body, [breadcrumb([("Accueil", "/"), ("Journal", "/journal/")])], priority="0.8")


# ---------------------------------------------------------------- sitemap & robots
def build_sitemap():
    urls = "".join(f"<url><loc>{SITE}{p}</loc><lastmod>{lm}</lastmod><priority>{pr}</priority></url>\n"
                   for p, lm, pr in PAGES)
    write("/sitemap.xml", f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}</urlset>\n')
    write("/robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")


def build_404():
    body = """
<main class="section page-texte"><div class="wrap texte">
<h1 class="titre-page">Page introuvable</h1>
<p>Cette page n'existe pas ou a été déplacée. <a href="/">Retour à l'accueil</a> ou <a href="/journal/">voir le Journal</a>.</p>
</div></main>"""
    write("/404.html", head(f"Page introuvable | {BRAND}", "Page introuvable.", "/404.html") + header() + body + footer())


def main():
    slugs = [g["slug"] for g in GUIDES] + [p["slug"] for p in POSTS]
    assert len(slugs) == len(set(slugs)), "slug en double"
    for p in POSTS:
        assert not p.get("guide") or p["guide"] in {g["slug"] for g in GUIDES}, f"guide inconnu : {p['guide']}"
    # anciennes pages supprimées
    for old in ["remboursement.html"]:
        fp = os.path.join(OUT, old)
        if os.path.exists(fp):
            os.remove(fp)
    build_home()
    build_contact()
    build_static_pages()
    build_guides()
    build_blog()
    build_404()
    build_sitemap()
    print(f"OK : {len(PAGES)} pages, {len(GUIDES)} guides, {len(POSTS)} articles")


if __name__ == "__main__":
    main()
