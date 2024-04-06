import streamlit as st
import pandas as pd

def display_organisations_engagees(data):
    st.markdown("## OPEN DATA RSE")
    st.markdown("### Découvrez les organisations engagées RSE de la métropole de Bordeaux")
    num_etablissements = len(data)
    
    if num_etablissements > 0:
        st.markdown(f"Nombre d'établissements : {num_etablissements}")
        df = pd.DataFrame(data)
        st.dataframe(df[['nom_courant_denomination', 'commune', 'libelle_section_naf', 'tranche_effectif_entreprise', 'action_rse']].rename(columns={
            'nom_courant_denomination': 'Nom',
            'commune': 'Commune',
            'libelle_section_naf': 'Section NAF',
            'tranche_effectif_entreprise': 'Effectif',
            'action_rse': 'Action RSE'
        }))
    else:
        st.error("Données OPEN DATA RSE Bordeaux non disponibles actuellement. Veuillez vous reconnecter ultérieurement.")
