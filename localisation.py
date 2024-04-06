import requests
import folium
from streamlit_folium import folium_static
import streamlit as st

def get_data():
    url = "https://opendata.bordeaux-metropole.fr/api/records/1.0/search/?dataset=met_etablissement_rse&q=&rows=100"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        records = data.get("records", [])
        cleaned_data = []
        for record in records:
            fields = record.get("fields", {})
            # Assumer que 'geolocalisation' contient directement les coordonnées [lat, lon]
            if 'geolocalisation' in fields:
                lat, lon = fields['geolocalisation']
                cleaned_data.append({"lat": lat, "lon": lon, "name": fields.get("nom_courant_denomination", "Inconnu")})
        return cleaned_data
    else:
        st.error("Failed to fetch data")
        return []

def display_map(data):
    m = folium.Map(location=[44.837789, -0.57918], zoom_start=12)
    for item in data:
        lat, lon = item["lat"], item["lon"]
        folium.Marker(
            [lat, lon],
            popup=item["name"],
            icon=folium.Icon(color="green", icon="leaf"),
        ).add_to(m)
    folium_static(m)

# Cette partie est pour exécuter le test directement dans ce fichier, si désiré
if __name__ == "__main__":
    data = get_data()
    display_map(data)
