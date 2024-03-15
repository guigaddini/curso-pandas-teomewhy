# Converta o seguinte dicionário para DataFrame e obtenha:
# Sumário de cada coluna
# Média da coluna idade
# Último nome da coluna nome

# %%
# Importando a biblioteca pandas
import pandas as pd

# Definindo o dicionário de dados
dados = {"nome": ["Téo", "Nah", "Napoleão"], "idade": [31, 32, 14]}

# Convertendo o dicionário em um DataFrame do Pandas
df = pd.DataFrame(dados)
df

# %%
# Obtendo o sumário estatístico das colunas numéricas do DataFrame
sumario_numericas = df.describe()
sumario_numericas

# %%
# Calculando a média da coluna "idade"
media_idade = df["idade"].mean()
media_idade

# %%
# Obtendo o último nome da coluna "nome"
ultimo_nome = df["nome"].iloc[-1]
ultimo_nome

# %%
# Obtendo o último nome da coluna "nome" de outra forma
ultimo_nome_alternativo = df["nome"].tail(1)
ultimo_nome_alternativo
