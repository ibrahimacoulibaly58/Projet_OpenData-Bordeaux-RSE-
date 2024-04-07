
import streamlit as st
import data_manager

def display_actions_rse():
    # Utilisation de data_manager pour récupérer les données
    data, total_hits = data_manager.get_data()
    
    if total_hits > 0:
        # Correction des clés pour correspondre à celles des données
        noms_entreprises = sorted({record.get("nom_courant_denomination") for record in data if record.get("nom_courant_denomination")})
        secteurs = sorted({record.get("libelle_section_naf") for record in data if record.get("libelle_section_naf")})
        
        # Interface utilisateur pour les filtres - Transformation en choix unique
        entreprise_selectionnee = st.selectbox("Filtre par nom d'entreprise :", ["Tous"] + noms_entreprises)
        secteur_selectionne = st.selectbox("Filtre par secteur d'activité :", ["Tous"] + secteurs)
        
        # Filtrage des actions RSE
        actions_filtrees = [
            record for record in data
            if (record.get("nom_courant_denomination") == entreprise_selectionnee or entreprise_selectionnee == "Tous")
            and (record.get("libelle_section_naf") == secteur_selectionne or secteur_selectionne == "Tous")
        ]
        
        # Affichage des actions RSE filtrées
        if actions_filtrees:
            for action in actions_filtrees:
                st.write(f"Entreprise: {action.get('nom_courant_denomination')}, Action: {action.get('action_rse')}")
        else:
            st.write("Aucune action RSE correspondante trouvée.")
    else:
        st.write("Erreur lors de la récupération des données.")
