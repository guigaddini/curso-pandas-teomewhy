# %%
# Importando a biblioteca pandas
import pandas as pd

# %%
# Lendo o arquivo CSV e armazenando os dados em um DataFrame
df_customers = pd.read_csv("../data/customers.csv", sep=";")
df_customers

#%%
# Exibindo a forma do DataFrame (número de linhas e colunas)
df_customers.shape

# %%
# Exibindo informações sobre o DataFrame, incluindo uso de memória
df_customers.info(memory_usage='deep')

# %%
# Obtendo o sumário estatístico da coluna "Points"
df_customers["Points"].describe()

# %%
# Selecionando os clientes com mais de 1000 pontos
condicao = df_customers["Points"] > 1000
df_customers[condicao]

# %%
# Selecionando o cliente com o máximo de pontos
condicao = df_customers["Points"] == df_customers["Points"].max()
df_customers[condicao]

# %%
# Obtendo o nome do cliente com o máximo de pontos
condicao = df_customers["Points"] == df_customers["Points"].max()
df_maior = df_customers[condicao]
df_maior["Name"].iloc[0]

# %%
# Selecionando clientes com pontos entre 1000 e 2000
condicao = (df_customers["Points"] >= 1000) & (df_customers["Points"] <= 2000)
df_1000_2000 = df_customers[condicao].copy()

# %%
# Adicionando 1000 pontos aos clientes com pontos entre 1000 e 2000
df_1000_2000["Points"] = df_1000_2000["Points"] + 1000
df_1000_2000

# %%
# Exibindo o DataFrame original
df_customers

# %%
# Selecionando apenas as colunas "UUID" e "Name"
df_customers[["UUID", "Name"]]

# %%
# Ordenando as colunas alfabeticamente
colunas = df_customers.columns.tolist()
colunas.sort()

df_customers = df_customers[colunas]
df_customers

# %%
# Renomeando as colunas "Name" para "Nome" e "Points" para "Pontos"
df_customers = df_customers.rename(columns={"Name": "Nome", "Points": "Pontos"})
df_customers

# %%
# Renomeando a coluna "UUID" para "Id" usando inplace=True para modificar o DataFrame original
df_customers.rename(columns={"UUID": "Id"}, inplace=True)
df_customers
