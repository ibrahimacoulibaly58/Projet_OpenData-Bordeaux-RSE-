from folium import Map, Marker, Icon, Popup
from streamlit_folium import folium_static
import streamlit as st
from data_manager import get_data

def display_map():
    data, total_hits = get_data()  # Assurez-vous que get_data() retourne également total_hits
    if data:
        # Message au-dessus de la carte
        st.markdown("Cliquer sur l'icône pour découvrir l'entreprise et une de ses actions RSE remarquable")
        
        m = Map(location=[44.84474, -0.60711], zoom_start=12)
        for item in data:
            try:
                point_geo = item.get('point_geo', [])
                if point_geo:
                    lat, lon = float(point_geo[0]), float(point_geo[1])
                    if lat and lon:
                        popup_html = f"""
                        <div style="width:300px;">
                            <b>{item.get('nom_courant_denomination', 'Sans nom')}</b><br>
                            <b>Action RSE:</b><br>
                            {item.get('action_rse', 'Non spécifiée')}
                        </div>
                        """
                        popup = Popup(popup_html, max_width=500)
                        Marker([lat, lon], popup=popup, icon=Icon(color='green', icon='leaf', prefix='fa')).add_to(m)
            except (ValueError, TypeError, IndexError):
                continue
        
        folium_static(m)
        
        # Message et nombre d'organisations en dessous de la carte
        st.markdown(f"* Nombre d'organisations : {total_hits}")

if __name__ == "__main__":
    display_map()
