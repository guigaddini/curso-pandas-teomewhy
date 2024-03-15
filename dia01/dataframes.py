# %%
# Importando a biblioteca pandas
import pandas as pd

# %%
# Criando um dicionário com os dados
data = {
    "nome": ["teo", "nah", "lara", "maria"],
    "sobrenome": ["calvo", "ataide", "calvo", "calvo"],
    "idade": [31, 32, 31, 2]
}

#%%
# Acessando a idade da primeira pessoa na lista
data["idade"][0]

# %%
# Criando um DataFrame a partir do dicionário de dados
df = pd.DataFrame(data)
df

#%%
# Acessando a idade da primeira pessoa no DataFrame
df["idade"].iloc[0]

# %%
# Acessando o sobrenome da primeira pessoa no DataFrame
df['sobrenome'].iloc[0]

# %%
# Acessando todos os dados da primeira pessoa no DataFrame
df.iloc[0]

# %%
# Acessando a coluna de idades no DataFrame
df['idade']

# %%
# Alterando os índices do DataFrame
df.index = [3, 2, 1, 0]
df

# %%
# Acessando a idade da primeira pessoa no DataFrame após alteração dos índices
df["idade"][0]

# %%
# Acessando os índices do DataFrame
df.index

# %%
# Acessando os nomes das colunas do DataFrame
df.columns

# %%
# Obtendo informações sobre o DataFrame, incluindo uso de memória
df.info(memory_usage='deep')

# %%
# Obtendo os tipos de dados de cada coluna no DataFrame
df.dtypes

# %%
# Adicionando uma coluna "peso" ao DataFrame
df['peso'] = [80, 53, 65, 14]

# %%
# Calculando a média dos pesos no DataFrame
sumario = df.describe()
media_peso = sumario['peso']['mean']

# %%
# Exibindo as duas primeiras linhas do DataFrame
df.head(2)

# %%
# Exibindo as duas últimas linhas do DataFrame
df.tail(2)
# %%
