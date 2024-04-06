import streamlit as st
import pandas as pd
import requests

def display_organisations_engagees(data):
    st.markdown("## OPEN DATA RSE")
    st.markdown("### Découvrez les organisations engagées RSE de la métropole de Bordeaux")

    if not data:
        st.write("No data available.")
    return

if __name__ == "__main__":
    display_organisations_engagees()
