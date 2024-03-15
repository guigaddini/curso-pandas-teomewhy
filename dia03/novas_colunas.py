# %%
# Importando as bibliotecas pandas e numpy
import pandas as pd
import numpy as np

# %%
# Lendo o arquivo CSV e armazenando os dados em um DataFrame
df = pd.read_csv("../data/customers.csv", sep=";")

# %%
# Criando uma nova coluna "Points_double" que é o dobro da coluna "Points"
df["Points_double"] = df["Points"] * 2
df

# %%
# Criando uma nova coluna "Points_ratio" que é a razão entre "Points_double" e "Points"
df["Points_ratio"] = df["Points_double"] / df["Points"]
df

# %%
# Criando uma nova coluna "Constante" preenchida com valores nulos
df["Constante"] = None
df

# %%
# Criando uma nova coluna "Points_log" que contém o logaritmo natural dos valores da coluna "Points"
df["Points_log"] = np.log(df["Points"])
df

# %%
# Aplicando a função np.log aos valores das colunas "Points", "Points_double" e "Points_ratio"
np.log(df[["Points","Points_double","Points_ratio"]])

# %%
# Convertendo os nomes na coluna "Name" para letras maiúsculas e armazenando-os na coluna "Nome_Alta"
nomes_alta = []
for i in df['Name']:
    nomes_alta.append(i.upper())
df["Nome_Alta"] = nomes_alta
df

# %%
# Convertendo os nomes na coluna "Name" para letras maiúsculas usando o método str.upper()
df["Name"].str.upper()

# %%
# Definindo a função get_first para retornar o primeiro nome em uma sequência separada por "_"
def get_first(nome:str):
    nome = nome.upper()
    return nome.split("_")[0]

# %%
# Criando uma nova coluna "Name_First" que contém apenas o primeiro nome da coluna "Name"
df["Name_First"] = df["Name"].apply(get_first)
df

# %%
# Usando uma função lambda para criar uma nova coluna "Name_First" que contém apenas o primeiro nome da coluna "Name"
df["Name"].apply(lambda x: x.upper().split("_")[0])

# %%
# Definindo a função intervalo_pontos para classificar os pontos em baixo, médio ou alto
def intervalo_pontos(pontos):
    if pontos < 2500:
        return "baixo"
    elif pontos < 3500:
        return "medio"
    else:
        return "alto"

# Criando uma nova coluna "Faixa_Pontos" que contém a classificação dos pontos em baixo, médio ou alto
df["Faixa_Pontos"] = df["Points"].apply(intervalo_pontos)
df

# %%
# Extraindo os últimos três caracteres da coluna "UUID" e armazenando-os na mesma coluna
df["UUID"].apply(lambda x: x[-3:])

# %%
# Criando um DataFrame "df_crm" com dados de clientes para aplicar a função RFV
data = {
    "nome": ["Teo", "Nah", "Maria", "Lara"],
    "recencia": [1,30,10,45],
    "valor":[100,2000, 15, 500],
    "frequencia":[2, 5, 1, 15]
}
df_crm = pd.DataFrame(data)

# Definindo a função RFV para atribuir uma pontuação com base na recência, valor e frequência
def rfv(row):
    nota = 0
    if row['recencia'] <= 10:
        nota += 10
    elif 10 < row['recencia'] <= 30:
        nota += 5
    elif row['recencia'] > 30:
        nota += 0

    if row['valor'] > 1000:
        nota += 10
    elif 100 <= row['valor'] < 1000:
        nota += 5
    elif row['valor'] < 100:
        nota += 0

    if row['frequencia'] > 10:
        nota += 10
    elif 5 <= row['frequencia'] < 10:
        nota += 5
    elif row['frequencia'] < 5:
        nota += 0
    return nota

# Criando uma nova coluna "RFV" com a pontuação RFV aplicada aos dados de clientes
df_crm["RFV"] = df_crm.apply(rfv, axis=1)
df_crm

# %%
# Exibindo os dados da primeira linha do DataFrame df_crm
df_crm.iloc[0]