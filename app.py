import streamlit as st
import pandas as pd
import requests
import folium
from streamlit_folium import folium_static

# Fonction pour récupérer les données de l'API
def get_data():
    url = "https://opendata.bordeaux-metropole.fr/api/records/1.0/search/?dataset=met_etablissement_rse&q=&rows=100"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        records = data.get("records", [])
        return [record["fields"] for record in records], data.get("nhits", 0)
    else:
        return [], 0

# Fonction pour l'onglet "Organisations engagées"
def display_organisations_engagees():
    st.markdown("## OPEN DATA RSE")
    st.markdown("### Découvrez les organisations engagées RSE de la métropole de Bordeaux")
    
    data, _ = get_data()
    if data:
        df = pd.DataFrame(data)
        df = df.rename(columns={
            "nom_courant_denomination": "Nom",
            "commune": "Commune",
            "libelle_section_naf": "Section NAF",
            "tranche_effectif_entreprise": "Effectif",
            "action_rse": "Action RSE"
        })
        df = df[["Nom", "Commune", "Section NAF", "Effectif", "Action RSE"]]
        st.dataframe(df, width=None, height=None)

# Fonction pour afficher la carte
def display_map():
    data, _ = get_data()
    if data:
        m = folium.Map(location=[44.84474, -0.60711], zoom_start=12)
        for item in data:
            try:
                # On tente d'extraire et de convertir lat et lon en flottants
                lat = float(item.get('point_geo', {}).get('lat'))
                lon = float(item.get('point_geo', {}).get('lon'))
                # On vérifie que lat et lon ont été correctement convertis (ne sont pas NaN)
                if lat and lon:
                    folium.Marker([lat, lon], popup=item.get("nom_courant_denomination", "Sans nom")).add_to(m)
            except (ValueError, TypeError):
                # Cette exception attrape les cas où la conversion en float échoue
                # ou les valeurs de lat/lon ne sont pas présentes ou pas valides
                continue
        folium_static(m)

# Fonction pour l'onglet "Dialoguer avec l'assistant IA RSE bziiit"
def display_dialogue():
    st.markdown("# Patientez quelques heures encore... :)")

# Main function orchestrating the app UI
def main():
    st.sidebar.title("Navigation")
    app_mode = st.sidebar.radio("Choisissez l'onglet", ["Organisations engagées", "Carte", "Dialoguer avec l'assistant IA RSE bziiit"])

    if app_mode == "Organisations engagées":
        display_organisations_engagees()
    elif app_mode == "Carte":
        display_map()
    elif app_mode == "Dialoguer avec l'assistant IA RSE bziiit":
        display_dialogue()

if __name__ == "__main__":
    main()
