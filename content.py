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
<li><strong>Grande cuisine familiale, peu d'entretien :</strong> le quartz (pierre reconstituée), avec des dessous-de-plat.</li>
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
<p>En contrepartie, il demande un entretien régulier (huile ou vernis selon la finition) et n'aime pas l'eau qui stagne. Près d'un évier, une découpe soignée et une protection des chants sont indispensables.</p>""",
                "pros": ["Matériau naturel et chaleureux", "Se ponce et se rénove", "Agréable au toucher"],
                "cons": ["Entretien régulier à prévoir", "Sensible à l'eau stagnante et aux taches", "Marque avec les chocs et la chaleur"],
            },
            {
                "id": "quartz",
                "name": "Quartz (pierre reconstituée)",
                "best_for": "Cuisines familiales, plans clairs uniformes, peu d'entretien",
                "watch": "Chaleur directe et chocs thermiques : dessous-de-plat obligatoires",
                "body": """<p>Le quartz de synthèse est un agglomérat de quartz naturel et de résine (c'est le principe de marques comme Silestone ou Caesarstone). Sa surface est très peu poreuse : elle résiste bien aux taches et se nettoie à l'eau savonneuse. Les teintes sont régulières, ce qui permet de beaux plans clairs.</p>
<p>Sa limite, rappelée par les fabricants eux-mêmes dans leurs guides d'entretien : la chaleur directe. Il faut poser poêles et plats sortant du four sur un dessous-de-plat, car un choc thermique peut marquer ou fissurer la surface. Les chants et les angles sont aussi les zones les plus fragiles aux chocs.</p>""",
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
                "body": """<p>Chaque plaque de granit est unique. C'est une pierre dure, qui résiste bien à la chaleur et aux rayures. Sa porosité varie selon les variétés : certaines pierres doivent être traitées (hydrofuge / oléofuge) pour éviter que l'huile ou le vin ne marquent.</p>
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
<li><strong>Si vous vendez bientôt</strong>, un plan sobre et clair, bien posé, suffit à valoriser la cuisine : c'est souvent le meilleur rapport effet / coût en home staging.</li>
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
