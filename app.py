import streamlit as st
import pandas as pd
import requests
import folium
from streamlit_folium import folium_static

# Fonction pour récupérer les données de l'API (ajustez selon vos besoins)
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
        # Sélection et réorganisation des colonnes
        df = df[["nom_courant_denomination", "commune", "libelle_section_naf", "tranche_effectif_entreprise", "action_rse"]]
        st.dataframe(df, width=None, height=None)  # Ajustez width et height si nécessaire

# Fonction pour afficher la carte avec Folium (à ajuster selon vos données)
def display_map():
    data, _ = get_data()
    if data:
        # Création d'une carte centrée autour de Bordeaux
        m = folium.Map(location=[44.8378, -0.5792], zoom_start=12)
        # Ajout des entreprises sur la carte
        for item in data:
            if 'geolocalisation' in item:
                folium.Marker(location=[item['geolocalisation'][0], item['geolocalisation'][1]],
                              popup=item["nom_courant_denomination"]).add_to(m)
        folium_static(m)

# Fonction pour l'onglet "Dialoguer avec l'assistant IA RSE bziiit"
def display_dialogue():
    st.markdown("# Patientez quelques heures encore... :)")

# Création des onglets de l'application
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