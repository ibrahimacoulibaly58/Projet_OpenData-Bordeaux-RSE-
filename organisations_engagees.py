import streamlit as st
import pandas as pd
import requests

def get_data():
    url = "https://opendata.bordeaux-metropole.fr/api/records/1.0/search/?dataset=met_etablissement_rse&q=&rows=100"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Cela va déclencher une exception pour les réponses non-200
        data = response.json()
        records = data.get("records", [])
        if records:
            return [record.get("fields") for record in records]
        else:
            st.error("Aucun enregistrement trouvé dans les données de l'API.")
            return []
    except requests.RequestException as e:
        st.error(f"Erreur lors de la récupération des données de l'API: {e}")
        return []

def display_organisations_engagees():
    st.markdown("## OPEN DATA RSE")
    st.markdown("### Découvrez les organisations engagées RSE de la métropole de Bordeaux")
    
    data = get_data()
    if data:
        num_etablissements = len(data)
        st.markdown(f"Nombre d'établissements : {num_etablissements}")
        df = pd.DataFrame(data)
        df = df[['nom_courant_denomination', 'commune', 'libelle_section_naf', 'tranche_effectif_entreprise', 'action_rse']].rename(columns={
            'nom_courant_denomination': 'Nom',
            'commune': 'Commune',
            'libelle_section_naf': 'Section NAF',
            'tranche_effectif_entreprise': 'Effectif',
            'action_rse': 'Action RSE'
        })
        st.dataframe(df)
    else:
        st.error("Données OPEN DATA RSE Bordeaux non disponibles actuellement. Veuillez vous reconnecter ultérieurement.")

if __name__ == "__main__":
    display_organisations_engagees()
