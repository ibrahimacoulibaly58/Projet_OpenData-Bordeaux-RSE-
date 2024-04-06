import requests
from folium import Map, Marker, Icon
from streamlit_folium import folium_static
import streamlit as st
from data_manager import get_data

def display_map():
    data, _ = get_data()
    if data:
        m = Map(location=[44.84474, -0.60711], zoom_start=12)
        for item in data:
            try:
                point_geo = item.get('point_geo', [])
                if point_geo:
                    lat, lon = point_geo
                    lat, lon = float(lat), float(lon)
                    if lat and lon:
                        popup_content = f"<b>{item.get('nom_courant_denomination', 'Sans nom')}</b><br>" \
                                        f"<b>Action RSE</b><br>" \
                                        f"{item.get('action_rse', 'Non spécifiée')}"
                        Marker([lat, lon], 
                               popup=popup_content, 
                               icon=Icon(color='green', icon='leaf', prefix='fa')).add_to(m)
            except (ValueError, TypeError, IndexError):
                continue
        folium_static(m)

if __name__ == "__main__":
    display_map()
