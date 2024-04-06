
import streamlit as st
import pandas as pd
import requests
import folium
from streamlit_folium import folium_static

def get_data():
    url = "https://opendata.bordeaux-metropole.fr/api/records/1.0/search/?dataset=met_etablissement_rse&q=&rows=100"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        records = data["records"]
        data_for_map = []
        for record in records:
            fields = record.get("fields", {})
            geo = fields.get("geolocalisation")
            if geo and len(geo) == 2:
                lat, lon = geo
                fields["latitude"] = lat
                fields["longitude"] = lon
                data_for_map.append(fields)
        return data_for_map
    return []

def display_organisations_engagees(data):
    st.markdown("## OPEN DATA RSE")
    st.markdown("### Découvrez les organisations engagées RSE de la métropole de Bordeaux")
    df = pd.DataFrame(data)
    if not df.empty:
        st.dataframe(df)
    else:
        st.write("Aucune donnée disponible.")

def display_map(data):
    m = folium.Map(location=[44.837789, -0.57918], zoom_start=12)
    for item in data:
        folium.Marker(
            [item['latitude'], item['longitude']],
            icon=folium.Icon(color="green", icon="leaf"),
            popup=item.get('nom_courant_denomination', 'Sans nom'),
        ).add_to(m)
    folium_static(m)

def main():
    st.sidebar.title("Navigation")
    app_mode = st.sidebar.radio("Choisissez l'onglet", ["Organisations engagées", "Localisation des Entreprises"])

    data = get_data()

    if app_mode == "Organisations engagées":
        display_organisations_engagees(data)
    elif app_mode == "Localisation des Entreprises":
        display_map(data)

if __name__ == "__main__":
    main()
