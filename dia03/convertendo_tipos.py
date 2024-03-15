# %%
import pandas as pd

# %%
# Lendo o arquivo CSV e armazenando os dados em um DataFrame
df = pd.read_csv("../data/customers.csv", sep=";")
df

# %%
# Exibindo os tipos de dados de cada coluna
df.dtypes

# %%
# Criando uma nova coluna "Points_dobble" que é o dobro da coluna "Points"
df["Points_dobble"] = df["Points"] * 2

# %%
# Convertendo as colunas "Points" e "Points_dobble" para o tipo de dados float
df[["Points", "Points_dobble"]] = df[["Points", "Points_dobble"]].astype(float)

# %%
# Tentando converter as colunas "UUID" e "Name" para o tipo de dados int, o que não é possível
df[["UUID", "Name"]].astype(int)

# %%
# Criando uma nova coluna "Lista" contendo listas com os valores [1, 2] para cada linha
df["Lista"] = [[1, 2] for i in df.index]
df

# %%
# Exibindo os tipos de dados de cada coluna após as operações
df.dtypes