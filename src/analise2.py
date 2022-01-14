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
data_df = data_df.groupby('suburb').mean()
billings = data_df.sort_values(by='price_string', ascending=True)
billings = pd.DataFrame(billings)
print(billings)

chart = px.bar(billings, text_auto=True, title='Bairros x Faturamento médio R$ por listings')
chart.show()

print('------------------------------------------------------')