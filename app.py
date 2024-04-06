import streamlit as st
from organisations_engagees import display_organisations_engagees
from localisation import display_map, get_data

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
