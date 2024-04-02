import streamlit as st
import pandas as pd
import requests

def get_data(page, rows_per_page=25):
    """
    Récupère les données paginées de l'API.
    
    Args:
        page (int): Numéro de la page à récupérer.
        rows_per_page (int): Nombre de lignes par page.
        
    Returns:
        List[Dict]: Données de la page spécifiée sous forme de liste de dictionnaires.
    """
    # Construction de l'URL avec pagination
    url = f"https://opendata.bordeaux-metropole.fr/api/records/1.0/search/?dataset=met_etablissement_rse&q=&rows={rows_per_page}&start={page * rows_per_page}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        records = data.get("records", [])
        return [record["fields"] for record in records], data.get("nhits", 0)
    else:
        return [], 0

def display_organisations_engagees():
    """
    Affiche les organisations engagées avec pagination et colonnes réordonnées.
    """
    # Pagination
    page_number = st.sidebar.number_input("Page number", min_value=0, value=0, step=1)
    data, total_hits = get_data(page_number)
    
    if data:
        df = pd.DataFrame(data)
        # Réordonner les colonnes selon la spécification
        cols_order = ["nom_courant_denomination", "tranche_effectif_entreprise", "commune", "hierarchie_naf", "action_rse"]
        # Filtre les colonnes pour s'assurer qu'elles existent dans les données
        cols_order = [col for col in cols_order if col in df.columns]
        df = df[cols_order]
        
        # Affichage des données avec les colonnes réordonnées
        st.write(f"Organisations engagées - Page {page_number + 1} sur {((total_hits - 1) // 25) + 1}", df)
    else:
        st.write("Aucune donnée disponible.")

if __name__ == "__main__":
    st.sidebar.title("Navigation")
    app_mode = st.sidebar.selectbox("Choisissez l'onglet", ["Organisations engagées", "Autre Onglet"])

    if app_mode == "Organisations engagées":
        display_organisations_engagees()