import pandas as pd
import os
from upload_dados import *
import plotly.express as px

os.system('cls')

#2. Ordene os bairros em ordem crescente de faturamento médio dos listings

print('----- Bairros x Faturamento médio R$ por listings-----')

#simplificando a tabela
data_df = data_df[['suburb','price_string','booked_on']]

# filtrando todos os dados dos anuncios alugados
data_df = data_df.loc[data_df['booked_on'] != 'blank']

#recebendo o faturamento médio dos anuncios alugados 
billing = data_df[['suburb', 'price_string']].groupby('suburb').mean()

#imprimindo o resultado em ordem crescente de faturamento médio
print(billing.sort_values(by='price_string', ascending=True))

print('------------------------------------------------------')

#histograma referenciando os bairros x faturamento total
chart = px.histogram(data_df, 'suburb', 'price_string', title='Faturamento total por bairro')
chart.show()

#barra referenciando os bairros x faturamento médio
billing = pd.DataFrame(billing)
chart = px.bar(billing, title='Faturamento médio R$ por bairro')
chart.show()

