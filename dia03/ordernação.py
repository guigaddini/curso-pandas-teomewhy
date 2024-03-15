# %%
import pandas as pd

# %%
# Lendo o arquivo CSV e armazenando os dados em um DataFrame
df = pd.read_csv("../data/customers.csv", sep=';')
df

# %%
# Ordenando o DataFrame pelos valores das colunas "Points" e "Name" em ordem decrescente e ascendente, respectivamente
# Renomeando as colunas "Name" e "Points" para "Nome" e "Pontos", respectivamente
df = (df.sort_values(by=["Points", "Name"], ascending=[False, True])
        .rename(columns={"Name":"Nome", "Points":"Pontos"}))
df