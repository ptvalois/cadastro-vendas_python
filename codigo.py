# Título - Sistema de Vendas
# Seçao Cadastrar Vendas
      # Campo Data
      # campo Vendedod - Anan, Bruno e Carla
      # Campo Produto - Notebook, Celular e Fone
      # Campo Quantidade 
      # Campo Valor
#    Botão Cadatrar - Quando acionado: 
      # 1- incluir a venda cadastrada na tabela
      # 2 - Aatualizar o Dashboard com o total de vendas, quantidade de produtos vendidos e o produto mais vendido
# Seção Vendas Cadastradas
      #  Tabela com as vendas cadastradas
# Seção Dashboard
      # Card/Métrica - Faturado Total
      # Grafico de Barras/Coluna -  Quantidade de Produtos Vendidos p/ vemdedor
      # Grafico de Pizza - Venda p /Produto
      
      # Pacotes necessários
      # Para executar o streamlit, executar no terminal> streamlit run - nome do arquivo (codigo.py) 
      
import streamlit as st
import pandas as pd
import plotly.express as px

# Carregar dados de vendas do arquivo CSV
try:
    tabela_vendas = pd.read_csv("vendas.csv")
except FileNotFoundError:
    tabela_vendas = pd.DataFrame(columns=["Data", "Vendedor", "Produto", "Quantidade", "Valor"])  
    

st.write ("# Sistema de Vendas")

# Seção Cadastrar Vendas  
st.sidebar.write("## Cadastrar Vendas")

data = st.sidebar.date_input("Data") 
vendedor = st.sidebar.selectbox("Vendedor", ["Ana", "Bruno", "Carla"])
produto = st.sidebar.selectbox("Produto", ["Notebook", "Celular", "Fone"])  
quantidade = st.sidebar.number_input("Quantidade", min_value=1, step=1)
valor = st.sidebar.number_input("Valor", min_value=0.0, step=0.01)
botao_cadastrar = st.sidebar.button("Cadastrar Venda")  

# 1- incluir a venda cadastrada na tabela
if botao_cadastrar:
  if  valor == 0.0:
    st.error("O valor da venda não pode ser zero!")
  else:
    nova_venda = [str(data), vendedor, produto, quantidade, valor]
    ultima_linha = len(tabela_vendas) # número de registro da tabela_vendas
    tabela_vendas.loc[ultima_linha] = nova_venda   
    tabela_vendas.to_csv("vendas.csv", index=False)
    st.success("Venda cadastrada com sucesso!")

# 2 - Aatualizar o Dashboard com o total de vendas, quantidade de produtos vendidos e o produto mais vendido


# Seção Visualizar Vendas Cadastradas
st.write("## Vendas Cadastradas")
st.dataframe(tabela_vendas)


# Seção Dashboard
st.write("## Dashboard")

#  Card/Métrica - Faturado Total  
faturamento=tabela_vendas["valor"].sum()
st.metric(label="Faturamento Total", value=f"R$ {faturamento:,.2f}")

# Grafico de Barras/Coluna -  Quantidade de Produtos Vendidos p/ vemdedor
garfico1=px.bar(tabela_vendas, x="vendedor", y="valor", color="produto", barmode="group")
st.plotly_chart(garfico1)

# Grafico de Pizza - Venda p /Produto
grafic2=px.pie(tabela_vendas, values="quantidade", names="produto", title="Venda por Produto", hole=0.5)
st.plotly_chart(grafic2)


# como execultar o streamlit na web: streamlit run nome_codigo.py
# Como fazer deploy  
    # ataulizar o arquivo requirements.txt com os pacotes necessários. Ex: streamlit, pandas, plotly
