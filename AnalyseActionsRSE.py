import streamlit as st
from ISO26000 import classify_actions_rse_ISO26000 as classify_iso26000
from ODD import classify_actions_rse_ODD as classify_ODD
from impactscore import classify_actions_rse_IMPACTSCORE as classify_impactscore
from data_manager import get_data

criteria = {}
if "Autres" not in criteria:
    criteria["Autres"] = []

company_info = "Some company info"

criteria["Autres"].append(company_info)

def display_analyse_actions_rse():
    st.markdown("## IA RSE :mag_right:")
    st.markdown("### Classification des actions RSE selon 3 approches :")

    approach = st.radio(
        "Choisissez l'approche de classification :point_down:",
        
        ["Norme ISO 26000", "ODD Objectifs de Développement Durable (en cours de développement)","Impact Score (en cours de développement)"],
        index=0,
        format_func=lambda x: x.split(" :")[0]
    )

    if approach == "Norme ISO 26000":
        # Récupérer les données depuis data_manager.py
        data, total_hits = get_data()

        st.markdown("""<hr style='border-color: darkgrey;'>""", unsafe_allow_html=True)

        st.markdown("""
                    :earth_africa: **QU'EST-CE QUE LA NORME ISO 26000 ?**
                    
                    La norme ISO 26000 propose une grille de lecture de la thématique développement durable ultra-pratique pour déployer une politique RSE d'entreprise bien structurée, qui ne laisse rien de côté. Publiée en 2010, cette norme volontaire a été élaborée en concertation avec près de 90 pays à travers le monde, dont la France.
                    
                    **COMMENT EST-ELLE STRUCTURÉE ?**
                    
                    ISO 26000 : Une grille de lecture à 7 entrées
                    
                    - 🏢 La gouvernance de la structure
                    - 👨‍👩‍👧‍👦 Les droits humains
                    - 🤝 Les conditions et relations de travail
                    - 🌱 La responsabilité environnementale
                    - ⚖️ La loyauté des pratiques
                    - 🛍️ Les questions relatives au consommateur et à la protection du consommateur
                    - 🌍 Les communautés et le développement local.
                """)
        st.markdown("""<small>Source AFNOR : <a href="https://www.afnor.org/developpement-durable/demarche-iso-26000/" target="_blank">www.afnor.org/developpement-durable/demarche-iso-26000/</a></small>""", unsafe_allow_html=True)

        st.markdown("""<hr style='border-color: darkgrey;'>""", unsafe_allow_html=True)
        st.markdown("### Classification des actions RSE selon ISO 26000")

        pictograms = {
            "Gouvernance de la structure": "🏢",
            "Droits humains": "👨‍👩‍👧‍👦",
            "Conditions et relations de travail": "🤝",
            "Responsabilité environnementale": "🌱",
            "Loyauté des pratiques": "⚖️",
            "Questions relatives au consommateur": "🛍️",
            "Communautés et développement local": "🌍",
            "Autres": "❓"
        }

        
        criteria_counts = classify_iso26000(data)

        total_actions = 0

        for category, actions in criteria_counts.items():
            if category in pictograms:
                st.subheader(f"{pictograms[category]} {category}")
            else:
                st.subheader(f"{pictograms['Autres']} Autres")
            total_actions += len(actions)
            for action in actions:
                nom_entreprise = action.get('nom_courant_denomination', 'Information non disponible')
                st.write(f"Entreprise : {action.get('name','N/A')}, Action RSE : {action.get('action_rse', 'N/A')}, Activité : {action.get('activity', 'N/A')}, Ville : {action.get('city', 'N/A')}")

        st.markdown("""<hr style='border-color: darkgrey;'>""", unsafe_allow_html=True)
        st.markdown(f"**Total des actions RSE :** {total_actions}")

    elif approach == "Impact Score (en cours de développement)":
        # Récupérer les données depuis data_manager.py
        data, total_hits = get_data()

        st.markdown("""<hr style='border-color: darkgrey;'>""", unsafe_allow_html=True)

        st.markdown("""
                    🌳 **QU'EST-CE QUE L'IMPACT SCORE ?**
                    
                    Ce référentiel commun et unique a été co-construit par 30 réseaux d’entreprises afin de publier en transparence leurs données d’impact, exigence européenne depuis 2024.
                    
                    **COMMENT EST-IL STRUCTURÉE ?**
                    
                    IMPACT SCORE repose sur 3 piliers essentiels : 
                    
                    - 🚫 LIMITATION DES EXTERNALITÉS NÉGATIVES
                    - 💡 PARTAGE DU POUVOIR ET DE LA VALEUR
                    - 🎯 STRATÉGIE À IMPACT
                                    """)
        
     
        st.markdown("""<small>Source MOUVEMENT IMPACT FRANCE : <a href="https://impactscore.fr/comprendre-limpact-score/" target="_blank">https://impactscore.fr/comprendre-limpact-score/</a></small>""", unsafe_allow_html=True)

        st.markdown("""<hr style='border-color: darkgrey;'>""", unsafe_allow_html=True)
        pictograms  = {
            "Initiatives pour réduire l'empreinte carbone": "🚫",
            "Amélioration des conditions de travail": "💡",
            "Promotion du recyclage": "🎯",
            "Autres": "❓"
                                    }
        criteria_counts = classify_impactscore(data)

        total_actions = 0
        for category, actions in criteria_counts.items():
            if category in pictograms:
                st.subheader(f"{pictograms[category]} {category}")
            else:
                st.subheader(f"{pictograms['Autres']} Autres")
            total_actions += len(actions)
            for action in actions:
                nom_entreprise = action.get('nom_courant_denomination', 'Information non disponible')
                st.write(f"Entreprise : {action.get('name','N/A')}, Action RSE : {action.get('action_rse', 'N/A')}, Activité : {action.get('activity', 'N/A')}, Ville : {action.get('city', 'N/A')}")

        st.markdown("""<hr style='border-color: darkgrey;'>""", unsafe_allow_html=True)
        st.markdown(f"**Total des actions RSE :** {total_actions}")

   ### OBJECTIF DE DEVELOPPEMENT DURABLE ###
    elif approach == "ODD Objectifs de Développement Durable (en cours de développement)":
        # Récupérer les données depuis data_manager.py
        data, total_hits = get_data()

        st.markdown("""<hr style='border-color: darkgrey;'>""", unsafe_allow_html=True)

        st.markdown("""
                    🌳 **QU'EST-CE QUE LES 17 ODD ?**
                    
                    Au cœur de l’Agenda 2030, 17 Objectifs de développement durable (ODD) ont été fixés. Ils couvrent l’intégralité des enjeux de développement dans tous les pays tels que le climat, la biodiversité, l’énergie, l’eau, la pauvreté, l’égalité des genres, la prospérité économique ou encore la paix, l’agriculture, l’éducation, etc.
                    
                    **COMMENT SONT-ILS STRUCTURÉS ?**
                                                
                    - ODD n°1 - Pas de pauvreté
                    - ODD n°2 - Faim « Zéro »
                    - ODD n°3 - Bonne santé et bien-être
                    - ODD n°4 - Éducation de qualité
                    - ODD n°5 - Égalité entre les sexes
                    - ODD n°6 - Eau propre et assainissement
                    - ODD n°7 - Énergie propre et d'un coût abordable
                    - ODD n°8 - Travail décent et croissance économique
                    - ODD n°9 - Industrie, innovation et infrastructure
                    - ODD n°10 - Inégalités réduites
                    - ODD n°11 - Villes et communautés durable
                    - ODD n°12 - Consommation et production responsables
                    - ODD n°13 - Lutte contre les changements climatiques
                    - ODD n°14 - Vie aquatique
                    - ODD n°15 - Vie terrestre
                    - ODD n°16 - Paix, justice et institutions efficaces
                    - ODD n°17 - Partenariats pour la réalisation des objectifs
                    
                    """)
        pictograms = {
            "ODD 1 - Fin de la pauvreté": "1",
            "ODD 2 - Faim zéro": "2",
            "ODD 3 - Bonne santé et bien-être": "3",
            "ODD 4 - Éducation de qualité": "4",
            "ODD 5 - Égalité entre les sexes": "5",
            "ODD 6 - Eau propre et assainissement": "6",
            "ODD 7 - Énergie propre et abordable": "7",
            "ODD 8 - Travail décent et croissance économique": "8",
            "ODD 9 - Industrie, innovation et infrastructure": "9",
            "ODD 10 - Inégalités réduites": "10",
            "ODD 11 - Villes et communautés durables": "️11",
            "ODD 12 - Consommation et production responsables": "12",
            "ODD 13 - Lutte contre le changement climatique": "13",
            "ODD 14 - Vie aquatique": "14",
            "ODD 15 - Vie terrestre": "15",
            "ODD 16 - Paix, justice et institutions solides": "️16",
            "ODD 17 - Partenariats pour les objectifs": "17",
            "Autres": "❓"
        }
     
        st.markdown("""<small>Source AGENDA 2030 EN FRANCE : <a href="https://www.agenda-2030.fr/17-objectifs-de-developpement-durable/?" target="_blank">https://impactscore.fr/comprendre-limpact-score/</a></small>""", unsafe_allow_html=True)

        st.markdown("""<hr style='border-color: darkgrey;'>""", unsafe_allow_html=True)
        criteria_counts = classify_ODD(data)

        total_actions = 0

        for category, actions in criteria_counts.items():
            if category in pictograms:
                st.subheader(f"{pictograms[category]} {category}")
            else:
                st.subheader(f"{pictograms['Autres']} Autres")
            total_actions += len(actions)
            for action in actions:
                nom_entreprise = action.get('nom_courant_denomination', 'Information non disponible')
                st.write(f"Entreprise : {action.get('name','N/A')}, Action RSE : {action.get('action_rse', 'N/A')}, Activité : {action.get('activity', 'N/A')}, Ville : {action.get('city', 'N/A')}")

        st.markdown("""<hr style='border-color: darkgrey;'>""", unsafe_allow_html=True)
        st.markdown(f"**Total des actions RSE :** {total_actions}")
        criteria_counts = classify_impactscore(data)
    

    if approach == "Norme ISO 26000":
        st.subheader("Synthèse par catégorie ISO 26000")
        synthesis = {category: len(actions) for category, actions in criteria_counts.items()}
        synthesis_sorted = dict(sorted(synthesis.items(), key=lambda item: item[1], reverse=True))
        for category, count in synthesis_sorted.items():
            st.write(f"{category}: {count} action(s) RSE")

if __name__ == "__main__":
    display_analyse_actions_rse()