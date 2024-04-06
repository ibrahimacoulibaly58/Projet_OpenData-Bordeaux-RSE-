# statistiques.py
import streamlit as st
import pandas as pd
import plotly.express as px
from data_manager import get_data

def display_companies_by_sector(df):
    sector_counts = df['Libellé groupe NAF'].value_counts().reset_index()
    sector_counts.columns = ['Secteur', 'Nombre']
    fig = px.bar(sector_counts, x='Secteur', y='Nombre', title="Répartition des entreprises par secteur d'activité",
                 color='Nombre', labels={'Nombre':'Nombre d\'entreprises'}, template='plotly_white')
    fig.update_layout(transition_duration=500)
    st.plotly_chart(fig)

def display_company_sizes(df):
    fig = px.histogram(df, x='tranche_effectif_entreprise', title="Distribution des tailles d'entreprises",
                       labels={'tranche_effectif_entreprise':'Taille de l\'entreprise'}, template='plotly_white')
    fig.update_traces(marker_color='green')
    st.plotly_chart(fig)

def display_rse_actions_wordcloud(df):
    # Génération d'un nuage de mots serait normalement fait ici.
    # Un placeholder pour l'intégration d'un vrai nuage de mots en utilisant une bibliothèque appropriée.
    st.title("Cartographie des Actions RSE")
    st.markdown("Cette section affichera un nuage de mots des actions RSE.")

def main():
    st.title("Statistiques sur les entreprises engagées RSE")
    data, _ = get_data()
    df = pd.DataFrame(data)
    
    if not df.empty:
        display_companies_by_sector(df)
        display_company_sizes(df)
        display_rse_actions_wordcloud(df)
    else:
        st.write("Aucune donnée à afficher pour le moment.")

if __name__ == "__main__":
    main()
