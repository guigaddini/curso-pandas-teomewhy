# %%
import pandas as pd

# Dados dos usuários
data_users = {
    "id": [1, 2, 3, 4],
    "nome": ["Teo", "Mat", "Nah", "Mah"],
    "idade": [31, 31, 32, 32]
}

# DataFrame dos usuários
df_user = pd.DataFrame(data_users)
df_user

# %%

# Dados das transações
data_transacoes = {
    "id_user": [1, 1, 1, 2, 3, 3, 5],
    "vl": [432, 532, 123, 6, 4, 87, 10],
    "qtProdutos": [2, 1, 3, 6, 10, 2, 7]
}

# DataFrame das transações
df_transacao = pd.DataFrame(data_transacoes)
df_transacao

# %%

# Junção das tabelas de usuários e transações usando LEFT JOIN
df_left_join = df_transacao.merge(df_user,
                                  how="left",
                                  left_on="id_user",
                                  right_on="id")
df_left_join

# %%

# Junção das tabelas de usuários e transações usando RIGHT JOIN
df_right_join = df_user.merge(df_transacao,
                               how="right",
                               left_on="id",
                               right_on="id_user")
df_right_join

# %%

# Junção das tabelas de usuários e transações usando INNER JOIN
df_inner_join = df_transacao.merge(df_user,
                                   how="inner",
                                   left_on="id_user",
                                   right_on="id")
df_inner_join

# %%

# Encontrando as linhas que não têm correspondência na junção (LEFT JOIN)
df_missing_users = df_left_join[df_left_join["nome"].isna()]
df_missing_users