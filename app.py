import streamlit as st
from organisations_engagees import display_organisations_engagees
from localisation import display_map
from statistiques import main as display_statistics
from ActionsRSE import display_actions_rse

# Import des fonctions IA depuis le sous-répertoire
from IA_RSE.analyseActionsRSE import display_analyse_actions_rse

# from IA_COMMERCE.Doc_Ref_COMMERCE import display_doc_ref_commerce
# from IA_COMMERCE.BP_COMMERCE import display_bp_commerce
# from IA_COMMERCE.Financement_TE_COMMERCE import display_Financement_TE_Commerce
# from IA_COMMERCE.IA_COMMERCE import display_ia_commerce

def main():
    st.sidebar.title("OPEN DATA & IA au service de la RSE")
    section_principale = st.sidebar.radio(
        "Choisissez votre section",
        ["Data Bordeaux métropole", "Data bziiit", "IA RSE"]
    )

    if section_principale == "Data Bordeaux métropole":
        app_mode = st.sidebar.radio(
            "Choisissez votre onglet",
            ["Organisations engagées", "Localisations", "Statistiques", "Actions RSE"]
        )
        if app_mode == "Organisations engagées":
            display_organisations_engagees()
        elif app_mode == "Localisations":
            display_map()
        elif app_mode == "Statistiques":
            display_statistics()
        elif app_mode == "Actions RSE":
            display_actions_rse()

    elif section_principale == "Data bziiit":
        ia_mode = st.sidebar.radio(
            "Choisissez votre onglet",
            ["Projets RSE", "Labels RSE", "Marques engagées"]
        )
#        if ia_mode == "Documents Référence":
#            display_doc_ref_commerce()
#        elif ia_mode == "Bonnes Pratiques":
#            display_bp_commerce()
#        elif ia_mode == "Financements":
#            display_Financement_TE_Commerce()
#        elif ia_mode == "Dialogue IA":
#            display_ia_commerce()

    elif section_principale == "IA RSE":
        ia_mode = st.sidebar.radio(
            "Choisissez votre onglet",
            ["Analyse actions RSE"]
        )
        if ia_mode == "Analyse actions RSE":
           display_analyse_action_rse()

    # Instructions communes à toutes les sections
    st.sidebar.markdown("---")
    st.sidebar.markdown("Powered by **bziiit IA RSE**")
    st.sidebar.markdown("2024 : Open source en Licence MIT")
    st.sidebar.markdown("info@bziiit.com")
    st.sidebar.markdown("---")

if __name__ == "__main__":
    main()
