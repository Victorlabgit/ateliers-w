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
        "slug": "declaration-prealable-de-travaux-quand-la-deposer",
        "title": "Déclaration préalable de travaux : quand la déposer ?",
        "h1": "Déclaration préalable de travaux : quand est-elle obligatoire ?",
        "description": "Fenêtres, volets, façade, extension : quand la déclaration préalable de travaux est obligatoire, comment la déposer à Paris et quels délais prévoir.",
        "date": "2026-11-28",
        "category": "Aides & règles",
        "read": 6,
        "guide": None,
        "image": "/img/og/declaration-prealable-de-travaux-quand-la-deposer.jpg",
        "answer": """<p>La <strong>déclaration préalable de travaux</strong> (DP) est obligatoire pour les travaux qui ne relèvent pas du permis de construire mais qui créent une petite surface, modifient l'aspect extérieur d'un bâtiment (fenêtres, volets, façade, toiture) ou changent la destination d'un local. Des travaux purement intérieurs, sans création de surface ni changement de destination, n'en demandent pas. La mairie dispose en principe d'un mois pour s'opposer au projet.</p>""",
        "body": """<p>Avant de changer des fenêtres, repeindre une façade ou transformer un local, la question de la déclaration préalable de travaux se pose presque toujours. C'est une autorisation d'urbanisme plus légère que le permis de construire, mais l'oublier peut bloquer un chantier ou compliquer une vente. Voici ce qu'en dit {{lien:Service-Public déclaration préalable|la fiche officielle de Service-Public}}, appliqué aux situations que nous rencontrons à Paris.</p>

<h2>Quels travaux sont soumis à déclaration préalable ?</h2>
<p>La DP concerne les travaux non soumis à permis de construire qui entraînent l'une de ces trois choses :</p>
<ul>
<li><strong>une création de surface de plancher ou d'emprise au sol</strong> de petite taille : agrandissement, véranda, terrasse, mezzanine, surélévation limitée. Au-delà de certains seuils, c'est un permis de construire ; la fiche officielle détaille ces seuils selon que la commune est couverte ou non par un plan local d'urbanisme ;</li>
<li><strong>une modification de l'aspect extérieur</strong> : remplacement de fenêtres ou de portes qui n'est pas à l'identique, volets, toiture, fenêtre de toit, balcon, isolation thermique par l'extérieur, ravalement qui change couleurs ou matériaux, boîtier extérieur de climatisation ou de pompe à chaleur, panneaux solaires ;</li>
<li><strong>un changement de destination</strong>, par exemple transformer un local commercial en logement, sans toucher aux structures porteuses ni à la façade.</li>
</ul>
<p>À l'inverse, refaire une cuisine, une salle de bains, abattre une cloison non porteuse ou changer un sol à l'intérieur d'un appartement ne demande pas d'autorisation d'urbanisme. En copropriété, d'autres règles s'ajoutent : voir notre article sur <a href="/journal/travaux-copropriete-faut-il-une-autorisation.html">l'autorisation de l'assemblée générale</a>.</p>

<h2>Façade et ravalement : le cas particulier</h2>
<p>Selon {{lien:Service-Public ravalement|Service-Public}}, un ravalement ou une remise en peinture <strong>à l'identique</strong> (même couleur, mêmes matériaux) est un simple entretien, dispensé d'autorisation. Dès que la couleur ou les matériaux changent, une DP est nécessaire. Elle l'est aussi dans tous les cas lorsque le bâtiment se trouve en <strong>secteur protégé</strong> (site patrimonial remarquable, abords d'un monument historique, site classé…), lorsqu'il est lui-même protégé au titre des monuments historiques, ou lorsque la commune a décidé de soumettre les ravalements à autorisation. L'isolation thermique par l'extérieur est, elle, toujours soumise à DP.</p>
<p>À Paris, une grande partie des immeubles se trouve dans des secteurs protégés : la vérification auprès du service de l'urbanisme est indispensable avant tout projet visible depuis la rue.</p>

<h2>Comment déposer la déclaration à Paris</h2>
<p>Le dossier comprend le formulaire officiel de déclaration préalable et des pièces graphiques : un plan de situation dans tous les cas, puis selon le projet un plan de masse, un plan en coupe, des plans de façades et de toitures s'ils sont modifiés, et des pièces complémentaires selon les cas.</p>
<p>Dans la plupart des communes, on peut déposer en ligne, par lettre recommandée ou en mairie contre récépissé. À Paris, Service-Public indique que le dépôt se fait <strong>uniquement par voie dématérialisée</strong>, sur le guichet électronique de la Ville. Un récépissé indique la date à partir de laquelle le délai court.</p>

<h2>Délais : combien de temps attendre ?</h2>
<p>Lorsque le dossier est complet, le délai d'instruction est de <strong>un mois</strong> à compter du dépôt. S'il manque des pièces, la mairie doit le signaler dans le premier mois ; vous avez alors trois mois pour compléter, faute de quoi la demande est rejetée, et le délai ne démarre qu'au dossier complet. Dans certains cas, notamment en secteur protégé, la mairie peut vous notifier un délai plus long : il faut alors l'intégrer au calendrier du chantier.</p>
<p>Sans réponse à la fin du délai, vous bénéficiez d'une <strong>décision tacite de non-opposition</strong>. Vous pouvez demander à la mairie un certificat qui l'atteste, utile notamment au moment d'une vente.</p>

<h2>Après l'accord : affichage, recours, validité</h2>
<ul>
<li><strong>Affichage</strong> : un panneau visible de l'extérieur doit être installé sur le terrain dès l'accord (ou dès la fin du délai d'instruction), pendant toute la durée des travaux.</li>
<li><strong>Recours des tiers</strong> : un voisin peut contester l'autorisation pendant deux mois à compter du premier jour d'affichage continu. Démarrer les travaux après ce délai limite le risque.</li>
<li><strong>Validité</strong> : l'autorisation est valable trois ans. Elle est périmée si les travaux ne commencent pas dans ce délai ou s'ils sont interrompus plus d'un an. Elle peut être prolongée deux fois d'un an, sur demande au moins deux mois avant son expiration.</li>
</ul>

<h2>Notre conseil avant de lancer le projet</h2>
<p>Listez ce qui, dans votre projet, se voit de l'extérieur ou change l'usage du lieu : c'est là que se trouve l'autorisation d'urbanisme. Pour un appartement en copropriété, comptez deux démarches distinctes, l'AG et la mairie, qui ne se remplacent pas. Pour un doute sur votre situation, le service de l'urbanisme de la mairie ou l'{{lien:ANIL|ADIL de votre département}} renseigne gratuitement. Si vous préparez une <a href="/renovation-appartement-paris.html">rénovation à Paris</a>, nous intégrons ces démarches au planning dès l'étude du projet : décrivez-le-nous via une <a href="/contact.html">demande de devis</a>.</p>""",
        "faq": [
            ("Faut-il une déclaration préalable pour changer ses fenêtres ?",
             "<p>Oui si le remplacement n'est pas à l'identique (forme, matériau, couleur ou découpage différents). Un remplacement strictement identique relève de l'entretien. En copropriété, l'accord de l'assemblée générale est aussi nécessaire, car les fenêtres touchent l'aspect extérieur de l'immeuble.</p>"),
            ("Des travaux intérieurs dans un appartement demandent-ils une déclaration préalable ?",
             "<p>Non, tant qu'ils ne créent pas de surface de plancher, ne changent pas la destination du local et ne modifient pas l'aspect extérieur. Cuisine, salle de bains, sols ou cloisons non porteuses n'en demandent pas.</p>"),
            ("Que se passe-t-il si la mairie ne répond pas ?",
             "<p>À la fin du délai d'instruction (un mois si le dossier est complet, sauf délai plus long notifié), le silence vaut décision tacite de non-opposition. Vous pouvez demander un certificat de non-opposition à la mairie.</p>"),
            ("Combien de temps une déclaration préalable est-elle valable ?",
             "<p>Trois ans. Elle peut être prolongée deux fois d'un an si les règles d'urbanisme n'ont pas changé, à condition de le demander au moins deux mois avant la fin de validité.</p>"),
        ],
        "sources": [
            ("Service-Public — Déclaration préalable (DP)", "https://www.service-public.gouv.fr/particuliers/vosdroits/F17578"),
            ("Service-Public — Quelle autorisation d'urbanisme pour ravaler ou repeindre une façade ?", "https://www.service-public.gouv.fr/particuliers/vosdroits/F36779"),
            ("Service-Public — Autorisations d'urbanisme", "https://www.service-public.gouv.fr/particuliers/vosdroits/N319"),
        ],
    },
    {
        "slug": "diagnostics-obligatoires-vente-appartement",
        "title": "Diagnostics obligatoires pour vendre un appartement",
        "h1": "Diagnostics obligatoires pour vendre un appartement : la liste",
        "description": "DPE, amiante, plomb, électricité, gaz, état des risques, loi Carrez : les diagnostics obligatoires pour vendre un appartement, leur validité, quand les fournir.",
        "date": "2026-11-27",
        "category": "Vendre / louer",
        "read": 6,
        "guide": None,
        "image": "/img/og/diagnostics-obligatoires-vente-appartement.jpg",
        "answer": """<p>Pour vendre un appartement, les diagnostics obligatoires sont réunis dans le <strong>dossier de diagnostic technique (DDT)</strong>, à remettre à l'acheteur dès la promesse de vente. Le DPE est toujours exigé ; les autres (amiante, plomb, électricité, gaz, termites, état des risques…) dépendent de l'âge de l'immeuble, de ses installations et de sa localisation. La surface Carrez doit aussi figurer dans la promesse et dans l'acte.</p>""",
        "body": """<p>Avant de mettre un appartement en vente, la question des diagnostics obligatoires arrive très vite, souvent en même temps que celle des petits travaux et de la préparation du bien. Voici la liste telle que la présentent {{lien:Service-Public diagnostics vente|Service-Public}} et l'{{lien:ANIL diagnostics|ANIL}}, avec les durées de validité à surveiller. Les règles évoluent : vérifiez toujours votre cas avec votre notaire et votre diagnostiqueur.</p>

<h2>Le DDT : un dossier à remettre dès la promesse</h2>
<p>Les diagnostics sont regroupés dans le dossier de diagnostic technique. Le vendeur le joint à la promesse (ou au compromis) de vente, ou, à défaut de promesse, à l'acte de vente. Concrètement, il vaut mieux le commander dès la mise en vente : le DPE doit de toute façon être disponible dès ce moment, puisque ses résultats doivent apparaître dans l'annonce.</p>
<p>Les diagnostics sont réalisés par un professionnel certifié et assuré, sans lien avec le vendeur ; un {{lien:Annuaire diagnostiqueurs|annuaire officiel}} permet de vérifier la certification. Seul l'état des risques peut être établi par le vendeur lui-même, éventuellement aidé d'un professionnel.</p>

<h2>Les diagnostics selon votre appartement</h2>
<ul>
<li><strong>DPE (diagnostic de performance énergétique)</strong> : toujours obligatoire. Valable 10 ans pour un DPE réalisé depuis le 1er juillet 2021 ; ceux réalisés avant cette date ne sont plus valables et doivent être refaits.</li>
<li><strong>Amiante</strong> : si le permis de construire de l'immeuble a été délivré avant le 1er juillet 1997. Un constat d'absence d'amiante n'a pas de limite de validité. En copropriété, il porte sur les parties privatives ; la fiche récapitulative du dossier technique amiante des parties communes se demande au syndic.</li>
<li><strong>Plomb (Crep)</strong> : si l'immeuble a été construit avant le 1er janvier 1949, ce qui concerne une grande partie des immeubles anciens parisiens. Il doit dater de moins d'un an à la signature, sauf s'il ne relève pas de plomb, auquel cas il n'est pas à refaire.</li>
<li><strong>Électricité</strong> et <strong>gaz</strong> : si l'installation intérieure a plus de 15 ans. Validité de 3 ans.</li>
<li><strong>Termites</strong> : si l'immeuble est dans une zone délimitée par arrêté préfectoral. Validité de 6 mois.</li>
<li><strong>État des risques</strong> : si le bien est situé dans une zone à risques (naturels, miniers, technologiques, sismicité, radon…). Il doit dater de moins de 6 mois. Le vendeur informe aussi des sinistres indemnisés au titre d'une catastrophe naturelle ou technologique.</li>
<li><strong>Bruit</strong> : si le logement est dans une zone d'exposition au bruit d'un aérodrome.</li>
<li><strong>Mérule</strong> : une information à donner dans les zones fixées par arrêté.</li>
<li><strong>Assainissement</strong> : selon les cas (installation autonome, ou contrôle du raccordement au réseau dans certaines communes d'Île-de-France listées par décret). Votre notaire sait si votre commune est concernée.</li>
<li><strong>Carnet d'information du logement</strong> : si des travaux de rénovation ou un permis / une déclaration préalable datent de 2023 ou après.</li>
</ul>
<p>L'audit énergétique, exigé pour certaines ventes de maisons ou d'immeubles en monopropriété mal classés, ne concerne pas la vente d'un lot de copropriété selon l'ANIL.</p>

<h2>Copropriété : la surface Carrez et les documents du syndic</h2>
<p>La superficie privative du lot (loi Carrez) doit figurer dans la promesse et dans l'acte de vente. Le mesurage par un professionnel est recommandé : une erreur peut avoir des conséquences sur le prix. S'y ajoutent les documents propres à la copropriété, à remettre au plus tard à la promesse : fiche synthétique, règlement de copropriété, procès-verbaux des trois dernières assemblées générales, carnet d'entretien, conclusions du diagnostic technique global et plan pluriannuel de travaux s'ils existent. Pensez aussi à vérifier que les travaux réalisés dans l'appartement avaient bien été autorisés lorsqu'ils le devaient (voir notre article sur les <a href="/journal/travaux-copropriete-faut-il-une-autorisation.html">travaux en copropriété et l'accord de l'AG</a>).</p>

<h2>DPE : ce qui change avec le nouveau calcul</h2>
<p>Selon la {{lien:Service-Public DPE|fiche officielle sur le DPE}}, le coefficient de conversion de l'électricité est passé de 2,3 à 1,9 le 1er janvier 2026, ce qui peut améliorer l'étiquette des logements chauffés à l'électricité. Un arrêté du 19 août 2026 l'abaisse encore à 1,7 au 1er janvier 2027. Le ministère indique que les DPE réalisés jusqu'au 31 décembre 2026 restent valables et pourront être mis à jour gratuitement, sans nouvelle visite, sur l'{{lien:Observatoire DPE ADEME|Observatoire DPE-Audit de l'ADEME}} à partir du 1er janvier 2027.</p>
<p>Dans l'annonce, les classes énergie et climat doivent apparaître de façon lisible, avec l'estimation des dépenses annuelles d'énergie ; un logement classé F ou G porte la mention « logement à consommation énergétique excessive ».</p>

<h2>Que se passe-t-il si un diagnostic manque ?</h2>
<p>Si un diagnostic obligatoire n'est pas fourni à la signature de l'acte, le vendeur ne peut pas s'exonérer de la garantie des vices cachés correspondante, même avec une clause d'exonération dans l'acte. Pour l'état des risques, l'acheteur peut demander l'annulation de la vente ou une diminution du prix. Mieux vaut donc un dossier complet et à jour avant les premières visites.</p>

<h2>Préparer la vente au-delà des diagnostics</h2>
<p>Les diagnostics décrivent le bien ; ils ne le mettent pas en valeur. Un DPE ou un constat électrique peut pointer des défauts qu'un acheteur intégrera dans sa négociation. Avant la mise en vente, il est souvent utile de faire le tri : ce qui mérite d'être réparé, ce qui relève simplement d'une remise en état, et ce qui se règle par une mise en scène soignée et de bonnes photos d'annonce. C'est le cœur de notre travail en <a href="/home-staging-paris.html">home staging</a>, en <a href="/photos-immobilieres-paris.html">photos immobilières</a> et en <a href="/renovation-appartement-paris.html">rénovation</a> : si vous préparez une vente à Paris, <a href="/contact.html">demandez-nous un devis</a> et nous regarderons ensemble ce qui vaut la peine d'être fait.</p>""",
        "faq": [
            ("Qui paie les diagnostics lors d'une vente ?",
             "<p>Le vendeur : c'est à lui de fournir le dossier de diagnostic technique. Le prix des diagnostics n'est pas réglementé, il varie selon le bien et les diagnostics nécessaires : comparez plusieurs devis de diagnostiqueurs certifiés.</p>"),
            ("Combien de temps le DPE est-il valable pour vendre ?",
             "<p>Dix ans pour un DPE réalisé depuis le 1er juillet 2021. Les DPE réalisés avant cette date ne sont plus valables et doivent être refaits avant la vente.</p>"),
            ("Faut-il un audit énergétique pour vendre un appartement ?",
             "<p>Selon l'ANIL, non pour un lot de copropriété : l'audit énergétique vise la vente de maisons individuelles ou d'immeubles en monopropriété mal classés.</p>"),
            ("Peut-on signer la promesse sans tous les diagnostics ?",
             "<p>Le DDT doit être joint à la promesse. S'il est incomplet à la signature de l'acte, le vendeur reste tenu de la garantie des vices cachés correspondante. Pour l'état des risques, l'acheteur peut demander l'annulation ou une baisse du prix.</p>"),
            ("La surface Carrez est-elle un diagnostic ?",
             "<p>C'est une mention obligatoire de la promesse et de l'acte pour un lot de copropriété. Elle fait partie des éléments à fournir ; le mesurage par un professionnel est recommandé.</p>"),
        ],
        "sources": [
            ("Service-Public — Quels sont les diagnostics immobiliers à fournir en cas de vente d'un logement ?", "https://www.service-public.gouv.fr/particuliers/vosdroits/F10798"),
            ("Service-Public — Diagnostic de performance énergétique (DPE)", "https://www.service-public.gouv.fr/particuliers/vosdroits/F16096"),
            ("ANIL — Les différents diagnostics pour devenir propriétaire", "https://www.anil.org/votre-besoin/acheter/diagnostics/quels-diagnostics/"),
            ("Service-Public — Vente d'un logement en copropriété", "https://www.service-public.gouv.fr/particuliers/vosdroits/F2604"),
            ("Ministère de la Transition écologique — Facteur de conversion de l'électricité à 1,7 au 1er janvier 2027", "https://www.ecologie.gouv.fr/presse/dpe-audits-energetiques-publication-larrete-abaissant-facteur-conversion-lelectricite-17-1er"),
        ],
    },
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
<p>Classez chaque poste de votre projet : privatif, partie commune ou aspect extérieur. Une <a href="/renovation-appartement-paris.html">rénovation de cuisine ou de salle de bains</a> sans toucher aux colonnes ni aux murs porteurs se lance en général rapidement ; dès qu'un mur porteur ou une façade entre en jeu, le calendrier se construit autour de l'AG. Pour choisir les finitions de la cuisine en attendant, voyez notre <a href="/guides/plan-de-travail-cuisine-quel-materiau-choisir.html">comparatif des plans de travail</a>. Pour un cas particulier, l'{{lien:ANIL|ADIL de votre département}} renseigne gratuitement.</p>""",
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
