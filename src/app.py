import sys
import os

# Adiciona o diretório raiz do projeto (sales_analysis) ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import pandas as pd
import plotly.express as px

# Configuração da Página
st.set_page_config(page_title="Dashboard de Vendas", layout="wide")

# Upload do Arquivo
upload_file = st.file_uploader('Faça upload do arquivo CSV', type='csv')

if upload_file is not None:
    # Carrega os dados do arquivo enviado
    data = pd.read_csv(upload_file)
    st.write('Dados carregados:')
    st.write(data)

    # Processamento e exibição do dashboard
    st.title("Dashboard de Vendas")
    st.markdown("## Análise de Dados de Vendas")

    # Cálculo das Métricas
    faturamento_total = data["Valor Total da Venda"].sum()
    quantidade_total = data["Quantidade Vendida"].sum()
    media_preco_produto = data["Preço"].mean()
    compras_concluidas = data[data["Status da Venda"] == "Concluída"].shape[0]
    percentual_concluidas = (compras_concluidas / len(data)) * 100

    # Métricas no Topo
    col1, col2, col3, col4, col5 = st.columns(5)

    col1.metric(label="Faturamento Total", value=f"R$ {faturamento_total:,.2f}")
    col2.metric(label="Quantidade Total Vendida", value=f"{quantidade_total}")
    col3.metric(label="Média de Preço por Produto", value=f"R$ {media_preco_produto:,.2f}")
    col4.metric(label="Compras Concluídas", value=f"{compras_concluidas}")
    col5.metric(label="% Compras Concluídas", value=f"{percentual_concluidas:.2f}%")

    # Gráficos
    st.markdown("---")
    st.markdown("### Gráficos de Análise")

    # Gráfico 1: Faturamento Mensal
    st.subheader("Faturamento Mensal")
    data["Data de Compra"] = pd.to_datetime(data["Data da Venda"])
    data["Mês"] = data["Data de Compra"].dt.to_period("M")

    faturamento_mensal = data.groupby("Mês")["Valor Total da Venda"].sum().reset_index()
    faturamento_mensal["Mês"] = faturamento_mensal["Mês"].astype(str)

    fig1 = px.line(faturamento_mensal, x="Mês", y="Valor Total da Venda", title="Faturamento Mensal", markers=True)
    st.plotly_chart(fig1, use_container_width=True)

    # Gráfico 2: Quantidade Vendida por Produto
    st.subheader("Quantidade Vendida por Produto")
    quantidade_produto = data.groupby("Produto")["Quantidade Vendida"].sum().sort_values(ascending=False).reset_index()

    fig2 = px.bar(quantidade_produto, x="Produto", y="Quantidade Vendida", title="Quantidade Vendida por Produto", text_auto=True)
    st.plotly_chart(fig2, use_container_width=True)

    # Gráfico 3: Método de Pagamento
    st.subheader("Distribuição por Método de Pagamento")
    metodo_pagamento = data["Método de Pagamento"].value_counts().reset_index()
    metodo_pagamento.columns = ["Método de Pagamento", "Contagem"]

    fig3 = px.pie(metodo_pagamento, names="Método de Pagamento", values="Contagem", title="Método de Pagamento")
    st.plotly_chart(fig3, use_container_width=True)

    # Gráfico 4: Status da Compra
    st.subheader("Distribuição por Status da Compra")
    status_compra = data["Status da Venda"].value_counts().reset_index()
    status_compra.columns = ["Status da Venda", "Contagem"]

    fig4 = px.bar(status_compra, x="Status da Venda", y="Contagem", title="Status da Venda", text_auto=True)
    st.plotly_chart(fig4, use_container_width=True)

else:
    # Mensagem pedindo o upload do arquivo
    st.warning('Por favor, faça o upload de um arquivo CSV antes de começar.')
