# %%
# Importando a biblioteca pandas
import pandas as pd

# %%
# Lendo o arquivo CSV e armazenando os dados em um DataFrame
df = pd.read_csv("../data/products.csv",
                 sep=";",
                 names=["Id", "Name", "Description"]
                 )

df

# %%
# Renomeando as colunas "Name" para "Nome" e "Description" para "Descricao"
df = df.rename(columns={"Name":"Nome",
                        "Description":"Descricao"})

df
# %%
# Renomeando as colunas "Name" para "Nome" e "Description" para "Descricao" usando inplace=True
df.rename(columns={"Name": "Nome",
                   "Description": "Descricao"},
                   inplace=True)

df
