import requests
import folium
from streamlit_folium import folium_static
import streamlit as st

def get_data():
    # URL de l'API
    url = "https://opendata.bordeaux-metropole.fr/api/records/1.0/search/?dataset=met_etablissement_rse&q=&rows=100"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            records = data.get("records", [])
            cleaned_data = []
            for record in records:
                fields = record.get("fields", {})
                # Assurez-vous que la structure de 'fields' correspond à ce que vous attendez
                if 'geolocalisation' in fields:
                    cleaned_data.append(fields)
            return cleaned_data
        else:
            st.error("Échec de la récupération des données. Statut HTTP : {}".format(response.status_code))
            return []
    except requests.exceptions.RequestException as e:
        st.error("Erreur lors de la connexion à l'API : {}".format(e))
        return []

def display_map(data):
    # Initialise la carte
    m = folium.Map(location=[44.837789, -0.57918], zoom_start=12)
    # Ajoute un marqueur pour chaque élément dans 'data'
    for item in data:
        point_geo = item.get('geolocalisation')
        if point_geo:
            lat, lon = point_geo[0], point_geo[1]
            folium.Marker([lat, lon],
                          icon=folium.Icon(color="green", icon="leaf"),
                          popup=item.get('nom_courant_denomination', 'Inconnu')
                          ).add_to(m)
    folium_static(m)
