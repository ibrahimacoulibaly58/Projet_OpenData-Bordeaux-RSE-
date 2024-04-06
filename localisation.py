import requests
import folium
from streamlit_folium import folium_static
import streamlit as st

def get_data():
    url = "https://opendata.bordeaux-metropole.fr/api/records/1.0/search/?dataset=met_etablissement_rse&q=&rows=100"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            records = data.get("records", [])
            cleaned_data = []
            for record in records:
                fields = record.get("fields", {})
                point_geo = fields.get("geolocalisation")
                if point_geo and isinstance(point_geo, list) and len(point_geo) == 2:
                    lat, lon = point_geo  # Directement extraire la latitude et la longitude
                    fields["latitude"], fields["longitude"] = lat, lon
                    cleaned_data.append(fields)
            return cleaned_data
        else:
            st.error("Aucun enregistrement trouvé dans les données de l'API.")
            return []
    except requests.RequestException as e:
        st.error(f"Erreur lors de la récupération des données de l'API: {e}")
        return []

def display_map(data):
    m = folium.Map(location=[44.837789, -0.57918], zoom_start=12)
    for item in data:
        lat = item.get('latitude')
        lon = item.get('longitude')
        if lat and lon:
            lat, lon = float(lat), float(lon)  # Assurez-vous que les coordonnées sont des nombres flottants
            folium.Marker(
                [lat, lon],
                icon=folium.Icon(color="green", icon="leaf"),
                popup=item.get('nom_courant_denomination', "Information non disponible"),
            ).add_to(m)
    folium_static(m)
