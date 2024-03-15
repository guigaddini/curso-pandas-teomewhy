# %%
import pandas as pd

# Lendo o arquivo Excel e armazenando os dados em um DataFrame
df = pd.read_excel("../data/transactions.xlsx")

# %%
# Filtrando o DataFrame para obter o último registro de cada cliente
df_last = (df.sort_values("DtTransaction", ascending=False)
             .drop_duplicates(subset=['IdCustomer'], keep='first'))

# Contando o número de clientes únicos no DataFrame resultante
df_last['IdCustomer'].nunique()

# %%
# Definindo a condição de filtro para o cliente com ID '5f8fcbe0-6014-43f8-8b83-38cf2f4887b3'
condicao = df['IdCustomer'] == '5f8fcbe0-6014-43f8-8b83-38cf2f4887b3'

# Aplicando a condição para filtrar os dados do cliente especificado
df[condicao]

# %%
# Filtrando os dados do último registro do cliente com ID '5f8fcbe0-6014-43f8-8b83-38cf2f4887b3'
df_last[df_last['IdCustomer'] == '5f8fcbe0-6014-43f8-8b83-38cf2f4887b3']