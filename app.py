import streamlit as st
import pandas as pd
import requests
import folium
from streamlit_folium import folium_static
from organisations_engagees import display_organisations_engagees
from localisation import display_map

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

# Main function orchestrating the app UI
def main():
    st.sidebar.title("Navigation")
    app_mode = st.sidebar.radio("Choisissez l'onglet", ["Organisations engagées", "Localisations"])

    if app_mode == "Organisations engagées":
        display_organisations_engagees()
    elif app_mode == "Localisations":
        display_map()
    
if __name__ == "__main__":
    main()
