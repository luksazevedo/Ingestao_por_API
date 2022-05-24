"""
Ingestão e Análise de Dados via API.ipynb

"""

import requests
import json
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#Requisição dos Dados
url = 'https://dadosabertos.camara.leg.br/api/v2/deputados'
parametros = {}
resposta = requests.request( "GET", url, params = parametros )
objetos = json.loads(resposta.text)
dados_parametros = objetos['dados']

# Estruturação dos Dados obtidos via API
df = pd.DataFrame(dados_parametros)

# Analise dos Dados obtidos via API
x = df['siglaPartido'].value_counts().head(5).values # seleciona os 5 maiores
y = df['siglaPartido'].value_counts().head(5).index  
plt.figure(figsize = (15,5)) #dimensiona o tamanho do gráfico
sns.barplot(x = x, y = y, palette = 'deep')
plt.title('5 Maiores Partidos', 
          fontdict = {'color' : 'black',
                     'weight': 'bold',
                     'size': 24}
                      )
plt.xlabel('Quantidade de Deputados', size = 18,)
plt.ylabel('Partido', size = 18)
plt.plot()

# Analise dos Dados sobre partidos obtidos via API
x = df['siglaPartido'].value_counts().tail(5).values # seleciona os 5 menores
y = df['siglaPartido'].value_counts().tail(5).index  
plt.figure(figsize = (15,5)) #dimensiona o tamanho do gráfico
sns.barplot(x = x, y = y, palette = 'deep')
plt.title('5 Menores Partidos', 
          fontdict = {'color' : 'black',
                     'weight': 'bold',
                     'size': 24}
                      )
plt.xlabel('Quantidade de Deputados', size = 18,)
plt.ylabel('Partido', size = 18)
plt.plot()

# Analise de Dados por Estado
x = df['siglaUf'].value_counts().head(3).values # seleciona os 3 maiores
y = df['siglaUf'].value_counts().head(3).index  
plt.figure(figsize = (15,3)) #dimensiona o tamanho do gráfico
sns.barplot(x = x, y = y, palette = 'deep')
plt.title('Estados com mais deputados', #define o titulo , cor e tamanho
          fontdict = {'color' : 'black',
                     'weight': 'bold',
                     'size': 24}
                      )
plt.xlabel('Quantidade de Deputados', size = 18,) # gráfico eixo x
plt.ylabel('Estado', size = 18) #gráfico eixo y
plt.plot()