#%%

# Importando a biblioteca pandas
import pandas as pd  # pd é um alias de pandas

# Lista de idades
idades = [30, 42, 90, 34]
idades

#%%

# Calculando a média das idades
media = sum(idades) / len(idades)

# Calculando a variância das idades (ou seja, desvio padrão: o quanto um conjunto de dados difere da média)
total = 0
for i in idades:
    total += (media - i) ** 2
variancia = total / (len(idades) - 1)  # O desvio padrão é calculado pela raiz quadrada da média dos quadrados das diferenças entre cada valor e a média.

#%%

# Transformação da lista em uma série do Pandas
series_idades = pd.Series(idades)  # Convertendo a lista "idades" para uma "série"

#%%

# Explicação da diferença entre listas e séries:
# LISTAS são estruturas de dados básicas em Python que podem armazenar uma coleção ordenada de itens.
# SÉRIES são uma estrutura de dados mais avançada fornecida pela biblioteca Pandas que são especialmente úteis para trabalhar com dados tabulares.
# Enquanto listas são mais genéricas e podem conter qualquer tipo de dado, séries são otimizadas para dados homogêneos (todos do mesmo tipo), como números.
# Além disso, as séries Pandas oferecem muitas funcionalidades estatísticas e de manipulação de dados que não estão disponíveis diretamente para listas em Python nativo.

#%%

# Métodos da série pandas
# Média
series_idades.mean()

#%%

# Variância
series_idades.var()

#%%

# Desvio padrão
series_idades.std()

#%%

# Mediana
series_idades.median()

#%%

# 3o Quartil
series_idades.quantile(0.75)

#%%

# Sumarização estatística da série
series_idades.describe()

#%%

# Dimensão da série
series_idades.shape

#%%

# Acessando o primeiro elemento da lista
idades[0]

#%%

# Acessando o quarto elemento da série
series_idades[3]  # Esse número final é o ÍNDICE da série, ou seja, a posição do item na série

#%%

# Alterando os índices da série
series_idades.index = ['t', 'e', 'o', 'c']

#%%

# Acessando um elemento da série com o novo índice 't'
series_idades['t']

#%%

# Alterando os índices para números
series_idades.index = [40, 10, 30, 20]

#%%

# Exibindo a série com os novos índices
series_idades

#%%

# Exibindo novamente a série
series_idades

#%%

# Exibindo um intervalo de elementos da série
series_idades.iloc[2:4]

#%%

# Exibindo outro intervalo de elementos da série
series_idades.iloc[0:2]

#%%

# Acessando um elemento específico da série pelo índice
series_idades.loc[40]

#%%

# Nomeando a série
series_idades.name = 'idades'

#%%

# Exibindo a série com o novo nome
series_idades

#%%

# Criando uma série com nome ao criá-la
series_idades = pd.Series(idades, name="idades")

#%%

# Exibindo a série com nome
series_idades
