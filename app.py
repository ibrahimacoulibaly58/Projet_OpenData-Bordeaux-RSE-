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
    num_etablissements = len(data)
    st.markdown(f"Nombre d'établissements : {num_etablissements}")
    if data:
        df = pd.DataFrame(data)
        st.dataframe(df[['nom_courant_denomination', 'commune', 'libelle_section_naf', 'tranche_effectif_entreprise', 'action_rse']].rename(columns={
            'nom_courant_denomination': 'Nom',
            'commune': 'Commune',
            'libelle_section_naf': 'Section NAF',
            'tranche_effectif_entreprise': 'Effectif',
            'action_rse': 'Action RSE'
        }))

def display_map(data):
    m = folium.Map(location=[44.837789, -0.57918], zoom_start=12)
    for item in data:
        point_geo = item.get('point_geo')
        if isinstance(point_geo, dict):
            lon = point_geo.get('lon')
            lat = point_geo.get('lat')
            if lon and lat:
                folium.Marker(
                    [lat, lon],
                    icon=folium.Icon(color="green", icon="leaf"),
                    popup=item.get('nom_courant_denomination', 'Information non disponible'),
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
