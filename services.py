"""Pages services d'Ateliers W (une page par métier, ciblée « <service> Paris »).

Chaque service : slug, name (court, pour les menus), title (<60 car.), h1, description (140-160 car.),
image (photo réelle /img/...), alt, intro (HTML), sections [(h2, HTML)], faq [(question, réponse HTML)],
related (liens internes [(texte, url)]).

Règles : aucun nom de personne, jamais de prix, délais chiffrés, avis ou réalisations inventés ;
les règles citées renvoient vers nos articles ou des sources officielles ({{lien:Clé}}).
"""

SERVICES = [
    {
        "slug": "renovation-appartement-paris",
        "name": "Rénovation",
        "title": "Rénovation d'appartement à Paris | Ateliers W",
        "h1": "Rénovation d'appartement à Paris",
        "description": "Rénovation d'appartement à Paris : cuisine, salle de bains, sols, peinture, redistribution. Nos artisans réalisent tout, du gros œuvre aux finitions.",
        "image": "/img/service-renovation.jpg",
        "alt": "Cuisine rénovée avec îlot central",
        "intro": """<p>Rénover un appartement à Paris, c'est composer avec la copropriété, des volumes souvent contraints et des immeubles anciens. {BRAND} est une entreprise d'artisans : nous concevons le projet avec vous puis nous le réalisons nous-mêmes, du gros œuvre aux finitions, sans sous-traiter la coordination à un intermédiaire.</p>
<p>Rénovation complète ou partielle, pour y vivre, louer ou vendre : vous avez un seul interlocuteur, un devis détaillé poste par poste et un chantier suivi de bout en bout.</p>""",
        "sections": [
            ("Ce que nous rénovons", """<ul>
<li><strong>Cuisine</strong> : dépose, réseaux, pose des meubles, plan de travail et crédence. Pour choisir le plan de travail, voyez notre <a href="/guides/plan-de-travail-cuisine-quel-materiau-choisir.html">comparatif des matériaux</a>.</li>
<li><strong>Salle de bains et WC</strong> : douche ou baignoire, faïence, carrelage, meuble vasque, ventilation.</li>
<li><strong>Sols et murs</strong> : parquet, carrelage, ragréage, enduits, peinture.</li>
<li><strong>Redistribution des pièces</strong> : cloisons, ouvertures, cuisine ouverte, verrière, rangements sur mesure.</li>
<li><strong>Électricité et plomberie</strong> dans le cadre de la rénovation des pièces concernées.</li>
<li><strong>Intérieur et extérieur</strong> : nous intervenons aussi sur les espaces extérieurs et les petits travaux de construction.</li>
</ul>"""),
            ("Comment se déroule une rénovation avec nous", """<ol class="etapes">
<li><strong>Visite et écoute.</strong> Nous voyons le logement, vos usages et votre objectif (habiter, louer, vendre).</li>
<li><strong>Conception.</strong> Plan, choix des matériaux, couleurs et ambiance. Si vous le souhaitez, notre service de <a href="/design-interieur-paris.html">design d'intérieur</a> prend le relais sur l'aménagement et le décor.</li>
<li><strong>Devis détaillé.</strong> Chaque poste est chiffré séparément, pour que vous puissiez arbitrer.</li>
<li><strong>Chantier sans intermédiaire.</strong> Nos artisans réalisent les travaux et vous tiennent informé de l'avancement.</li>
<li><strong>Réception et finitions.</strong> Nous faisons le tour du chantier avec vous avant de le clore.</li>
</ol>"""),
            ("Copropriété et autorisations : ce qu'il faut vérifier avant", """<p>À Paris, la plupart des appartements sont en copropriété. Les travaux purement privatifs se lancent en général sans vote, mais tout ce qui touche aux parties communes (mur porteur, colonnes, façade, fenêtres visibles de l'extérieur) passe par l'assemblée générale. Nous expliquons la règle en détail dans <a href="/journal/travaux-copropriete-faut-il-une-autorisation.html">travaux en copropriété : faut-il une autorisation ?</a>, avec les sources officielles. Nous vous aidons à identifier ces points dès la visite, pour construire un calendrier réaliste.</p>"""),
            ("Rénover avant de vendre ou de louer", """<p>Avant une mise en vente, il n'est pas toujours utile de tout refaire : quelques travaux bien choisis, puis une <a href="/home-staging-paris.html">mise en scène</a> et de <a href="/photos-immobilieres-paris.html">belles photos</a>, suffisent souvent à présenter le bien sous son meilleur jour. Pensez aussi aux <a href="/journal/diagnostics-obligatoires-vente-appartement.html">diagnostics obligatoires</a>, notamment le DPE, qui peut orienter le choix des travaux.</p>"""),
        ],
        "faq": [
            ("Combien coûte la rénovation d'un appartement à Paris ?",
             "<p>Le coût dépend de la surface, de l'état du logement, des pièces concernées, des matériaux et des contraintes de l'immeuble. Nous ne donnons pas de prix au mètre carré générique : nous établissons un devis détaillé après visite.</p>"),
            ("Faites-vous les travaux vous-mêmes ?",
             "<p>Oui. {BRAND} est une entreprise d'artisans : nous réalisons les travaux, du gros œuvre aux finitions, sans intermédiaire.</p>"),
            ("Pouvez-vous rénover seulement une pièce ?",
             "<p>Oui, nous intervenons aussi bien sur une rénovation complète que sur une cuisine, une salle de bains ou des sols seuls.</p>"),
            ("Faut-il l'accord de la copropriété ?",
             "<p>Pas pour des travaux purement privatifs, mais oui dès que les parties communes ou l'aspect extérieur sont touchés. Voir notre article <a href=\"/journal/travaux-copropriete-faut-il-une-autorisation.html\">travaux en copropriété</a>.</p>"),
        ],
    },
    {
        "slug": "home-staging-paris",
        "name": "Home staging",
        "title": "Home staging à Paris : valoriser son bien | Ateliers W",
        "h1": "Home staging à Paris",
        "description": "Home staging à Paris : désencombrer, rafraîchir et mettre en scène un appartement pour la vente ou la location, puis le photographier. Demandez un devis.",
        "image": "/img/service-home-staging.jpg",
        "alt": "Salon mis en scène pour une vente",
        "intro": """<p>Le home staging consiste à préparer un logement pour qu'il plaise au plus grand nombre d'acheteurs ou de locataires : on désencombre, on dépersonnalise, on répare ce qui se voit et on met en valeur les volumes et la lumière. Le but n'est pas de décorer à son goût, mais d'aider les visiteurs à se projeter.</p>
<p>Chez {BRAND}, le home staging s'appuie sur nos autres métiers : nos artisans font les petits travaux de remise en état, puis nous mettons en scène et nous <a href="/photos-immobilieres-paris.html">photographions le bien</a> pour l'annonce.</p>""",
        "sections": [
            ("Ce que comprend notre home staging", """<ul>
<li><strong>Diagnostic du bien</strong> : ce qui freine la projection (encombrement, couleurs marquées, défauts visibles, éclairage).</li>
<li><strong>Petits travaux</strong> : peinture, joints, luminaires, poignées, réparations visibles, réalisés par nos artisans.</li>
<li><strong>Mise en scène</strong> : réorganisation du mobilier, linge, accessoires, éclairage, pour un intérieur neutre et chaleureux.</li>
<li><strong>Images</strong> : photos et visuels pour l'annonce, avant / après si utile.</li>
</ul>"""),
            ("Pour qui ?", """<ul>
<li><strong>Vendeurs</strong> d'un appartement occupé ou vide, qui veulent une annonce plus attractive.</li>
<li><strong>Propriétaires bailleurs</strong> qui préparent une mise en location.</li>
<li><strong>Agences et professionnels de l'immobilier</strong> qui cherchent un partenaire unique pour remettre en état, mettre en scène et photographier.</li>
</ul>"""),
            ("Home staging ou rénovation ?", """<p>Le home staging travaille la présentation, la <a href="/renovation-appartement-paris.html">rénovation</a> transforme le logement. Entre les deux, il y a souvent un juste milieu : quelques travaux ciblés (peinture claire, sol rafraîchi, cuisine remise en état) avant la mise en scène. Pour une cuisine, un plan de travail sobre et clair suffit souvent : voyez notre <a href="/guides/plan-de-travail-cuisine-quel-materiau-choisir.html">comparatif des plans de travail</a>.</p>"""),
            ("Avant la mise en vente", """<p>Préparez les documents en parallèle : le dossier de <a href="/journal/diagnostics-obligatoires-vente-appartement.html">diagnostics obligatoires</a> doit être prêt dès la promesse, et la classe énergie (DPE) figure obligatoirement dans l'annonce.</p>"""),
        ],
        "faq": [
            ("Le home staging fait-il vendre plus vite ?",
             "<p>Un bien bien présenté et bien photographié attire davantage de visites, mais aucun professionnel honnête ne peut garantir un délai ou un prix de vente : ils dépendent aussi du marché, de l'emplacement et du prix demandé.</p>"),
            ("Peut-on faire du home staging dans un appartement habité ?",
             "<p>Oui. On travaille alors surtout sur le désencombrement, la réorganisation du mobilier, la lumière et les petites réparations.</p>"),
            ("Quelle différence avec la décoration d'intérieur ?",
             "<p>La décoration vise votre goût à vous ; le home staging vise celui du plus grand nombre de futurs occupants. Pour votre propre intérieur, voyez notre service de <a href=\"/design-interieur-paris.html\">design d'intérieur</a>.</p>"),
            ("Combien coûte un home staging ?",
             "<p>Cela dépend de la surface, de l'état du bien et de ce qu'il faut prévoir (travaux, mobilier, photos). Nous établissons un devis après visite.</p>"),
        ],
    },
    {
        "slug": "design-interieur-paris",
        "name": "Design d'intérieur",
        "title": "Design et décoration d'intérieur à Paris | Ateliers W",
        "h1": "Design d'intérieur à Paris",
        "description": "Design et décoration d'intérieur à Paris : plan, couleurs, matières, lumière et ambiance, puis réalisation par nos artisans. Du projet à la pose.",
        "image": "/img/service-design-interieur.jpg",
        "alt": "Chambre au décor soigné",
        "intro": """<p>Repenser un intérieur, c'est d'abord comprendre comment vous y vivez. Notre service de design d'intérieur travaille le plan, les couleurs, les matières, la lumière et les rangements pour créer une ambiance cohérente, adaptée aux volumes parisiens.</p>
<p>La différence {BRAND} : le projet ne reste pas sur le papier. Nos artisans le réalisent, ce qui évite les allers-retours entre un concepteur et des entreprises séparées.</p>""",
        "sections": [
            ("Ce que nous concevons", """<ul>
<li><strong>Aménagement et plan</strong> : circulation, cuisine ouverte ou non, verrière, mezzanine, optimisation des petites surfaces.</li>
<li><strong>Couleurs et matières</strong> : peintures, sols, revêtements muraux, plans de travail, textiles.</li>
<li><strong>Lumière</strong> : éclairage général, d'ambiance et fonctionnel, mise en valeur de la lumière naturelle.</li>
<li><strong>Rangements sur mesure</strong> : placards, bibliothèques, dressing, niches.</li>
<li><strong>Mobilier et décor</strong> : sélection et agencement pour une ambiance cohérente.</li>
</ul>"""),
            ("Du projet à la réalisation", """<ol class="etapes">
<li><strong>Rencontre</strong> : vos usages, vos goûts, votre budget, les contraintes du logement.</li>
<li><strong>Proposition</strong> : plan, palette de couleurs et de matériaux, ambiance.</li>
<li><strong>Devis</strong> : travaux et fournitures détaillés poste par poste.</li>
<li><strong>Réalisation</strong> par nos artisans : voyez notre page <a href="/renovation-appartement-paris.html">rénovation d'appartement</a>.</li>
</ol>"""),
            ("Bien choisir ses matériaux", """<p>Nos guides comparatifs vous aident à trancher avant de vous engager, sans jamais avancer de prix ni de tests inventés. Commencez par le <a href="/guides/plan-de-travail-cuisine-quel-materiau-choisir.html">plan de travail de cuisine</a>, et retrouvez tous nos <a href="/guides/">guides</a>.</p>"""),
        ],
        "faq": [
            ("Faut-il forcément faire des travaux ?",
             "<p>Non. Un projet de décoration peut se limiter aux couleurs, à la lumière, au mobilier et aux textiles. Quand des travaux sont utiles, nos artisans les réalisent.</p>"),
            ("Travaillez-vous sur les petites surfaces ?",
             "<p>Oui : studios et petits appartements parisiens sont justement ceux où un bon plan et des rangements sur mesure font la plus grande différence.</p>"),
            ("Comment est établi le prix ?",
             "<p>Selon l'étendue du projet (conception seule ou conception et travaux), la surface et les fournitures. Nous établissons un devis après un premier échange.</p>"),
        ],
    },
    {
        "slug": "photos-immobilieres-paris",
        "name": "Communication immobilière",
        "title": "Photos immobilières et annonce à Paris | Ateliers W",
        "h1": "Photos immobilières et communication à Paris",
        "description": "Photos immobilières à Paris : préparation du bien, photos d'annonce, visuels avant / après et aide à la rédaction de l'annonce, pour vendre ou louer.",
        "image": "/img/service-communication-immobiliere.jpg",
        "alt": "Séjour et cuisine ouverte photographiés pour une annonce",
        "intro": """<p>Sur les portails immobiliers, les photos sont la première visite. Notre service de communication immobilière prépare le bien, le photographie et produit les visuels de l'annonce, pour que les acheteurs ou locataires aient envie de venir le voir.</p>
<p>Parce que nous faisons aussi la <a href="/renovation-appartement-paris.html">rénovation</a> et le <a href="/home-staging-paris.html">home staging</a>, nous pouvons remettre en état et mettre en scène avant la séance photo, au lieu de photographier le bien tel quel.</p>""",
        "sections": [
            ("Ce que nous réalisons", """<ul>
<li><strong>Préparation</strong> : rangement, mise en scène, lumière, petites réparations visibles.</li>
<li><strong>Photos d'annonce</strong> : pièces principales, volumes, lumière naturelle, détails qui font la différence.</li>
<li><strong>Visuels avant / après</strong> pour montrer le potentiel d'un bien ou le résultat d'une rénovation.</li>
<li><strong>Aide à l'annonce</strong> : mise en avant des points forts, informations à ne pas oublier.</li>
</ul>"""),
            ("Les mentions obligatoires d'une annonce", """<p>Une annonce de vente ou de location doit notamment indiquer la classe énergie issue du DPE ; la fiche {{lien:Service-Public DPE|Service-Public sur le DPE}} détaille les règles en vigueur. Pour la vente, le dossier de <a href="/journal/diagnostics-obligatoires-vente-appartement.html">diagnostics obligatoires</a> doit aussi être prêt.</p>"""),
            ("Pour les particuliers et les professionnels", """<p>Nous travaillons pour des propriétaires qui vendent ou louent eux-mêmes comme pour des agences et des professionnels de l'immobilier qui veulent un partenaire capable de préparer, mettre en scène et photographier.</p>"""),
        ],
        "faq": [
            ("Pourquoi ne pas prendre les photos soi-même ?",
             "<p>C'est possible, mais la préparation du bien, la lumière et le cadrage font une grande différence sur la façon dont un logement est perçu en ligne. C'est là que nous intervenons.</p>"),
            ("Pouvez-vous préparer le bien avant les photos ?",
             "<p>Oui : rangement, mise en scène et petites réparations peuvent être faits juste avant la séance, grâce à nos services de <a href=\"/home-staging-paris.html\">home staging</a> et de rénovation.</p>"),
            ("Combien coûte une séance photo immobilière ?",
             "<p>Cela dépend de la surface, du nombre de visuels et de la préparation nécessaire. Nous établissons un devis selon votre bien.</p>"),
        ],
    },
]
