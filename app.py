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
        if not records:
            st.error("Aucun enregistrement trouvé dans les données de l'API.")
            return []
        cleaned_data = []
        for record in records:
            fields = record.get("fields", {})
            point_geo = fields.get("geolocalisation")
            if point_geo and isinstance(point_geo, list) and len(point_geo) == 2:
                lat, lon = point_geo
                fields["latitude"] = lat
                fields["longitude"] = lon
                cleaned_data.append(fields)
        return cleaned_data
    else:
        st.error(f"Échec de la récupération des données de l'API. Statut: {response.status_code}")
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
        # Utilise les coordonnées extraites
        if "latitude" in item and "longitude" in item:
            folium.Marker(
                [item["latitude"], item["longitude"]],
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
