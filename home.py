import streamlit as st
from CRUD import create as c, read as r, update as u, delete as d

st.set_page_config(
    page_title="#IAAD",
    page_icon="🗂️",
    layout="wide"
)

st.sidebar.title("Menu")

menu_options = ["🎲Página Inicial", "📝Create", "🔍Read", "🔃Update", "📂Delete"]
selected_option = st.sidebar.selectbox("Selecione uma operação CRUD:", menu_options)

if selected_option == "Página Inicial":
    st.title("🎲Página Inicial")
    st.write("Este projeto consiste na implementação das operações CRUD, do MySQL, aliada ao Streamlit.")
    st.write("Integrantes: Caio Farias, Keila Viana, Leonardo Antônio e Raquel Silva.")
elif selected_option == "📝Create":
    c.main()
elif selected_option == "🔍Read":
    r.main()
elif selected_option == "🔃Update":
    u.main()
elif selected_option == "📂Delete":
    d.main()
