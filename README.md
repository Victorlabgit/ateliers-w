# Ateliers W

Site vitrine statique (HTML / CSS / JS) : rénovation et home staging, Paris et sud de la Corse.

## Structure

```
public/            ← tout ce qui est publié
  index.html       ← accueil (hero, Notre Entreprise, Nos Réalisations, contact)
  contact.html     ← page « Demandez un devis »
  confidentialite.html, accessibilite.html, conditions.html, remboursement.html
  css/style.css    ← couleurs et polices en haut du fichier (variables :root)
  js/main.js
render.yaml        ← configuration Render (site statique)
```

Les images sont pour l'instant appelées depuis les serveurs Wix (static.wixstatic.com). Pour être indépendant de Wix, téléchargez-les dans `public/assets/` et remplacez les URL dans `index.html` et `css/style.css`.

## Tester en local

```bash
cd public
python3 -m http.server 8000
# puis http://localhost:8000
```

## Publier : GitHub puis Render

1. Créer un dépôt vide sur GitHub (ex. `ateliers-w`), puis :
   ```bash
   git init && git add . && git commit -m "Premier jet du site"
   git branch -M main
   git remote add origin https://github.com/VOTRE-COMPTE/ateliers-w.git
   git push -u origin main
   ```
2. Sur Render : **New → Blueprint** (ou **Static Site**), choisir le dépôt.
   - Blueprint : Render lit `render.yaml` tout seul.
   - Static Site à la main : Build command vide, **Publish directory = `public`**.
3. Chaque `git push` sur `main` redéploie le site.
4. Domaine perso : Render → Settings → Custom Domains.

## À personnaliser avant la mise en ligne

- Formulaire : créer un formulaire sur formspree.io, puis remplacer `VOTRE_ID` dans `public/index.html` (attribut `action`).
- Coordonnées : e-mail et téléphone dans `index.html` (section Contact).
- Pages légales : compléter les quatre pages du pied de page.
- Photos : rapatrier les images Wix dans `public/assets/` (voir plus haut).
- Textes de remplacement : e-mail, téléphone, réseaux sociaux et témoignage viennent du modèle Wix.
