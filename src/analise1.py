import pandas as pd
import os
from upload_dados import *
import plotly.express as px

os.system('cls')

#1. Ordene os bairros em ordem crescente de número de listings

print('----- Bairros x Número de anúncios -----')
dados_asc = data_df['suburb'].value_counts()
print(dados_asc.sort_values(ascending=True))
print('----------------------------------------')
print(f'Total de anúncios: {data_df.shape[0]}')
print('----------------------------------------')

#histograma referenciando os bairros x anuncios
chart = px.histogram(data_df, x='suburb', title='Total de anúncios por bairro')
chart.show()