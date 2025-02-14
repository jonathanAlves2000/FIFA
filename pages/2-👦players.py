import streamlit as st

st.set_page_config(
    page_title="Players",
    page_icon = "⛹️‍♂️",
    layout = "wide"
)

df_data = st.session_state["data"]

clubes = df_data["Club"].value_counts().index
club = st.sidebar.selectbox("Clube", clubes)

df_players = df_data[(df_data["Club"] == club)]
players = df_players["Name"].value_counts().index
player = st.sidebar.selectbox("Jogador", players)

player_stats = df_data[df_data["Name"] == player].iloc[0]

st.image(player_stats["Photo"])
st.title(player_stats["Name"])

st.markdown(f"**Clube:** {player_stats['Club']}")
st.markdown(f"**Posição:** {player_stats['Position']}")

col1, col2, col3, col4 = st.columns(4)
col1.markdown(f"**Idade:** {player_stats['Age']} Anos")
col2.markdown(f"**Altura** {player_stats['Height(cm.)'] / 100} m")
col3.markdown(f"**Peso:** {player_stats['Weight(lbs.)']} lbs")

st.subheader(f"Overall {player_stats['Overall']}")
overall = int(player_stats["Overall"])

# Define a cor com base no valor de "Overall"
if overall >= 85:
    bar_color = "green"
elif 70 <= overall < 85:
    bar_color = "yellow"
else:
    bar_color = "red"

# Cria uma barra de progresso personalizada
progress_html = f"""
<div style="width: 100%; background-color: #ddd; border-radius: 8px;">
    <div style="
        width: {overall}%; 
        background-color: {bar_color}; 
        height: 20px; 
        border-radius: 8px;">
    </div>
</div>
<p style="text-align: center;">{overall}%</p>
"""

st.markdown(progress_html, unsafe_allow_html=True)

col1, col2, col3, col4, = st.columns(4)
col1.metric(label="Valor de mercado", value=f"£ {player_stats['Value(£)']:,}")
col2.metric(label="Remuneração semanal", value=f"£ {player_stats['Wage(£)']:,}")
col3.metric(label="Cláusula de rescisão", value=f"£ {player_stats['Release Clause(£)']:,}")



