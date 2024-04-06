
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

def display_map(data):
    m = folium.Map(location=[44.837789, -0.57918], zoom_start=12)
    for item in data:
        if 'latitude' in item and 'longitude' in item:
            folium.Marker(
                location=[item['latitude'], item['longitude']],
                popup=item.get('Nom', 'Sans nom'),
                icon=folium.Icon(color="green", icon="leaf")
            ).add_to(m)
    folium_static(m)

def main():
    st.sidebar.title("Navigation")
    app_mode = st.sidebar.radio("Choisissez l'onglet", ["Organisations engagées", "Localisation des Entreprises"])

    if app_mode == "Organisations engagées":
        display_organisations_engagees()
    elif app_mode == "Localisation des Entreprises":
        data, _ = get_data()
        display_map(data)

if __name__ == "__main__":
    main()
