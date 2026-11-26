"""Journal (blog) d'Ateliers W.

Chaque article : slug, title (<60 car.), h1, description (140-160 car.), date (ISO, Europe/Paris),
category (Rénovation, Copropriété, Home staging, Décoration, Vendre / louer, Aides & règles),
read (minutes), guide (slug d'un guide de content.py ou None), image (optionnel),
answer (HTML : réponse directe en 2-3 phrases), body (HTML : 4-6 <h2>), faq [(q, réponse HTML)],
sources [(titre, url)] — sources officielles uniquement.

Liens sortants : {{lien:Clé}} ou {{lien:Clé|texte}} (Clé dans LINKS de build.py).
Liens internes : <a href="/guides/<slug>.html"> et <a href="/journal/<slug>.html">.
Règles : 600 à 1 100 mots, jamais de prix / chiffres / avis inventés, aucun nom de personne.
Insérer les nouveaux articles EN HAUT de la liste.
"""

POSTS = [
    {
        "slug": "travaux-copropriete-faut-il-une-autorisation",
        "title": "Travaux en copropriété : faut-il une autorisation ?",
        "h1": "Travaux en copropriété : faut-il une autorisation de l'AG ?",
        "description": "Cuisine, cloison, fenêtres, mur porteur : quels travaux dans un appartement en copropriété exigent l'accord de l'assemblée générale, et comment le demander.",
        "date": "2026-11-26",
        "category": "Copropriété",
        "read": 6,
        "guide": "plan-de-travail-cuisine-quel-materiau-choisir",
        "answer": """<p>Dans les parties privatives de votre appartement (cloisons non porteuses, revêtements, cuisine, salle de bains), vous pouvez en principe faire des travaux <strong>sans autorisation</strong> de l'assemblée générale. Il faut en revanche son accord <strong>avant</strong> de commencer dès que les travaux touchent les parties communes (mur porteur, canalisations communes) ou l'aspect extérieur de l'immeuble (fenêtres, volets, climatisation).</p>""",
        "body": """<p>À Paris, la grande majorité des appartements sont en copropriété. Avant de lancer une rénovation, la question revient toujours : faut-il passer par l'assemblée générale (AG) ? La réponse dépend de ce que touchent les travaux. Voici la règle, telle que la présente {{lien:Service-Public copropriété|Service-Public}}, et la façon dont nous l'appliquons en préparant un chantier.</p>

<h2>Les travaux libres : vos parties privatives</h2>
<p>Les parties privatives sont celles réservées à votre usage exclusif, telles que les définit le règlement de copropriété. On y trouve généralement les cloisons non porteuses, les portes intérieures, les revêtements de sol et de mur, les installations électriques et de plomberie intérieures, les aménagements comme la cuisine ou la salle de bains.</p>
<p>Pour ces travaux, aucune autorisation de l'AG n'est nécessaire en principe. Deux limites s'appliquent toutefois :</p>
<ul>
<li><strong>la destination de l'immeuble et le règlement de copropriété</strong> : transformer un logement en local commercial, par exemple, sort du cadre ;</li>
<li><strong>les droits des autres copropriétaires</strong> : des travaux qui dégradent l'isolation phonique (remplacer une moquette par un parquet moins isolant, par exemple) ou qui causent un dommage chez un voisin peuvent poser problème.</li>
</ul>
<p>Dans ces deux cas, la loi exige l'accord de l'AG à l'unanimité. En pratique, pour un changement de sol, vérifiez les clauses acoustiques du règlement avant de choisir le revêtement.</p>

<h2>Les travaux qui touchent les parties communes</h2>
<p>Le gros œuvre (murs porteurs, planchers, structure), les canalisations communes et les équipements partagés sont des parties communes, même lorsqu'ils traversent votre appartement. Ouvrir un mur porteur pour créer une cuisine ouverte, déplacer une évacuation raccordée à une colonne commune : ces travaux nécessitent l'<strong>autorisation de l'assemblée générale avant le début du chantier</strong>.</p>
<p>Le vote se fait en général à la majorité absolue (article 25 de la loi de 1965). Si les travaux conduisent à s'approprier ou à détruire une partie commune, c'est la double majorité de l'article 26 qui s'applique. Point important : ni le syndic ni le conseil syndical ne peuvent donner cette autorisation à la place de l'AG.</p>
<p>Pour un mur porteur, l'AG demandera presque toujours une étude d'un bureau d'études structure. Prévoyez-la dans votre calendrier.</p>

<h2>Les travaux qui modifient l'aspect extérieur</h2>
<p>Fenêtres, volets, garde-corps, grilles, sortie de hotte en façade, unité extérieure de climatisation : tout ce qui se voit de l'extérieur relève aussi de l'AG, à la majorité absolue. Le règlement peut en plus contenir une clause d'harmonie (couleur des volets, modèle de menuiseries) qu'il faut respecter.</p>
<p>Certains de ces travaux demandent également une autorisation d'urbanisme auprès de la mairie, par exemple un changement de fenêtres qui n'est pas un remplacement à l'identique, une nouvelle ouverture ou un changement de couleur des volets. À Paris, les règles locales et les secteurs protégés rendent cette vérification indispensable.</p>

<h2>Comment demander l'autorisation à l'AG</h2>
<ol>
<li><strong>Relisez le règlement de copropriété</strong> : il ne doit pas interdire les travaux envisagés.</li>
<li><strong>Écrivez au syndic par lettre recommandée avec accusé de réception</strong> pour demander l'inscription de votre projet à l'ordre du jour de la prochaine AG. Vous pouvez aussi demander une AG spécifique, mais ses frais sont alors entièrement à votre charge.</li>
<li><strong>Joignez un dossier complet</strong> : descriptif des travaux, plans, devis, et pour un mur porteur l'étude structure. Un dossier clair facilite le vote.</li>
<li><strong>Attendez le vote avant de commencer</strong>. En cas de refus, vous disposez de deux mois après réception du procès-verbal pour le contester devant le tribunal judiciaire (avocat obligatoire).</li>
</ol>
<p>Comptez donc avec le calendrier des assemblées générales : si l'AG annuelle vient de passer, l'attente peut être longue. C'est l'une des premières choses que nous vérifions avec nos clients.</p>

<h2>Et si l'on fait les travaux sans autorisation ?</h2>
<p>Les travaux sont alors irréguliers. Le syndicat des copropriétaires peut exiger l'arrêt du chantier et la remise en état, au besoin par une action en justice, ce qui peut aller jusqu'à la démolition. Une régularisation après coup par l'AG reste possible, mais rien ne la garantit. Au moment de la vente, des travaux non autorisés peuvent aussi inquiéter l'acheteur et son notaire.</p>

<h2>Notre conseil avant une rénovation en copropriété</h2>
<p>Classez chaque poste de votre projet : privatif, partie commune ou aspect extérieur. Une rénovation de cuisine ou de salle de bains sans toucher aux colonnes ni aux murs porteurs se lance en général rapidement ; dès qu'un mur porteur ou une façade entre en jeu, le calendrier se construit autour de l'AG. Pour choisir les finitions de la cuisine en attendant, voyez notre <a href="/guides/plan-de-travail-cuisine-quel-materiau-choisir.html">comparatif des plans de travail</a>. Pour un cas particulier, l'{{lien:ANIL|ADIL de votre département}} renseigne gratuitement.</p>""",
        "faq": [
            ("Faut-il prévenir le syndic pour refaire sa cuisine ?",
             "<p>Pas d'autorisation à demander si les travaux restent dans vos parties privatives. Prévenir le syndic et les voisins du calendrier du chantier reste une bonne pratique, et le règlement peut fixer des horaires pour les travaux bruyants. Si vous touchez une évacuation commune, l'accord de l'AG est nécessaire.</p>"),
            ("Peut-on abattre une cloison sans autorisation ?",
             "<p>Oui s'il s'agit d'une cloison non porteuse située dans vos parties privatives. Faites vérifier qu'elle n'est pas porteuse avant de démolir : en cas de doute, un professionnel ou un bureau d'études tranche.</p>"),
            ("Quelle majorité pour ouvrir un mur porteur ?",
             "<p>En général la majorité absolue de l'article 25 de la loi de 1965. Si les travaux entraînent l'appropriation ou la destruction de parties communes, c'est la double majorité de l'article 26.</p>"),
            ("Changer ses fenêtres en copropriété : qui décide ?",
             "<p>L'assemblée générale, à la majorité absolue, car les fenêtres touchent l'aspect extérieur. Une autorisation d'urbanisme peut aussi être nécessaire si le remplacement n'est pas à l'identique.</p>"),
        ],
        "sources": [
            ("Service-Public — Copropriété : travaux dans l'appartement du propriétaire occupant", "https://www.service-public.gouv.fr/particuliers/vosdroits/F31513"),
            ("ANIL — Travaux en copropriété, de la prise de décision à la réalisation", "https://www.anil.org/votre-projet/vous-etes-proprietaire/copropriete/travaux-de-la-prise-de-decision-a-la-realisation/"),
        ],
    },
]
