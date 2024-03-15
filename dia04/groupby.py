# %%
import pandas as pd

# %%
# Carregando o arquivo de transações
df = pd.read_excel("../data/transactions.xlsx")
df

# %%
# Calculando a pontuação total de um usuário específico
condicao = df["IdCustomer"] == "5f8fcbe0-6014-43f8-8b83-38cf2f4887b3"
df_user = df[condicao]
pontuacao_total_usuario = df_user['Points'].sum()
pontuacao_total_usuario

# %%
# Calculando a pontuação total de cada usuário
pontos = {}
for i in df['IdCustomer'].unique():
    condicao = df["IdCustomer"] == i
    pontos[i] = df[condicao]["Points"].sum()

pontos

# %%
# Resumo da pontuação para cada cliente
df_summary = df.groupby(["IdCustomer"])["Points"].sum()
df_summary.reset_index()

# %%
# Resumo detalhado para cada cliente
df_summary_detalhado = (df.groupby(["IdCustomer"])
                        .agg({ "Points": 'sum',
                               "UUID": "count",
                               "DtTransaction": "max"})
                        .rename(columns={
                                "Points":"Valor",
                                "UUID": "Frequencia",
                                "DtTransaction":"UltimaData"
                                })
                        .reset_index())
df_summary_detalhado

# %%
# Calculando a recência das transações para cada cliente
import datetime

data1 = df["DtTransaction"][0]
agora = datetime.datetime.now()

dias_desde_ultima_transacao = (agora - data1).days
dias_desde_ultima_transacao

# %%
# Calculando a recência das transações usando uma função
def recencia(x):
    diff = datetime.datetime.now() - x.max()
    return diff.days

df_recencia = (df.groupby(["IdCustomer"])
               .agg({ "Points": 'sum',
                      "UUID": "count",
                      "DtTransaction": ['max', recencia]
                      })
                .rename(columns={
                        "Points":"Valor",
                        "UUID": "Frequencia",
                        "DtTransaction":"UltimaData"
                        })
               .reset_index())
df_recencia