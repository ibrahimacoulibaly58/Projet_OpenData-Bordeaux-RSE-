
import streamlit as st
import pandas as pd
import requests
import folium
from streamlit_folium import folium_static

def get_data():
    url = "https://opendata.bordeaux-metropole.fr/api/records/1.0/search/?dataset=met_etablissement_rse&q=&rows=100"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        records = data.get("records", [])
        return [record["fields"] for record in records], data.get("nhits", 0)
    else:
        return [], 0

def display_organisations_engagees():
    st.markdown("## OPEN DATA RSE")
    st.markdown("### Découvrez les organisations engagées RSE de la métropole de Bordeaux")
    
    data, _ = get_data()
    if data:
        df = pd.DataFrame(data)
        df = df.rename(columns={
            "nom_courant_denomination": "Nom",
            "commune": "Commune",
            "libelle_section_naf": "Section NAF",
            "tranche_effectif_entreprise": "Effectif",
            "action_rse": "Action RSE"
        })
        df = df[["Nom", "Commune", "Section NAF", "Effectif", "Action RSE"]]
        st.dataframe(df, width=None, height=None)

def main():
    st.sidebar.title("Navigation")
    app_mode = st.sidebar.radio("Choose a page", ["Home", "Organisations Engagées"])
    
    if app_mode == "Home":
        st.header("Welcome to the RSE Data Explorer!")
        st.markdown("Please select a page on the left.")
    elif app_mode == "Organisations Engagées":
        display_organisations_engagees()

if __name__ == "__main__":
    main()
