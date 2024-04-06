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
        records = data["records"]
        data_for_display = []
        for record in records:
            field = record["fields"]
            # Assume that 'geolocalisation' field is present and correctly formatted
            if "geolocalisation" in field:
                lat, lon = field["geolocalisation"]
                field["latitude"] = lat
                field["longitude"] = lon
                data_for_display.append(field)
        return data_for_display
    else:
        return []

def display_organisations_engagees(data):
    st.markdown("## OPEN DATA RSE")
    st.markdown("### Découvrez les organisations engagées RSE de la métropole de Bordeaux")
    
    df = pd.DataFrame(data)
    df = df[['nom_courant_denomination', 'commune', 'libelle_section_naf', 'tranche_effectif_entreprise', 'action_rse']]
    st.dataframe(df.rename(columns={
        'nom_courant_denomination': 'Nom',
        'commune': 'Commune',
        'libelle_section_naf': 'Section NAF',
        'tranche_effectif_entreprise': 'Effectif',
        'action_rse': 'Action RSE'
    }))

def display_map(data):
    m = folium.Map(location=[44.837789, -0.57918], zoom_start=12)
    for item in data:
        if 'latitude' in item and 'longitude' in item:
            folium.Marker(
                [item['latitude'], item['longitude']],
                icon=folium.Icon(color="green", icon="leaf"),
                popup=item['nom_courant_denomination'],
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
