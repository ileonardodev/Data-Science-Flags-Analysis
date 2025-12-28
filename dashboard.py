import streamlit as st
import pandas as pd
import sqlite3

# 1. Título e Configuração da Página
st.set_page_config(page_title="Monitor de Bandeiras", layout="wide")
st.title("🌍 Dashboard de IA: Previsão de Religião por Bandeiras")

# 2. Conectando no Banco de Dados (que você acabou de validar!)
conn = sqlite3.connect("bandeiras_db.db")
df = pd.read_sql("SELECT * FROM relatorios_previsao", conn)

# 3. Métricas (Os números grandes)
col1, col2, col3 = st.columns(3)
col1.metric("Total de Países Analisados", len(df))

# Calculando a média de acertos
acuracia_media = df['acertou'].mean() * 100
col2.metric("Acurácia Global do Modelo", f"{acuracia_media:.2f}%")

# Contando erros
erros = len(df[df['acertou'] == 0])
col3.metric("Total de Erros", erros, delta=-erros, delta_color="inverse")

# 4. Gráficos e Tabelas
st.divider()

col_grafico, col_dados = st.columns([2, 1])

with col_grafico:
    st.subheader("Onde o modelo mais acertou?")
    # Filtra só os acertos e conta por religião
    acertos_por_religiao = df[df['acertou'] == 1]['religion'].value_counts()
    st.bar_chart(acertos_por_religiao, color="#00FF00")

with col_dados:
    st.subheader("Amostra dos Dados")
    # Mostra uma tabela interativa
    st.dataframe(df[['name', 'religion', 'religiao_prevista', 'acertou']], height=400)