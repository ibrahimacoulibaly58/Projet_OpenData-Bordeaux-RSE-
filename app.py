import streamlit as st
from organisations_engagees import display_organisations_engagees
from localisation import display_map
from statistiques import main as display_statistics

# Main function orchestrating the app UI
def main():
    st.sidebar.title("Navigation")
    app_mode = st.sidebar.radio("Choisissez l'onglet", ["Organisations engagées", "Localisations", "Statistiques"])

    if app_mode == "Organisations engagées":
        display_organisations_engagees()
    elif app_mode == "Localisations":
        display_map()
    elif app_mode == "Statistiques":
        display_statistics()

if __name__ == "__main__":
    main()
