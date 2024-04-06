import folium
from streamlit_folium import folium_static
import streamlit as st

def display_test_map():
    # Coordonnées GPS de l'exemple fourni
    lat, lon = 44.86091098994118, -0.6997150007542606

    # Affichage des coordonnées GPS pour le test
    st.write(f"Test d'affichage du point pour les coordonnées GPS : Latitude = {lat}, Longitude = {lon}")

    # Création de la carte centrée sur les coordonnées avec un zoom approprié
    m = folium.Map(location=[lat, lon], zoom_start=15)

    # Ajout d'un marqueur pour ces coordonnées
    folium.Marker(
        [lat, lon],
        icon=folium.Icon(color="green", icon="leaf"),
        popup="ARIANE GROUP OMNISPORTS RASSEMBLEMENT ASSOCIATIF",
    ).add_to(m)

    # Affichage de la carte dans l'application Streamlit
    folium_static(m)

# Remplacer temporairement le point d'entrée par display_test_map pour le test
if __name__ == "__main__":
    display_test_map()
