import pandas as pd
import os
from upload_dados import *
import plotly.express as px
import numpy as np

os.system('cls')

#4. Qual a antecedência média das reservas?

# filtrando todos os dados dos anuncios alugados
data_df = data_df.loc[data_df['booked_on'] != 'blank']
data_df = pd.DataFrame(data_df)

#convertendo os dados para o tipo data
data_df['date'] = pd.to_datetime(data_df['date'])
data_df['booked_on'] = pd.to_datetime(data_df['booked_on'])

#adicionando a antecedencia de dias de cada reserva
data_df['days_to_book'] = (data_df['date'] - data_df['booked_on'])

#retornando a antecedencia média das reservas
antecedence = data_df['days_to_book'].mean()

print('-------------------------------------------------------')
print(f'Antecedência média das reservas: {antecedence.days} dias')
print('-------------------------------------------------------')

#4. Qual a antecedência média das reservas?
#   a. Esse número é maior ou menor para finais de semana?

#incluindo os dias da semana na tabela
data_df['day_of_booking'] = data_df['booked_on'].dt.day_name()

#filtrando os dados a ser analisados
comparisson = data_df[['day_of_booking','days_to_book']]

#retornando a antecedencia média por dia da semana
print('---Antecedência média das reservas por dia da semana---')
comparisson = comparisson.groupby(['day_of_booking']).mean()
comparisson = comparisson['days_to_book'].apply(lambda x: x / np.timedelta64(1,'D'))
comparisson = pd.DataFrame(comparisson)
print(comparisson.sort_values(by='day_of_booking', ascending=True))
print('-------------------------------------------------------')

#grafico em barras mostrando a antecedencia média das reservas por dia da semana
comparisson = pd.DataFrame(comparisson)
chart = px.bar(comparisson, text_auto=True, category_orders={"day_of_booking": ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']}, title='Antecedência média das reservas por dia da semana')
chart.show()

#a. Esse número é maior ou menor para finais de semana?

#função para separar as semanas do final de semana
def status(data):
    if data['day_of_booking'] == 'Saturday' or data['day_of_booking'] == 'Sunday':
        return 'weekend'
    return 'week'  

#inclusão do status 'week' ou 'weekend'
data_df['status'] = data_df.apply(status, axis=1)

# filtro por status
print('----Verificação da antecedencia média durante semana---')
status = data_df[['status','days_to_book']].groupby(['status']).mean()
status = status['days_to_book'].apply(lambda x: x / np.timedelta64(1,'D'))
status = pd.DataFrame(status)
print(status)
print('-------------------------------------------------------')

#grafico mostrando a média entre 'week' e 'weekend'
chart = px.pie(status, values='days_to_book', names=['Week','Weekend'],hole=.3, title='Verificação da antecedencia média durante semana', color_discrete_sequence=px.colors.sequential.RdBu)
chart.update_traces(textposition='inside', textinfo='percent+label', textfont_size=20)
chart.show()

