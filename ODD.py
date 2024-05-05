from data_manager import get_data

def classify_actions_rse_ODD(data):
    data, _ = get_data()  # Récupérer les données depuis data_manager.py

    criteria = {
        "ODD 1 - Pas de pauvreté": [],
        "ODD 2 - Faim zéro": [],
        "ODD 3 - Bonne santé et bien-être": [],
        "ODD 4 - Éducation de qualité": [],
        "ODD 5 - Égalité entre les sexes": [],
        "ODD 6 - Eau propre et assainissement": [],
        "ODD 7 - Énergie propre et abordable": [],
        "ODD 8 - Travail décent et croissance économique": [],
        "ODD 9 - Industrie, innovation et infrastructure": [],
        "ODD 10 - Inégalités réduites": [],
        "ODD 11 - Villes et communautés durables": [],
        "ODD 12 - Consommation et production responsables": [],
        "ODD 13 - Lutte contre le changement climatique": [],
        "ODD 14 - Vie aquatique": [],
        "ODD 15 - Vie terrestre": [],
        "ODD 16 - Paix, justice et institutions solides": [],
        "ODD 17 - Partenariats pour les objectifs": [],
        "Autres": []
    }

    keywords = {
        "ODD 1 - Pas de pauvreté": ["pauvreté", "réduction de la pauvreté", "exclusion sociale"],
        "ODD 2 - Faim zéro": ["faim", "malnutrition", "sécurité alimentaire"],
        "ODD 3 - Bonne santé et bien-être": ["santé", "bien-être", "accès aux soins"],
        "ODD 4 - Éducation de qualité": ["éducation", "formation", "alphabétisation"],
        "ODD 5 - Égalité entre les sexes": ["égalité des genres", "femmes", "droits des femmes"],
        "ODD 6 - Eau propre et assainissement": ["eau potable", "assainissement", "hygiène"],
        "ODD 7 - Énergie propre et abordable": ["énergie", "renouvelable", "accès à l'énergie"],
        "ODD 8 - Travail décent et croissance économique": ["travail décent", "emploi", "croissance économique"],
        "ODD 9 - Industrie, innovation et infrastructure": ["industrie", "innovation", "infrastructures"],
        "ODD 10 - Inégalités réduites": ["inégalités", "justice sociale", "équité"],
        "ODD 11 - Villes et communautés durables": ["villes durables", "urbanisation", "habitat"],
        "ODD 12 - Consommation et production responsables": ["consommation responsable", "production durable", "déchets"],
        "ODD 13 - Lutte contre le changement climatique": ["changement climatique", "réchauffement climatique", "émissions de CO2"],
        "ODD 14 - Vie aquatique": ["océans", "biodiversité marine", "pêche durable"],
        "ODD 15 - Vie terrestre": ["biodiversité terrestre", "forêts", "écosystèmes"],
        "ODD 16 - Paix, justice et institutions solides": ["paix", "justice", "systèmes judiciaires"],
        "ODD 17 - Partenariats pour les objectifs": ["partenariats", "coopération", "engagement"],
    }

    for record in data:
        action_rse = record.get("action_rse", "").lower()
        company_info = {
            "name": record.get("nom_courant_denomination", "N/A"),
            "action_rse": action_rse,
            "activity": record.get("libelle_section_naf", "N/A"),
            "city": record.get("commune", "N/A")
        }
        found_category = False
        for criterion, key_phrases in keywords.items():
            if any(key_phrase in action_rse for key_phrase in key_phrases):
                criteria[criterion].append(company_info)
                found_category = True
                break  # Assuming each action belongs to one category only
        
        # Si l'action n'a pas été classifiée dans une catégorie existante, la placer dans "Autres"
        if not found_category:
            criteria["Autres"].append(company_info)

    return criteria
