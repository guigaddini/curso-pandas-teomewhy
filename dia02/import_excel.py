# %%
# Importando a biblioteca pandas
import pandas as pd

# %%
# Lendo o arquivo Excel e armazenando os dados em um DataFrame
df = pd.read_excel("../data/transactions.xlsx")
df

# %%
# Exibindo a forma do DataFrame (número de linhas e colunas)
df.shape

# %%
# Exibindo as primeiras linhas do DataFrame
df.head()

# %%
# Exibindo as últimas linhas do DataFrame
df.tail()

# %%
# Selecionando apenas as colunas especificadas
colunas = ['UUID', "Points", 'IdCustomer', "DtTransaction"]
df = df[colunas]
df

# %%
# Exibindo informações sobre o DataFrame, incluindo uso de memória
df.info(memory_usage='deep')
