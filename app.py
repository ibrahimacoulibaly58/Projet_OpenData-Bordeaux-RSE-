import streamlit as st
import pandas as pd
import requests
import folium
from streamlit_folium import folium_static
from data_manager import get_data
from organisations_engagees import display_organisations_engagees
from localisation import display_map

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
