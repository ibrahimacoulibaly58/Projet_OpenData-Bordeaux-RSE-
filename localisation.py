import requests
from folium import Map, Marker, Icon, Popup
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
                    lat, lon = float(point_geo[0]), float(point_geo[1])
                    if lat and lon:
                        # Définition du contenu HTML avec style CSS pour élargir le popup
                        popup_html = f"""
                        <div style="width:300px;">
                            <b>{item.get('nom_courant_denomination', 'Sans nom')}</b><br>
                            <b>Action RSE:</b><br>
                            {item.get('action_rse', 'Non spécifiée')}
                        </div>
                        """
                        popup = Popup(popup_html, max_width=500)  # Vous pouvez ajuster max_width comme souhaité
                        Marker([lat, lon], popup=popup, icon=Icon(color='green', icon='leaf', prefix='fa')).add_to(m)
            except (ValueError, TypeError, IndexError):
                continue
        folium_static(m)

if __name__ == "__main__":
    display_map()
