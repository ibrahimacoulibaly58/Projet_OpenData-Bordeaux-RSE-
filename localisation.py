import requests
import folium
from streamlit_folium import folium_static

def get_data():
    url = "https://opendata.bordeaux-metropole.fr/api/records/1.0/search/?dataset=met_etablissement_rse&q=&rows=100"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        records = data.get("records", [])
        cleaned_data = []
        for record in records:
            fields = record.get("fields", {})
            # Assurez-vous que point_geo est un dictionnaire avec lat et lon.
            point_geo = fields.get("geolocalisation")
            if point_geo and isinstance(point_geo, list) and len(point_geo) == 2:
                # Stockez directement lat et lon dans fields pour un accès facile.
                fields["latitude"], fields["longitude"] = point_geo[0], point_geo[1]
                cleaned_data.append(fields)
        return cleaned_data
    else:
        return []

def display_map(data):
    m = folium.Map(location=[44.837789, -0.57918], zoom_start=12)
    for item in data:
        # Utilisez directement latitude et longitude.
        lat, lon = item.get("latitude"), item.get("longitude")
        if lat and lon:
            folium.Marker(
                [lat, lon],
                icon=folium.Icon(color="green", icon="leaf"),
                popup=item.get('nom_courant_denomination', 'Information non disponible'),
            ).add_to(m)
    folium_static(m)
