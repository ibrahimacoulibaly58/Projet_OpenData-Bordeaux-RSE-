# IA_RSE/AnalyseActionsRSE.py
import streamlit as st
import pandas as pd
from data_manager import get_data

# Fonction pour l'onglet "Analyse actions RSE"
def display_analyse_actions_rse():
    st.markdown("## IA RSE")
    st.markdown("### Classification des actions RSE selon les critères de la norme ISO 26000")
    
