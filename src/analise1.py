import pandas as pd
import os
from upload_dados import *
import plotly.express as px

os.system('cls')

#1. Ordene os bairros em ordem crescente de número de listings

print('----- Bairros x Número de anúncios -----')

#filtrando a quantidade de anuncios
data = data_df['suburb'].value_counts(ascending=True)
data = pd.DataFrame(data)
print(data)

#total de anuncios
print('----------------------------------------')
print(f'Total de anúncios: {data_df.shape[0]}')
print('----------------------------------------')

#grafico de barra referenciando os bairros x anuncios
chart = px.bar(data, text_auto=True, title='Bairros x Número de anúncios')
chart.show()