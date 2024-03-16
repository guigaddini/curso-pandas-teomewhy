# %%
import pandas as pd

# Definindo o primeiro DataFrame
data_01 = {
    "id": [1,2,3,4],
    "nome":["Teo", "Mat", "Nah", "Mah"],
    "idade": [31,31,32,32]
}

df_01 = pd.DataFrame(data_01)
df_01

# %%

# Definindo o segundo DataFrame
data_02 = {
    "id": [5,6,7,8],
    "nome":["Jose", "Nathan", "Arnaldo", "Mario"],
    "idade": [23,33,19,21]
}

df_02 = pd.DataFrame(data_02)
df_02

# %%

# Concatenando os dois DataFrames verticalmente e resetando os índices
pd.concat([df_01, df_02]).reset_index(drop=True)

# %%

# Definindo o terceiro DataFrame
data_03 = {
    "sobrenome":["Calvo", "Silva", "Costa", "Souza"],
    "renda": [3100, 3100, 3200, 3200]
}
df_03 = pd.DataFrame(data_03).sort_values(['renda','sobrenome'], ascending=[False, True])

df_03
# %%

# Concatenando os DataFrames df_01 e df_03 horizontalmente
pd.concat([df_01, df_03], axis=1)