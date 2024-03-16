# %%

import pandas as pd

# Carregando os dados dos clientes
df_customer = pd.read_csv("../data/customers.csv", sep=";")
df_customer

# %%

# Carregando os dados das transações
df_transactions = pd.read_excel("../data/transactions.xlsx")
df_transactions

# %%

# Carregando os dados dos produtos transacionados
df_transactions_product = pd.read_parquet("../data/transactions_cart.parquet")
df_transactions_product

# %%

# Realizando um merge entre os DataFrames df_transactions e df_customer com base nos IDs dos clientes
# Em seguida, realizando um merge com os dados dos produtos transacionados
df_join = (df_transactions.merge(df_customer,
                                how="inner",
                                left_on="IdCustomer",
                                right_on="UUID",
                                suffixes=["_transacao", "_cliente"])
                          .merge(df_transactions_product,
                                 how='inner',
                                 left_on="UUID_transacao",
                                 right_on="IdTransaction")
                                 )

df_join