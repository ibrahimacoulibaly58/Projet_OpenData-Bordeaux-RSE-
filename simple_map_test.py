import folium
from streamlit_folium import folium_static
import streamlit as st

def display_simple_map():
    # Coordonnées pour Bordeaux
    lat, lon = 44.837789, -0.57918

    # Création de la carte centrée sur Bordeaux
    m = folium.Map(location=[lat, lon], zoom_start=15)

    # Ajout d'un marqueur pour ces coordonnées
    folium.Marker([lat, lon], popup="Centre de Bordeaux", icon=folium.Icon(color="red", icon="info-sign")).add_to(m)

    # Affichage de la carte dans Streamlit
    folium_static(m)

if __name__ == "__main__":
    display_simple_map()
