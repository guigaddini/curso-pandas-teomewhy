# %%
import pandas as pd
import numpy as np

# Dados
data = {
    "nome": ["Téo", "Nah", "Lah", "Mah", "Jo"],
    "idade": [31, 32, 34, 12, np.nan],
    "renda": [np.nan, 3245, 357, 12432, np.nan],
}

# DataFrame
df = pd.DataFrame(data)
df

# %%
# Quantidade de valores NaN na coluna "idade"
df["idade"].isna().sum()

# %%
# Total de valores NaN em cada coluna
df.isna().sum()

# %%
# Proporção de valores NaN em cada coluna
df.isna().mean()

# %%
# Preenchimento dos valores NaN na coluna "idade" e "renda" com as médias dessas colunas
df_filled = df.fillna({
    "idade": df["idade"].mean(),
    "renda": df["renda"].mean(),
})
df_filled

# %%
# Remoção das linhas que contenham pelo menos um valor NaN nas colunas "idade" ou "renda"
df_dropped_rows = df.dropna(subset=["idade", "renda"], how='any')
df_dropped_rows

# %%
# Remoção das colunas que contenham menos de 3 valores não NaN
df_dropped_columns = df.dropna(axis=1, thresh=3)
df_dropped_columns