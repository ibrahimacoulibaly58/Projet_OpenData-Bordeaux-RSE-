import requests
import streamlit as st

def get_data():
    url = "https://opendata.bordeaux-metropole.fr/api/records/1.0/search/?dataset=met_etablissement_rse&q=&rows=10"  # Récupère seulement les 10 premiers pour le test
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        records = data.get("records", [])
        if records:  # Vérifie si des enregistrements ont été trouvés
            # Test d'impression pour les 3 premiers enregistrements
            for record in records[:3]:
                st.write(record)  # Imprime le record complet pour inspection
                fields = record.get("fields", {})
                point_geo = fields.get("geolocalisation")
                st.write("point_geo:", point_geo)  # Imprime spécifiquement point_geo
        else:
            st.error("Aucun enregistrement trouvé dans les données de l'API.")
            return []
    else:
        st.error(f"Échec de la récupération des données de l'API. Statut: {response.status_code}")
        return []
