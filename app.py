import streamlit as st
from organisations_engagees import display_organisations_engagees
from localisation import display_map

def get_data():
    url = "https://opendata.bordeaux-metropole.fr/api/records/1.0/search/?dataset=met_etablissement_rse&q=&rows=100"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Cela va déclencher une exception pour les réponses non-200
        data = response.json()
        records = data.get("records", [])
        if records:
            return [record.get("fields") for record in records]
        else:
            st.error("Aucun enregistrement trouvé dans les données de l'API.")
            return []
    except requests.RequestException as e:
        st.error(f"Erreur lors de la récupération des données de l'API: {e}")
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
