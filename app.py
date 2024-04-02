# Importation des bibliothèques nécessaires
import streamlit as st
import pandas as pd
import requests

# Fonction pour récupérer les données de l'API
def get_data():
    """
    Cette fonction effectue une requête GET vers l'API spécifiée et retourne une liste des enregistrements (records).
    Elle utilise l'URL de l'API pour récupérer les données des établissements engagés dans la RSE à Bordeaux.
    La fonction gère également les éventuelles erreurs de requête.
    
    Returns:
        List[Dict]: Une liste de dictionnaires où chaque dictionnaire représente les données d'un établissement.
    """
    # URL de l'API pour accéder aux données des établissements RSE
    url = "https://opendata.bordeaux-metropole.fr/api/records/1.0/search/?dataset=met_etablissement_rse&q=&rows=100"
    # Envoi de la requête GET à l'API
    response = requests.get(url)
    # Vérification du statut de la réponse
    if response.status_code == 200:
        # Conversion de la réponse en JSON
        data = response.json()
        # Récupération des enregistrements (records) depuis la réponse
        records = data.get("records", [])
        # Extraction des champs (fields) de chaque enregistrement
        return [record["fields"] for record in records]
    else:
        # Retourne une liste vide si la requête échoue
        return []

# Fonction pour afficher les organisations engagées dans l'application Streamlit
def display_organisations_engagees():
    """
    Cette fonction récupère les données des organisations engagées via la fonction `get_data`, les convertit en un DataFrame pandas,
    puis utilise Streamlit pour les afficher dans un tableau sur l'interface utilisateur.
    """
    # Récupération des données via la fonction get_data
    data = get_data()
    # Vérification si des données ont été récupérées
    if data:
        # Conversion des données en DataFrame pandas pour une manipulation et un affichage plus faciles
        df = pd.DataFrame(data)
        # Affichage du DataFrame dans l'application Streamlit
        st.write("Organisations engagées", df)
    else:
        # Message d'erreur en cas d'absence de données
        st.write("Aucune donnée disponible.")

# Point d'entrée principal de l'application Streamlit
if __name__ == "__main__":
    # Configuration de la barre latérale pour la navigation entre différents onglets
    st.sidebar.title("Navigation")
    # Option de sélection pour les différents onglets de l'application
    app_mode = st.sidebar.selectbox("Choisissez l'onglet", ["Organisations engagées", "Autre Onglet"])

    # Affichage de l'onglet "Organisations engagées" si sélectionné
    if app_mode == "Organisations engagées":
        display_organisations_engagees()
    # Cette structure peut être étendue pour ajouter d'autres onglets à l'application
