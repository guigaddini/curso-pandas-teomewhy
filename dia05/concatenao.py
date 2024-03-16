# %%
import pandas as pd
import os

def import_etl(path:str):

    name = path.split("/")[-1].split(".")[0]

    # Importando o arquivo e ajustando o DataFrame
    df = (pd.read_csv(path, sep=';')
            .rename(columns={"valor":name})
            .set_index(["cod","nome","período"]))
    
    return df

# %%

# Diretório onde os arquivos estão localizados
path = "../data/ipea/"
files = os.listdir(path)

# Lista para armazenar os DataFrames de cada arquivo
dfs = []

# Iterando sobre cada arquivo no diretório
for i in files:
    # Chamando a função import_etl para cada arquivo e armazenando o DataFrame resultante na lista dfs
    dfs.append(import_etl(path+i))

# Concatenando os DataFrames da lista dfs ao longo do eixo das colunas
df_bia = pd.concat(dfs, axis=1).reset_index()

# Salvando o DataFrame consolidado em um arquivo CSV
df_bia.to_csv("../data/bia_consolidado.csv", sep=";", index=False)