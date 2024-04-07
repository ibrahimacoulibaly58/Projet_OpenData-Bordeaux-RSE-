import streamlit as st
import data_manager

def display_actions_rse():
    # Utilisation de data_manager pour récupérer les données
    data, total_hits = data_manager.get_data()
    
    if total_hits > 0:
        # Extraction des noms d'entreprises et des secteurs pour les options de filtre
        noms_entreprises = sorted({record.get("Nom courant/Dénomination") for record in data})
        secteurs = sorted({record.get("Libellé section NAF") for record in data})
        
        # Interface utilisateur pour les filtres
        entreprises_selectionnees = st.multiselect("Filtre par nom d'entreprise :", noms_entreprises)
        secteurs_selectionnes = st.multiselect("Filtre par secteur d'activité :", secteurs)
        
        # Filtrage des actions RSE
        actions_filtrees = [
            record for record in data
            if (record.get("Nom courant/Dénomination") in entreprises_selectionnees or not entreprises_selectionnees)
            and (record.get("Libellé section NAF") in secteurs_selectionnes or not secteurs_selectionnes)
        ]
        
        # Affichage des actions RSE filtrées
        if actions_filtrees:
            for action in actions_filtrees:
                st.write(f"Entreprise: {action.get('nom_entreprise')}, Action: {action.get('description_action_rse')}")
        else:
            st.write("Aucune action RSE correspondante trouvée.")
    else:
        st.write("Erreur lors de la récupération des données.")
