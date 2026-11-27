"""Guides comparatifs d'Ateliers W.

Chaque guide : slug, title (<60 car.), h1, description (140-160 car.), date (ISO),
updated (ISO, optionnel), read (minutes), image (optionnel, chemin /img/...),
intro (HTML), verdict (HTML), options (liste : id, name, best_for, watch, body, pros, cons),
how_to_choose (HTML), faq [(question, réponse HTML)], sources [(titre, url)], cta (optionnel).

Liens sortants : {{lien:Clé}} ou {{lien:Clé|texte}} avec Clé dans LINKS (build.py).
Règles : jamais de prix, chiffres, avis ou tests inventés ; sources officielles ; aucun nom de personne.
Insérer les nouveaux guides EN HAUT de la liste.
"""

GUIDES = [
    {
        "slug": "revetement-de-sol-parquet-stratifie-vinyle-carrelage",
        "title": "Revêtement de sol : parquet, stratifié, vinyle, carrelage",
        "h1": "Revêtement de sol : parquet, stratifié, vinyle ou carrelage ?",
        "description": "Parquet massif ou contrecollé, stratifié, vinyle, carrelage : quel revêtement de sol choisir pour un appartement à Paris ? Le comparatif, pièce par pièce.",
        "date": "2026-11-27",
        "read": 9,
        "image": "/img/og/revetement-de-sol-parquet-stratifie-vinyle-carrelage.jpg",
        "intro": """<p>Le revêtement de sol, c'est ce que l'on voit en premier en entrant dans une pièce, et ce que l'on use tous les jours. En appartement parisien, le choix se joue sur quatre critères : la pièce (sèche ou humide), le bruit transmis aux voisins du dessous, l'entretien que vous êtes prêt à faire et la durée pendant laquelle vous comptez garder le logement.</p>
<p>Voici les cinq familles que nous posons le plus souvent en rénovation, avec leurs vrais points forts et leurs limites. Nous ne donnons pas de prix au mètre carré : ils dépendent du produit, de l'état du support, de la sous-couche, des seuils et plinthes, et de la pose. Avant de remplacer un sol en copropriété, lisez aussi <a href="/journal/travaux-copropriete-faut-il-une-autorisation.html">travaux en copropriété : faut-il une autorisation ?</a></p>""",
        "verdict": """<ul>
<li><strong>Séjour et chambres, logement gardé longtemps :</strong> le parquet massif, qui se ponce et se rénove.</li>
<li><strong>Rendu bois authentique, pose plus simple :</strong> le parquet contrecollé.</li>
<li><strong>Budget serré, location ou préparation d'une vente :</strong> le stratifié, avec une {{lien:Amazon sous-couche acoustique|sous-couche acoustique}} adaptée.</li>
<li><strong>Cuisine, entrée, salle de bains sans carrelage :</strong> le vinyle (lames ou rouleau).</li>
<li><strong>Salle de bains, douche à l'italienne, pièces très sollicitées :</strong> le carrelage en grès cérame.</li>
</ul>""",
        "options": [
            {
                "id": "parquet-massif",
                "name": "Parquet massif",
                "best_for": "Séjours et chambres, appartements anciens, logement gardé longtemps",
                "watch": "Eau stagnante, variations d'humidité, rayures des pieds de meubles",
                "body": """<p>Chaque lame est taillée dans une seule épaisseur de bois (chêne le plus souvent). C'est le sol des appartements haussmanniens : point de Hongrie, bâtons rompus, lames droites. Son grand atout est sa longévité : un parquet massif usé se ponce et se vitrifie ou se huile à nouveau, plusieurs fois au cours de sa vie.</p>
<p>Il reste un matériau vivant, sensible à l'eau et aux écarts d'humidité : on l'évite dans la salle de bains et on le nettoie avec une serpillière bien essorée. Des {{lien:Amazon patins feutre|patins en feutre}} sous les chaises limitent les rayures. Si vous avez déjà un parquet ancien sous une moquette, sa rénovation est souvent plus intéressante qu'un remplacement.</p>""",
                "pros": ["Très durable, se ponce et se rénove plusieurs fois", "Matériau noble, valorise un bien ancien", "Grand choix de poses (bâtons rompus, point de Hongrie…)"],
                "cons": ["Sensible à l'eau et à l'humidité", "Pose plus longue, souvent collée ou clouée", "Bruits de pas si la pose n'intègre pas d'isolation"],
            },
            {
                "id": "parquet-contrecolle",
                "name": "Parquet contrecollé",
                "best_for": "Rendu bois véritable avec une pose plus rapide, y compris flottante",
                "watch": "Épaisseur de la couche d'usure : elle conditionne les ponçages possibles",
                "body": """<p>Le contrecollé associe une couche supérieure en bois noble (la couche d'usure) à un support en bois ou en panneau. En surface, c'est du vrai bois ; dessous, la structure en couches le rend plus stable que le massif face aux variations d'humidité.</p>
<p>Il se pose collé ou flottant (clipsé sur une sous-couche), ce qui le rend adapté à la rénovation. Le point à vérifier est l'épaisseur de la couche d'usure indiquée par le fabricant : plus elle est épaisse, plus le parquet pourra être poncé un jour. Certaines couches très fines ne se poncent pas.</p>""",
                "pros": ["Vrai bois en surface", "Plus stable que le massif", "Pose flottante possible, rapide en rénovation"],
                "cons": ["Nombre de ponçages limité par la couche d'usure", "Craint l'eau stagnante comme tout parquet", "Sonorité « creuse » en pose flottante sans bonne sous-couche"],
            },
            {
                "id": "stratifie",
                "name": "Stratifié",
                "best_for": "Petits budgets, location, home staging avant vente",
                "watch": "Eau sur les joints, sonorité, impossible à poncer",
                "body": """<p>Le stratifié n'est pas du bois : c'est un panneau de fibres recouvert d'une image décorative et d'une couche de protection. Les décors récents imitent bien le bois ou la pierre, et la surface résiste bien aux rayures du quotidien. Il se pose en flottant, rapidement, souvent directement sur l'ancien sol s'il est plan.</p>
<p>Son âme en fibres craint l'eau : les fabricants recommandent un nettoyage à la serpillière à peine humide, sans excès d'eau (voir les conseils de {{lien:Quick-Step humidité|Quick-Step}}). Certaines gammes sont annoncées résistantes à l'eau : fiez-vous à la fiche technique du fabricant pour savoir dans quelles pièces elles sont admises. Une rayure profonde ne se répare pas : on remplace la lame.</p>""",
                "pros": ["Économique et rapide à poser", "Bonne résistance aux rayures de surface", "Grand choix de décors"],
                "cons": ["Ne se ponce pas : une lame abîmée se remplace", "Sensible à l'eau selon la gamme", "Bruit de pas sans sous-couche acoustique adaptée"],
            },
            {
                "id": "vinyle",
                "name": "Vinyle (lames ou rouleau)",
                "best_for": "Cuisine, entrée, salle de bains sans carrelage, petits budgets",
                "watch": "Support parfaitement plan, objets lourds et pieds pointus",
                "body": """<p>Le sol vinyle (PVC) existe en rouleau, en dalles ou en lames clipsables ou à coller (souvent appelées LVT). Il est souple, doux et silencieux sous le pied, et sa surface ne craint pas l'eau : les fabricants comme {{lien:Tarkett pièces humides|Tarkett}} le présentent comme une solution pour la cuisine et la salle de bains, à condition d'une pose soignée aux jonctions et en périphérie.</p>
<p>Il demande un support très plan : les défauts du sol en dessous finissent par se voir. Les pieds de meubles lourds ou pointus peuvent le marquer. Les décors bois et pierre sont réalistes, mais le toucher reste différent d'un matériau naturel.</p>""",
                "pros": ["Surface insensible à l'eau", "Confortable et silencieux", "Pose rapide, faible épaisseur (pratique pour les seuils)"],
                "cons": ["Exige un support très plan", "Peut se marquer sous les charges lourdes", "Aspect moins noble qu'un bois ou une pierre"],
            },
            {
                "id": "carrelage",
                "name": "Carrelage (grès cérame)",
                "best_for": "Salle de bains, douche à l'italienne, cuisine, entrée",
                "watch": "Poids, bruits d'impact, pose et joints exigeants",
                "body": """<p>Le grès cérame est le carrelage le plus courant aujourd'hui : dense, peu poreux, très résistant à l'eau, aux taches et à l'usure. C'est le revêtement de référence pour la salle de bains et la seule option sérieuse sous une douche de plain-pied. Les grands formats et les imitations bois, béton ou pierre permettent d'unifier plusieurs pièces.</p>
<p>Il est froid au toucher (sauf plancher chauffant), lourd, et sa pose demande un support sain, des joints soignés et, dans les pièces d'eau, une étanchéité sous carrelage. En copropriété, remplacer une moquette par du carrelage collé peut augmenter fortement les bruits de chocs chez le voisin du dessous : prévoyez une sous-couche acoustique adaptée.</p>""",
                "pros": ["Insensible à l'eau, très durable", "Entretien simple", "Seul choix fiable sous une douche à l'italienne"],
                "cons": ["Froid et dur sous le pied", "Lourd, pose longue et technique", "Transmet les bruits de chocs sans isolation"],
            },
        ],
        "how_to_choose": """<ol>
<li><strong>Partez de la pièce.</strong> Pièces sèches (séjour, chambres) : parquet, contrecollé ou stratifié. Pièces humides : carrelage ou vinyle. Une même teinte déclinée dans plusieurs matériaux garde l'unité de l'appartement.</li>
<li><strong>Pensez aux voisins du dessous.</strong> Les bruits de pas se transmettent par le plancher ; l'{{lien:ADEME bruit|ADEME}} rappelle l'intérêt d'une sous-couche ou d'une chape désolidarisée pour les limiter. Vérifiez aussi ce qu'impose votre règlement de copropriété avant de changer un sol.</li>
<li><strong>Regardez l'horizon de temps.</strong> Vous restez longtemps : un sol qui se rénove (massif, contrecollé épais, carrelage). Vous vendez bientôt : un sol neutre et propre suffit, c'est souvent la base d'un <a href="/home-staging-paris.html">home staging</a> efficace.</li>
<li><strong>Faites vérifier le support.</strong> Planéité, humidité, ancien revêtement à déposer ou non : c'est souvent ce qui fait varier le chantier et le devis.</li>
<li><strong>Anticipez les seuils.</strong> Les épaisseurs différentes entre pièces créent des ressauts ; les portes peuvent devoir être recoupées.</li>
</ol>
<p>Vous refaites aussi la cuisine ? Notre guide <a href="/guides/plan-de-travail-cuisine-quel-materiau-choisir.html">plan de travail : quel matériau choisir ?</a> vous aidera à assortir sol et plan.</p>""",
        "faq": [
            ("Quel revêtement de sol choisir pour une salle de bains ?",
             "<p>Le carrelage en grès cérame est la référence, et le seul choix fiable sous une douche à l'italienne. Le vinyle est une alternative confortable hors zone de douche. Le parquet et le stratifié classiques sont à éviter dans les pièces d'eau, sauf gammes explicitement prévues par le fabricant.</p>"),
            ("Parquet massif ou contrecollé : quelle différence ?",
             "<p>Le massif est en bois sur toute son épaisseur et peut être poncé plusieurs fois. Le contrecollé n'a qu'une couche de bois noble en surface, sur un support plus stable : il se pose plus facilement, mais le nombre de ponçages dépend de l'épaisseur de cette couche.</p>"),
            ("Peut-on poser un nouveau sol sur l'ancien ?",
             "<p>Souvent oui pour un stratifié, un contrecollé flottant ou certains vinyles, si l'ancien sol est plan, sain et bien adhérent. La surépaisseur peut toutefois imposer de recouper les portes et créer des seuils. Un diagnostic du support avant devis évite les mauvaises surprises.</p>"),
            ("Faut-il une autorisation pour changer le sol en copropriété ?",
             "<p>Changer un revêtement à l'intérieur de son lot ne demande en général pas d'accord de l'assemblée générale, mais le règlement de copropriété peut imposer des exigences acoustiques. Vous restez responsable si le nouveau sol aggrave les nuisances chez le voisin. Voir <a href=\"/journal/travaux-copropriete-faut-il-une-autorisation.html\">notre article sur les travaux en copropriété</a>.</p>"),
            ("Combien coûte la pose d'un revêtement de sol ?",
             "<p>Cela dépend du matériau, de la surface, de l'état du support, de la sous-couche, des plinthes et des seuils. Nous ne donnons pas de fourchette générique : envoyez-nous des photos et les surfaces pour un devis précis.</p>"),
        ],
        "sources": [
            ("ADEME — Isolation phonique : réduire les nuisances sonores", "https://agirpourlatransition.ademe.fr/particuliers/proteger-sante/proteger-bruit/isolation-phonique-reduire-nuisances-sonores"),
            ("ADEME — Guide pratique « Isoler son logement du bruit »", "https://librairie.ademe.fr/ged/1955/guide-pratique-isoler-son-logement-du-bruit.pdf"),
            ("Quick-Step — How do I avoid humidity problems? (stratifié)", "https://www.quick-step.co.uk/en-gb/frequently-asked-questions/laminate/general/how-do-i-avoid-humidity-problems"),
            ("Tarkett — Vinyl floors in the kitchen and bathroom", "https://home.tarkett.co.uk/en_GB/node/vinyl-floors-in-the-kitchen-and-bathroom-14508"),
        ],
        "cta": "Vous changez les sols d'un appartement à Paris, avant d'emménager ou de vendre ? Nous conseillons, préparons le support et posons, sans intermédiaire.",
    },
    {
        "slug": "plan-de-travail-cuisine-quel-materiau-choisir",
        "title": "Plan de travail de cuisine : quel matériau choisir ?",
        "h1": "Plan de travail de cuisine : quel matériau choisir ?",
        "description": "Stratifié, bois massif, quartz, céramique, granit ou inox : le comparatif honnête des matériaux de plan de travail, usage par usage, avant de rénover votre cuisine.",
        "date": "2026-11-26",
        "read": 9,
        "image": "/img/service-renovation.jpg",
        "intro": """<p>Le plan de travail est la surface la plus sollicitée d'une cuisine : chaleur, eau, couteaux, taches. C'est aussi lui qui donne le ton de la pièce. Il n'existe pas de « meilleur » matériau dans l'absolu : il y a celui qui correspond à votre façon de cuisiner, à votre budget et au temps que vous êtes prêt à consacrer à l'entretien.</p>
<p>Voici les six familles que nous posons le plus souvent en rénovation, avec leurs vrais points forts et leurs limites. Nous ne donnons pas de prix au mètre linéaire : ils varient fortement selon l'épaisseur, la finition, les découpes (évier, plaque) et la pose. Le plus fiable reste un devis sur plan.</p>""",
        "verdict": """<ul>
<li><strong>Budget serré, cuisine de location ou de vente :</strong> le stratifié.</li>
<li><strong>Cuisine chaleureuse, prêt à entretenir :</strong> le bois massif.</li>
<li><strong>Grande cuisine familiale, peu d'entretien :</strong> le quartz (pierre reconstituée), avec des {{lien:Amazon dessous-de-plat|dessous-de-plat}}.</li>
<li><strong>Celui qui pose ses casseroles partout :</strong> la céramique / pierre frittée, en surveillant les chocs sur les chants.</li>
<li><strong>Aspect pierre naturelle unique :</strong> le granit.</li>
<li><strong>Usage intensif, esprit professionnel :</strong> l'inox.</li>
</ul>""",
        "options": [
            {
                "id": "stratifie",
                "name": "Stratifié",
                "best_for": "Petits budgets, cuisines de location, home staging avant vente",
                "watch": "Chaleur directe, eau sur les joints et découpes",
                "body": """<p>Le stratifié est un panneau de particules recouvert d'une feuille décorative résistante. Il imite le bois, la pierre ou le béton, et les rendus récents sont souvent convaincants. C'est la solution la plus économique et la plus rapide à poser.</p>
<p>Son point faible est l'âme du panneau : si l'eau s'infiltre par un chant ou une découpe mal protégée, le panneau peut gonfler. La qualité de la pose (joints silicone, chants scellés autour de l'évier) compte autant que le produit.</p>""",
                "pros": ["Le plus économique", "Très grand choix de décors", "Léger et rapide à poser", "Facile à remplacer"],
                "cons": ["Ne supporte pas une casserole brûlante posée directement", "Gonfle si l'eau pénètre par les chants", "Une rayure ou une brûlure ne se répare pas"],
            },
            {
                "id": "bois-massif",
                "name": "Bois massif",
                "best_for": "Cuisines chaleureuses, style naturel ou campagne chic",
                "watch": "Entretien régulier (huile), eau stagnante près de l'évier",
                "body": """<p>Chêne, hêtre, noyer… Le bois massif apporte une chaleur qu'aucune imitation n'égale tout à fait, et il vieillit bien. Ses marques d'usage se poncent : un plan bien entretenu peut être remis à neuf.</p>
<p>En contrepartie, il demande un entretien régulier ({{lien:Amazon huile plan de travail|huile pour plan de travail}} ou vernis selon la finition) et n'aime pas l'eau qui stagne. Près d'un évier, une découpe soignée et une protection des chants sont indispensables.</p>""",
                "pros": ["Matériau naturel et chaleureux", "Se ponce et se rénove", "Agréable au toucher"],
                "cons": ["Entretien régulier à prévoir", "Sensible à l'eau stagnante et aux taches", "Marque avec les chocs et la chaleur"],
            },
            {
                "id": "quartz",
                "name": "Quartz (pierre reconstituée)",
                "best_for": "Cuisines familiales, plans clairs uniformes, peu d'entretien",
                "watch": "Chaleur directe et chocs thermiques : dessous-de-plat obligatoires",
                "body": """<p>Le quartz de synthèse est un agglomérat de quartz naturel et de résine (c'est le principe de marques comme Silestone ou Caesarstone). Sa surface est très peu poreuse : elle résiste bien aux taches et se nettoie à l'eau savonneuse. Les teintes sont régulières, ce qui permet de beaux plans clairs.</p>
<p>Sa limite, rappelée par les fabricants eux-mêmes dans leurs guides d'entretien : la chaleur directe. Il faut poser poêles et plats sortant du four sur un {{lien:Amazon dessous-de-plat|dessous-de-plat}}, car un choc thermique peut marquer ou fissurer la surface. Les chants et les angles sont aussi les zones les plus fragiles aux chocs.</p>""",
                "pros": ["Très peu poreux : résiste bien aux taches", "Entretien simple au quotidien", "Teintes régulières, grand choix de coloris"],
                "cons": ["Ne pas poser de récipient brûlant directement", "Chants sensibles aux chocs", "Poids et pose par un professionnel"],
            },
            {
                "id": "ceramique",
                "name": "Céramique et pierre frittée",
                "best_for": "Cuisiniers intensifs, plans très fins, usage intérieur et extérieur",
                "watch": "Chocs sur les chants et angles, découpes délicates",
                "body": """<p>Les surfaces en céramique (grès cérame grand format) et en pierre frittée (type Dekton) sont fabriquées à très haute température à partir de minéraux. Résultat : une surface quasi non absorbante, très résistante aux rayures, aux taches et à la chaleur. Elles existent en épaisseurs fines, appréciées pour un look contemporain.</p>
<p>Leur faiblesse est l'impact : un objet lourd qui tombe sur un chant ou un angle peut l'écailler. La découpe et la pose demandent un savoir-faire spécifique ; c'est un poste à confier à un poseur habitué à ces matériaux.</p>""",
                "pros": ["Très résistante à la chaleur et aux rayures", "Quasi non absorbante", "Plans fins possibles, aussi en extérieur"],
                "cons": ["Chants et angles fragiles aux chocs", "Découpe et pose techniques", "Rendu parfois froid selon la finition"],
            },
            {
                "id": "granit",
                "name": "Granit et pierre naturelle",
                "best_for": "Aspect unique, cuisines de caractère",
                "watch": "Porosité variable selon la pierre : traitement à prévoir",
                "body": """<p>Chaque plaque de granit est unique. C'est une pierre dure, qui résiste bien à la chaleur et aux rayures. Sa porosité varie selon les variétés : certaines pierres doivent être traitées ({{lien:Amazon hydrofuge oléofuge pierre|hydrofuge / oléofuge}}) pour éviter que l'huile ou le vin ne marquent.</p>
<p>Les autres pierres naturelles (marbre notamment) sont plus sensibles aux acides et aux taches : superbes, mais à réserver à ceux qui acceptent la patine.</p>""",
                "pros": ["Pièce unique, aspect noble", "Bonne résistance à la chaleur et aux rayures", "Très durable"],
                "cons": ["Porosité selon la pierre : traitement à renouveler", "Très lourd", "Teinte non uniforme d'une plaque à l'autre"],
            },
            {
                "id": "inox",
                "name": "Inox",
                "best_for": "Usage intensif, esprit cuisine professionnelle",
                "watch": "Rayures et traces de doigts visibles",
                "body": """<p>L'inox est le matériau des cuisines professionnelles : hygiénique, insensible à la chaleur et à l'eau, il peut intégrer l'évier sans joint. Il se patine en se rayant ; certains aiment cet aspect, d'autres non.</p>""",
                "pros": ["Hygiénique, évier intégrable sans joint", "Insensible à la chaleur et à l'eau", "Très durable"],
                "cons": ["Se raye et garde les traces de doigts", "Rendu froid dans un intérieur classique", "Bruyant sans panneau support"],
            },
        ],
        "how_to_choose": """<ol>
<li><strong>Partez de votre usage.</strong> Vous posez vos casseroles en sortant du feu ? Évitez le stratifié et le quartz sans dessous-de-plat. Vous cuisinez peu ? Le stratifié ou le quartz suffisent largement.</li>
<li><strong>Pensez à l'entretien que vous êtes prêt à faire.</strong> Le bois et certaines pierres demandent un entretien régulier ; le quartz, la céramique et l'inox presque pas.</li>
<li><strong>Si vous vendez bientôt</strong>, un plan sobre et clair, bien posé, suffit à valoriser la cuisine : c'est souvent le meilleur rapport effet / coût en <a href="/home-staging-paris.html">home staging</a>.</li>
<li><strong>Demandez des échantillons</strong> et regardez-les à la lumière de votre cuisine, à côté des façades et de la crédence.</li>
<li><strong>Faites chiffrer sur plan</strong> : découpes, chants, épaisseur, crédence assortie et pose changent beaucoup le total.</li>
</ol>
<p>Votre cuisine est en copropriété et les travaux touchent aux évacuations ? Lisez aussi <a href="/journal/travaux-copropriete-faut-il-une-autorisation.html">travaux en copropriété : faut-il une autorisation ?</a></p>""",
        "faq": [
            ("Quel est le plan de travail le plus résistant ?",
             "<p>Pour la chaleur et les rayures, la céramique et la pierre frittée sont les plus résistantes, devant le granit. Leur point faible reste les chocs sur les chants. Le quartz résiste très bien aux taches mais pas à la chaleur directe.</p>"),
            ("Peut-on poser une casserole chaude sur un plan en quartz ?",
             "<p>Non. Les fabricants recommandent d'utiliser systématiquement un dessous-de-plat, car un choc thermique peut marquer ou fissurer la surface. Voir par exemple les conseils d'entretien de {{lien:Cosentino}}.</p>"),
            ("Quel plan de travail choisir pour vendre son appartement ?",
             "<p>Un plan sobre, clair et en bon état valorise la cuisine sans gros budget : un stratifié de qualité bien posé suffit souvent. L'important est l'impression d'ensemble (propreté, lumière, rangement) sur les photos et en visite.</p>"),
            ("Le bois massif est-il adapté autour de l'évier ?",
             "<p>Oui, à condition de soigner la découpe, de protéger les chants et d'entretenir régulièrement le bois (huile ou vernis selon la finition). L'eau stagnante est son ennemie.</p>"),
            ("Combien coûte un plan de travail posé ?",
             "<p>Cela dépend du matériau, de l'épaisseur, des découpes, des chants et de la pose. Nous préférons ne pas avancer de fourchette générique : envoyez-nous un plan ou des photos pour un devis précis.</p>"),
        ],
        "sources": [
            ("Cosentino — entretien et garanties Silestone / Dekton", "https://www.cosentino.com/fr-fr/"),
            ("Caesarstone — guide d'entretien (quartz, porcelaine)", "https://www.caesarstone.ca/wp-content/uploads/sites/5/2025/06/digital_FR_care_maintenance_manual.pdf"),
        ],
    },
]
