import streamlit as st
import webbrowser
import pandas as pd
from datetime import datetime

st.set_page_config(
    page_title="Home",
    page_icon = "🏠",
    layout = "wide"
)

if "data" not in st.session_state:
    df_data = pd.read_csv("datasets/CLEAN_FIFA23_official_data.csv", index_col=0)
    df_data = df_data[df_data["Contract Valid Until"] >= datetime.today().year]
    df_data = df_data[df_data["Value(£)"] > 0]
    df_data = df_data.sort_values(by="Overall", ascending=False)
    st.session_state["data"] = df_data

st.markdown("# FIFA2023 Oficial Dataset! ⚽")
st.sidebar.markdown("Desenvolvido por [Jonathan Alves](https://www.linkedin.com/in/jonathan-alves-408283183/)")

btn = st.button("Acesse os dados no Kaggle")
if btn:
    webbrowser.open_new_tab("https://docs.streamlit.io/develop/api-reference/text") 
    
st.markdown(
    
    '''O FIFA 23 traz um vasto conjunto de dados sobre jogadores, clubes e seleções do mundo todo. As estatísticas incluem atributos como velocidade, drible, passe, 
    finalização e defesa, influenciando o desempenho dos jogadores no jogo. O Overall Rating (OVR) é uma das métricas mais importantes, indicando a qualidade geral do atleta. 
    Os dados também cobrem ligas, times e até o desempenho em diferentes modos de jogo, como Ultimate Team e Modo Carreira. Além disso, com a tecnologia HyperMotion 2, 
    o jogo oferece animações mais realistas baseadas em dados coletados de partidas reais.'''
    
)