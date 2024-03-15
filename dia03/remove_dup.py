# %%
import pandas as pd

# %%
# Definindo os dados como um dicionário
data = {
    "Nome": ["Téo", "Nah", "Maria", "Nah", "Lara", "Téo"],
    "Idade": [32, 33, 2, 33, 31, 32],
    "updated_at": [1, 2, 3, 1, 2, 3]
}

# %%
# Criando um DataFrame a partir dos dados
df = pd.DataFrame(data)

# Ordenando o DataFrame pelos valores da coluna "updated_at" em ordem decrescente
# Mantendo apenas as linhas únicas com base nas colunas "Nome" e "Idade", mantendo a primeira ocorrência
df = (df.sort_values(by="updated_at", ascending=False)
        .drop_duplicates(subset=["Nome", "Idade"], keep='first'))

df
# %%