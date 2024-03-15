# Converta a seguinte lista de dados para uma Series Pandas e obtenha:
# Média
# Desvio Padrão
# Máximo Valor

# %%
# Importando a biblioteca pandas
import pandas as pd

# Definindo a lista de dados
dados = [10, 20, 42, 9, 12, 35, 24, 10, 8, 14, 21]

# Convertendo a lista de dados em uma Series do Pandas
series = pd.Series(dados)
series

# %%
# Calculando a média dos dados na série
media = series.mean()
media

# %%
# Calculando o desvio padrão dos dados na série
desvio = series.std()
desvio

# %%
# Obtendo o valor máximo na série de dados
maximo = series.max()
maximo