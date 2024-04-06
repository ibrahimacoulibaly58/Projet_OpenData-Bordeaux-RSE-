# statistiques.py
import streamlit as st
import pandas as pd
import plotly.express as px
from data_manager import get_data

def display_companies_by_sector(df):
    # Assurez-vous d'utiliser le nom correct de la colonne ici
    sector_counts = df['libelle_section_naf'].value_counts().reset_index()
    sector_counts.columns = ['Secteur', 'Nombre']
    fig = px.bar(sector_counts, x='Secteur', y='Nombre', title="Répartition des entreprises par secteur d'activité",
                 color='Nombre', labels={'Nombre':'Nombre d\'entreprises'}, template='plotly_white')
    # Rotation des étiquettes de l'axe des x pour une meilleure lisibilité
    fig.update_layout(xaxis_tickangle=-45)
    st.plotly_chart(fig)

def display_company_sizes(df):
    # Remplacez 'tranche_effectif_entreprise' par le nom correct de la colonne
    fig = px.histogram(df, x='tranche_effectif_entreprise', title="Distribution des tailles d'entreprises",
                       labels={'tranche_effectif_entreprise':'Taille de l\'entreprise'}, template='plotly_white')
    fig.update_traces(marker_color='green')
    st.plotly_chart(fig)

def display_rse_actions_wordcloud(df):
    st.title("Cartographie des Actions RSE")
    st.markdown("Cette section affichera un nuage de mots des actions RSE.")

def main():
    st.title("Statistiques sur les entreprises engagées RSE")
    data, _ = get_data()
    df = pd.DataFrame(data)
    
    # Affiche les noms des colonnes du DataFrame
    if not df.empty:
        st.write("Colonnes du DataFrame:", df.columns.tolist())
        display_companies_by_sector(df)
        display_company_sizes(df)
        display_rse_actions_wordcloud(df)
    else:
        st.write("Aucune donnée à afficher pour le moment.")

if __name__ == "__main__":
    main()
