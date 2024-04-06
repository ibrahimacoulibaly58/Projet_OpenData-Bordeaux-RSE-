
import requests
import streamlit as st
from organisations_engagees import display_organisations_engagees
from localisation import display_map

def get_data():
    url = "https://opendata.bordeaux-metropole.fr/api/records/1.0/search/?dataset=met_etablissement_rse&q=&rows=100"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json().get('records', [])
            cleaned_data = [{'nom': record['fields'].get('nom'),
                             'adresse': record['fields'].get('adresse'),
                             'engagement_rse': record['fields'].get('rse', 'Non'),
                             'lat': record['fields'].get('geo_point_2d', [None, None])[0],
                             'lon': record['fields'].get('geo_point_2d', [None, None])[1]}
                            for record in data if 'geo_point_2d' in record['fields']]
            return cleaned_data
    except requests.RequestException as e:
        print(f"Erreur lors de la récupération des données : {e}")
        return []

def main():
    st.title("Application RSE Bordeaux Métropole")
    
    data = get_data()
    
    if data:
        display_organisations_engagees(data)
        display_map(data)
    else:
        st.write("Aucune donnée disponible pour le moment.")
        
if __name__ == "__main__":
    main()
