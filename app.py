import streamlit as st
import pandas as pd
import requests
import folium
from streamlit_folium import folium_static
from transformers import pipeline

import tensorflow as tf
print("TensorFlow version:", tf.__version__)

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

# Fonction pour l'onglet "GeoRSE Insights"
def display_geo_rse_insights():
    data, _ = get_data()
    if data:
        m = folium.Map(location=[44.84474, -0.60711], zoom_start=11)
        for item in data:
            point_geo = item.get('point_geo', [])
            if point_geo:
                lat, lon = point_geo
                lat, lon = float(lat), float(lon)
                if lat and lon:
                    folium.Marker(
                        [lat, lon],
                        popup=f"<b>{item.get('nom_courant_denomination', 'Sans nom')}</b><br>Action RSE: {item.get('action_rse', 'Non spécifié')}",
                        icon=folium.Icon(color="green", icon="leaf"),
                    ).add_to(m)
        folium_static(m)

# Fonction pour la classification des actions RSE
def classify_rse_actions(descriptions):
    classifier = pipeline("zero-shot-classification", model="typeform/distilbert-base-uncased-mnli")
    categories = [
        "La gouvernance de la structure",
        "Les droits humains",
        "Les conditions et relations de travail",
        "La responsabilité environnementale",
        "La loyauté des pratiques",
        "Les questions relatives au consommateur et à la protection du consommateur",
        "Les communautés et le développement local"
    ]
    
    classified_data = []
    for description in descriptions:
        result = classifier(description, categories)
        top_category = result['labels'][0]
        classified_data.append(top_category)
    
    return classified_data

# Nouvelle fonction pour l'onglet de classification RSE
def display_rse_categorizer():
    st.header("Classification des Actions RSE")
    st.write("Cet outil classe les actions RSE des entreprises selon les normes ISO 26000.")
    
    data, _ = get_data()
    if data:
        descriptions = [item['action_rse'] for item in data if 'action_rse' in item]
        categories = classify_rse_actions(descriptions)
        for i, category in enumerate(categories):
            st.write(f"Action RSE: {descriptions[i]}")
            st.write(f"Catégorie prédite: {category}")
            st.write("---")

# Main function orchestrating the app UI
def main():
    st.sidebar.title("Navigation")
    app_mode = st.sidebar.radio("Choisissez l'onglet", ["Organisations engagées", "GeoRSE Insights", "Classification RSE"])

    if app_mode == "Organisations engagées":
        display_organisations_engagees()
    elif app_mode == "GeoRSE Insights":
        display_geo_rse_insights()
    elif app_mode == "Classification RSE":
        display_rse_categorizer()

if __name__ == "__main__":
    main()
