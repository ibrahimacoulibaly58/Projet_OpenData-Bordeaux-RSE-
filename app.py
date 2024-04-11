import sys
import os

import streamlit as st
from organisations_engagees import display_organisations_engagees
from localisation import display_map
from statistiques import main as display_statistics
from ActionsRSE import display_actions_rse
from AnalyseActionsRSE import display_analyse_actions_rse

# Import modifiédes fonctions liées aux scripts
from projetRSE import display_rse_projects
from labelRSE import display_rse_labels
from marquesengagees import display_engaged_brands

def main():
    st.sidebar.title("OPEN DATA & IA au service de la RSE")
    section_principale = st.sidebar.radio(
        "Choisissez votre section",
        ["Data Bordeaux métropole", "Data bziiit"]
    )

    if section_principale == "Data Bordeaux métropole":
        app_mode = st.sidebar.radio(
            "Choisissez votre sous-section",
            ["Localisations", "Organisations engagées", "Statistiques", "Actions RSE", "Analyse actions RSE"]
        )
        if app_mode == "Localisations":
            display_map()
        elif app_mode == "Organisations engagées":
            display_organisations_engagees()
        elif app_mode == "Statistiques":
            display_statistics()
        elif app_mode == "Actions RSE":
            display_actions_rse()
        elif app_mode == "Analyse actions RSE":
            display_analyse_actions_rse()

    elif section_principale == "Data bziiit":
        ia_mode = st.sidebar.radio(
            "Choisissez votre sous-section",
            ["Labels RSE", "Projets RSE"]
        )
        if ia_mode == "Labels RSE":
            display_rse_labels()
        elif ia_mode == "Projets RSE":
            display_rse_projects()

    # Instructions communes à toutes les sections
    st.sidebar.markdown("---")
    st.sidebar.markdown("Powered by **bziiit IA RSE**")
    st.sidebar.markdown("2024 : Open source en Licence MIT")
    st.sidebar.markdown("info@bziiit.com")
    st.sidebar.markdown("---")

if __name__ == "__main__":
    main()