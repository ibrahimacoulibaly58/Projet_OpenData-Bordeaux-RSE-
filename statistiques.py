# statistiques.py
import streamlit as st
import pandas as pd
import plotly.express as px
from data_manager import get_data
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

def display_companies_by_sector(df):
    sector_counts = df['libelle_section_naf'].value_counts().reset_index()
    sector_counts.columns = ['Secteur', 'Nombre']
    fig = px.bar(sector_counts, x='Secteur', y='Nombre', title="",
                 color='Nombre', labels={'Nombre':'Nombre d\'entreprises'}, template='plotly_white')
    fig.update_layout(xaxis_tickangle=-45, title_text="Répartition des entreprises par secteur d'activité", title_x=0.5)
    st.plotly_chart(fig)

def display_company_sizes(df):
    fig = px.histogram(df, x='tranche_effectif_entreprise', title="",
                       labels={'tranche_effectif_entreprise':'Taille de l\'entreprise'}, template='plotly_white')
    fig.update_traces(marker_color='green')
    fig.update_layout(title_text="Distribution des tailles d'entreprises", title_x=0.5)
    st.plotly_chart(fig)

def display_companies_by_commune(df):
    commune_counts = df['commune'].value_counts(normalize=True).reset_index()
    commune_counts.columns = ['Commune', 'Pourcentage']
    fig = px.pie(commune_counts, values='Pourcentage', names='Commune', title='',
                 template='plotly_white', hole=.3)
    fig.update_traces(textinfo='percent+label')
    fig.update_layout(title_text="Pourcentage d'entreprises par Commune", title_x=0.5)
    st.plotly_chart(fig)

def display_rse_actions_wordcloud(df):
    st.header("Nuage de mots Actions RSE")
    
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
        st.header("Répartition des entreprises par secteur d'activité")
        display_companies_by_sector(df)
        st.header("Distribution des tailles d'entreprises")
        display_company_sizes(df)
        st.header("Pourcentage d'entreprises par Commune")
        display_companies_by_commune(df)
        display_rse_actions_wordcloud(df)

if __name__ == "__main__":
    main()
