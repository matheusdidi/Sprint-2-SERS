import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="ChargeGrid Intelligence",
    page_icon="⚡",
    layout="wide"
)

st.title("⚡ ChargeGrid Intelligence")

st.write(
    "EV Challenge 2026 | Sistema inteligente de controle de demanda para eletropostos."
)

st.divider()

potencia_maxima = st.slider(
    "Potência Máxima da Instalação (kW)",
    10,
    100,
    30
)

consumo_predio = st.slider(
    "Consumo Atual do Prédio (kW)",
    0,
    potencia_maxima,
    18
)

potencia_solicitada = st.slider(
    "Potência Solicitada pelo Veículo (kW)",
    1,
    50,
    22
)

potencia_disponivel = (
    potencia_maxima - consumo_predio
)

if potencia_solicitada > potencia_disponivel:

    potencia_liberada = potencia_disponivel

    st.warning(
        "⚠ Controle de demanda ativado!"
    )

else:

    potencia_liberada = potencia_solicitada

    st.success(
        "✅ Carregamento normal"
    )

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Potência Disponível",
        f"{potencia_disponivel} kW"
    )

with col2:
    st.metric(
        "Potência Liberada",
        f"{potencia_liberada} kW"
    )

dados = pd.DataFrame({
    "Categoria": [
        "Consumo do Prédio",
        "Potência Liberada"
    ],
    "Potência": [
        consumo_predio,
        potencia_liberada
    ]
})

fig = px.bar(
    dados,
    x="Categoria",
    y="Potência",
    title="Distribuição de Potência"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

st.subheader("Benefícios Sustentáveis")

st.write(
"""
• Redução de picos de demanda

• Melhor utilização da infraestrutura elétrica

• Preparação para integração com energia solar

• Incentivo à mobilidade elétrica sustentável
"""
)