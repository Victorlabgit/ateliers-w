# Ateliers W

Site statique de l'entreprise Ateliers W (rénovation, home staging, design d'intérieur, communication immobilière — Paris).
Hébergement : GitHub Pages (branche main, dossier `docs/`), publié à chaque push sur `main` (1 à 3 min). DNS chez IONOS.

## Générer le site

```bash
python3 build.py      # régénère toutes les pages HTML dans docs/
rm -rf __pycache__
```

- `build.py` : gabarit, pages fixes, configuration (UMAMI_ID, NEWSLETTER_ACTION, SOCIAL, LEGAL, LINKS), sitemap, robots.
- `content.py` : guides comparatifs (`GUIDES`), publiés dans /guides/.
- `blog.py` : articles du Journal (`POSTS`), publiés dans /journal/.
- `docs/css/style.css`, `docs/js/main.js` : styles et scripts (le CSS est versionné ?v=hash).

Règles éditoriales : aucun nom de personne, jamais de prix / chiffres / avis / tests inventés, sources officielles citées,
liens affiliés signalés (rel="sponsored nofollow noopener"), qualité avant volume.
Ne pas supprimer les fichiers google*.html (vérification Search Console).
