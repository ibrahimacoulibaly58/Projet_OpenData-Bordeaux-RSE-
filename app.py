import streamlit as st

x = st.slider('Sélectionner une valeur')
st.write(x, 'Le carré de la valeur est ', x * x)


