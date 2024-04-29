import streamlit as st

# Titre "PORTFOLIO" centré au milieu
st.markdown("<h1 style='text-align: center;'>PORTFOLIO</h1>", unsafe_allow_html=True)
# Texte "Agit Firat Morcicek" centré au milieu
st.markdown("<h2 style='text-align: center;'>Agit Firat Morcicek</h2>", unsafe_allow_html=True)

# Images carrées côte à côte
col1, col2 = st.columns(2)  # Crée deux colonnes

# Insérer les images dans les colonnes
with col1:
    st.image("image1.jpeg", width=200)  # Remplacez "image1.png" par le chemin de votre première image

with col2:
    st.image("image2.png", width=200)  # Remplacez "image2.png" par le chemin de votre deuxième image
