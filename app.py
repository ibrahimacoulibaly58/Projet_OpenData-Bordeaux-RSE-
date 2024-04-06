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
        return [record.get("fields") for record in records]
    else:
        return []

def display_organisations_engagees(data):
    st.markdown("## OPEN DATA RSE")
    st.markdown("### Découvrez les organisations engagées RSE de la métropole de Bordeaux")
    
    df = pd.DataFrame(data)
    if not df.empty:
        df = df[["nom_courant_denomination", "commune", "libelle_section_naf", "tranche_effectif_entreprise", "action_rse"]]
        st.dataframe(df.rename(columns={
            "nom_courant_denomination": "Nom",
            "commune": "Commune",
            "libelle_section_naf": "Section NAF",
            "tranche_effectif_entreprise": "Effectif",
            "action_rse": "Action RSE"
        }))

def display_map(data):
    bordeaux_loc = [44.837789, -0.57918]
    m = folium.Map(location=bordeaux_loc, zoom_start=12)
    for item in data:
        if item.get("geolocalisation"):
            folium.Marker(
                location=[item["geolocalisation"][0], item["geolocalisation"][1]],
                popup=item.get("nom_courant_denomination", "Information non disponible"),
                icon=folium.Icon(color="green", icon="leaf"),
            ).add_to(m)
    folium_static(m)

def main():
    st.sidebar.title("Navigation")
    app_mode = st.sidebar.radio("Choisissez l'onglet", ["Organisations engagées", "Localisation des Entreprises"])

    data = get_data()

    if app_mode == "Organisations engagées":
        display_organisations_engagees(data)
    elif app_mode == "Localisation des Entreprises":
        display_map(data)

if __name__ == "__main__":
    main()
