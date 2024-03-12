#%%
import pandas as pd #pd é um alias de pandas

# %%

idades = [30, 123, 35, 89]
idades

media = sum(idades) / len(idades)
media

# O desvio padrão é calculado pela raiz quadrada da média dos
# quadrados das diferenças entre cada valor e a média.

total = 0
for i in idades:
    total += (media -i)**2

variancia = total / (len(idades) -1)
variancia


# %%
# O python "nativo" não é mto apropriado pra se trabalhar com estatística.
# Para isso, vamos usar a biblioteca Pandas:

series_idades = pd.Series(idades) #convertendo a lista "idades" para uma "série"
series_idades
# %%

# Métodos
# variavel.metodo() -> método é um verbo, uma ação. EX: ligar o celular...

#metodo media:
series_idades.mean()

#metodo variancia/desvio padrao:
series_idades.var()
series_idades.std()

#metodo mediana()
series_idades.median()

# Qual é a diferença entre lista e séries?
# LISTAS são estruturas de dados básicas em Python que podem armazenar uma coleção ordenada de itens.
# SÉRIES são uma estrutura de dados mais avançada fornecida pela biblioteca Pandas que são especialmente úteis para trabalhar com dados tabulares.
# Enquanto listas são mais genéricas e podem conter qualquer tipo de dado, séries são otimizadas para dados homogêneos (todos do mesmo tipo), como números.
# Além disso, as séries Pandas oferecem muitas funcionalidades estatísticas e de manipulação de dados que não estão disponíveis diretamente para listas em Python nativo.

# %%

# O método describe() fornece um resumo estatístico das informações contidas na série.
# Ele calcula estatísticas como média, desvio padrão, mínimo, máximo e quartis.
# É útil para entender rapidamente a distribuição e as características dos dados na série.

series_idades.describe()
# %%

series_idades.shape

#%%
#Navegando na lista
idades[0]

#%%
#Navegando na série
series_idades[2] #esse numero final é o INDICE da serie, ou seja, a posição do item na serie
# %%

#Dá pra mudar o "nome" dos índices:
series_idades.index
#resultado: RangeIndex(start=0, stop=4, step=1)

#para alterar:
series_idades.index = ['t', 'e', 'o', 'c']

#Navegando nos índices novos:
series_idades['t']
series_idades[0] #ele tenta achar um indice, se nao achar, busca a posiçao

# %%

#dá inclusive pra alterar os índices pra numeros
series_idades.index = [40, 10, 30, 20]

#E os valores continuam os mesmos:
series_idades
#resultados:
#40     30
#10    123
#30     35
#20     89
#dtype: int64

#%%
#Se vc nao está interessado no índice, apenas na posição:
series_idades.iloc[1]
#%%
series_idades.iloc[-1]
#%%
series_idades.iloc[0:2]
# %%

# Pelo contrário, para garantir que é pelo índice, usar: 
series_idades.loc[40]


# %%
# Para criar um nome para a série:
series_idades.name = 'idades'
series_idades
# %%
# Dá pra dar um nome assim que cria a serie tb:
series_idades = pd.Series(idades, name = 'idades')
series_idades
# %%
