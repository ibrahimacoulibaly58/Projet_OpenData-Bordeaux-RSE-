
import streamlit as st
import pandas as pd

def display_organisations_engagees(data):
    st.markdown("## OPEN DATA RSE")
    st.markdown("### Découvrez les organisations engagées RSE de la métropole de Bordeaux")

    if not data:
        st.write("No data available.")
    else:
        # Supposons que les données sont une liste de dictionnaires, où chaque dictionnaire contient des informations sur une organisation
        df = pd.DataFrame(data)
        st.dataframe(df)

if __name__ == "__main__":
    # Pour tester, nous passerons un ensemble de données fictives, car nous ne pouvons pas exécuter Streamlit ici
    # Voici un exemple de structure de données attendue
    test_data = [
        {'nom': 'Entreprise A', 'adresse': 'Adresse A', 'engagement_rse': 'Oui'},
        {'nom': 'Entreprise B', 'adresse': 'Adresse B', 'engagement_rse': 'Non'},
        # Ajouter plus de données fictives si nécessaire
    ]
    display_organisations_engagees(test_data)
