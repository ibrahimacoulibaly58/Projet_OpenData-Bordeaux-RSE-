import folium
from streamlit_folium import folium_static
import streamlit as st

def display_map():
    # Coordonnées de l'exemple "ARIANE GROUP OMNISPORTS RASSEMBLEMENT ASSOCIATIF"
    lat, lon = 44.86091098994118, -0.6997150007542606

    # Création de la carte centrée sur les coordonnées avec un niveau de zoom approprié
    m = folium.Map(location=[lat, lon], zoom_start=15)

    # Ajout d'un marqueur pour l'entreprise "ARIANE GROUP OMNISPORTS RASSEMBLEMENT ASSOCIATIF" avec ces coordonnées
    folium.Marker(
        [lat, lon],
        icon=folium.Icon(color="green", icon="leaf"),
        popup="ARIANE GROUP OMNISPORTS RASSEMBLEMENT ASSOCIATIF",
    ).add_to(m)

    # Affichage de la carte dans l'application Streamlit
    folium_static(m)
