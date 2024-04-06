import requests
import folium
from streamlit_folium import folium_static
import streamlit as st

def display_map(data):
    if not data:
        st.write("No data available to display on the map.")
        return
    
    # Initialiser la carte au centre de Bordeaux
    m = folium.Map(location=[44.837789, -0.57918], zoom_start=12)
    
    for item in data:
        lat, lon = item.get("lat"), item.get("lon")
        # Assurez-vous que lat et lon sont des flottants
        if lat and lon:
            folium.Marker(
                [float(lat), float(lon)],
                popup=item.get("name", "Inconnu"),
                icon=folium.Icon(color="green", icon="leaf"),
            ).add_to(m)
    
    folium_static(m)

if __name__ == "__main__":
    data = get_data()
    display_map(data)
