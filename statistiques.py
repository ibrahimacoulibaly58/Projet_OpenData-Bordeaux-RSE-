# statistiques.py
import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
from data_manager import get_data
from wordcloud import WordCloud, STOPWORDS

def display_companies_by_sector(df):
    sector_counts = df['libelle_section_naf'].value_counts().reset_index()
    sector_counts.columns = ['Secteur', 'Nombre']
    fig = px.bar(sector_counts, x='Secteur', y='Nombre', title="Répartition des entreprises par secteur d'activité",
                 color='Nombre', labels={'Nombre':'Nombre d\'entreprises'}, template='plotly_white')
    fig.update_layout(xaxis_tickangle=-45)
    st.plotly_chart(fig)

def display_company_sizes(df):
    fig = px.histogram(df, x='tranche_effectif_entreprise', title="Distribution des tailles d'entreprises",
                       labels={'tranche_effectif_entreprise':'Taille de l\'entreprise'}, template='plotly_white')
    fig.update_traces(marker_color='green')
    st.plotly_chart(fig)

def display_rse_actions_wordcloud(df):
    st.title("Cartographie des Actions RSE")
    
    custom_stopwords = set(["d ", "des", "qui", "ainsi", "toute", "hors", "plus", "cette", "afin", "via", "d'", "sa", "dans", "ont", "avec", "aux", "ce", "chez", "ont", "cela", "la", "un", "avons", "par", "c'est", "s'est", "aussi", "leurs", "d'un", "nos", "les", "sur", "ses", "tous", "nous", "du", "notre", "de", "et", "est", "pour", "le", "une", "se", "en", "au", "à", "que", "sont", "leur", "son"])
    stopwords = STOPWORDS.union(custom_stopwords)
    text = " ".join(action for action in df['action_rse'].dropna())
    wordcloud = WordCloud(stopwords=stopwords, background_color="white", width=800, height=400).generate(text)
    
    fig, ax = plt.subplots()
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis('off')
    st.pyplot(fig)

def main():
    st.title("Statistiques sur les entreprises engagées RSE")
    data, _ = get_data()
    df = pd.DataFrame(data)
    
    if not df.empty:
        display_companies_by_sector(df)
        display_company_sizes(df)
        display_rse_actions_wordcloud(df)

if __name__ == "__main__":
    main()
