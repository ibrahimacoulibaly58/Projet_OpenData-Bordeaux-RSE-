import requests
import streamlit as st
from organisations_engagees import display_organisations_engagees
from localisation import display_map

def get_data():
    url = "https://opendata.bordeaux-metropole.fr/api/records/1.0/search/?dataset=met_etablissement_rse&q=&rows=100"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            records = data.get("records", [])
            cleaned_data = []
            for record in records:
                fields = record.get("fields", {})
                geoloc = fields.get("geolocalisation")
                if geoloc and isinstance(geoloc, list) and len(geoloc) == 2:
                    lat, lon = geoloc
                    cleaned_data.append({"lat": lat, "lon": lon, "name": fields.get("nom_courant_denomination", "Inconnu")})
            return cleaned_data
        else:
            st.error(f"Failed to fetch data. Status code: {response.status_code}")
            return []
    except requests.RequestException as e:
        st.error(f"Error occurred: {e}")
        return []

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
