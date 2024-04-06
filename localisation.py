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
            # Assurez-vous que la structure des données correspond à ce qui est attendu.
            geoloc = fields.get("geolocalisation")
            if geoloc and isinstance(geoloc, list) and len(geoloc) == 2:
                lat, lon = geoloc
                cleaned_data.append({"lat": lat, "lon": lon, "name": fields.get("nom_courant_denomination", "Inconnu")})
        return cleaned_data
    else:
        st.error(f"Failed to fetch data. Status code: {response.status_code}")
        return []

def display_map(data):
    if not data:
        st.write("No data available to display on the map.")
        return

    m = folium.Map(location=[44.837789, -0.57918], zoom_start=12)

    for item in data:
        lat, lon = item["lat"], item["lon"]
        folium.Marker(
            [lat, lon],
            popup=item["name"],
            icon=folium.Icon(color="green", icon="leaf"),
        ).add_to(m)

    folium_static(m)

if __name__ == "__main__":
    data = get_data()
    display_map(data)
