import requests
import folium
from streamlit_folium import folium_static
import streamlit as st

def display_map():
    data, _ = get_data()
    if data:
        m = folium.Map(location=[44.84474, -0.60711], zoom_start=12)
        for item in data:
            try:
                # Supposons que 'point_geo' est une liste [lat, lon]
                point_geo = item.get('point_geo', [])
                if point_geo:
                    # Extraction de lat et lon par indexation de la liste, en supposant l'ordre correct [lat, lon]
                    lat, lon = point_geo
                    lat, lon = float(lat), float(lon)
                    # Vérification que lat et lon sont valides
                    if lat and lon:
                        folium.Marker([lat, lon], popup=item.get("nom_courant_denomination", "Sans nom")).add_to(m)
            except (ValueError, TypeError, IndexError):
                # Gestion des erreurs pour la conversion en float, format de données inattendu, ou index manquant
                continue
        folium_static(m)

if __name__ == "__main__":
    data = get_data()
    display_map(data)
