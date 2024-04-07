
import streamlit as st
import data_manager

def display_actions_rse():
    # Utilisation de data_manager pour récupérer les données
    data, total_hits = data_manager.get_data()
    
    if total_hits > 0:
        # Correction des clés pour correspondre à celles des données
        noms_entreprises = sorted({record.get("nom_courant_denomination") for record in data if record.get("nom_courant_denomination")})
        secteurs = sorted({record.get("libelle_section_naf") for record in data if record.get("libelle_section_naf")})
        
        # Interface utilisateur pour les filtres
        entreprises_selectionnees = st.multiselect("Filtre par nom d'entreprise :", noms_entreprises)
        secteurs_selectionnes = st.multiselect("Filtre par secteur d'activité :", secteurs)
        
        # Filtrage des actions RSE
        actions_filtrees = [
            record for record in data
            if (record.get("nom_courant_denomination") in entreprises_selectionnees or not entreprises_selectionnees)
            and (record.get("libelle_section_naf") in secteurs_selectionnes or not secteurs_selectionnes)
        ]
        
        # Affichage des actions RSE filtrées
        if actions_filtrees:
            for action in actions_filtrees:
                # Assurez-vous que les clés utilisées ici sont correctes
                st.write(f"Entreprise: {action.get('nom_courant_denomination')}, Action: {action.get('action_rse')}")
        else:
            st.write("Aucune action RSE correspondante trouvée.")
    else:
        st.write("Erreur lors de la récupération des données.")
