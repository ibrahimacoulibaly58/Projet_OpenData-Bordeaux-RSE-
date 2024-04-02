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

# Fonction pour afficher la carte ou les données géographiques
def display_map(items):
    for item in items:
        try:
            # Vérifie si 'point_geo' existe et contient 'lat'
            if 'point_geo' in item and 'lat' in item['point_geo']:
                lat_value = item['point_geo']['lat']
                if lat_value:  # Si 'lat' n'est pas vide, tente de convertir en float
                    lat = float(lat_value)
                    st.write(f"Latitude: {lat}")
                else:  # Si 'lat' est vide
                    st.error(f"La latitude est vide pour l'item: {item}")
            else:  # Si 'point_geo' ou 'lat' est absent
                st.error(f"Données géographiques incomplètes ou absentes pour l'item: {item}")
        except ValueError as e:
            # Si la conversion en float échoue
            st.error(f"Erreur lors de la conversion de la latitude pour l'item: {item}. Erreur: {e}")

def main():
    # Création d'une simple interface utilisateur pour afficher les latitudes
    st.title('Affichage des données géographiques')

    # Simuler des données d'entrée avec différents cas
    items = [
        {'name': 'Location A', 'point_geo': {'lat': '48.8566', 'lon': '2.3522'}},
        {'name': 'Location B', 'point_geo': {'lat': '', 'lon': '2.3522'}},  # Cet élément aura une latitude vide
        {'name': 'Location C'},  # Cet élément manquera de données géographiques
        {'name': 'Location D', 'point_geo': {'lat': 'not_a_float', 'lon': '2.3522'}}  # Cet élément aura une erreur de conversion
    ]
    
    # Appel de la fonction pour afficher les données
    display_map(items)

if __name__ == "__main__":
    main()
