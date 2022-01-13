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
print(f'Antecedência média das reservas:{antecedence.days} dias')
print('-------------------------------------------------------')

#4. Qual a antecedência média das reservas?
#   a. Esse número é maior ou menor para finais de semana?

#incluindo os dias da semana na tabela
data_df['day_of_booking'] = data_df['booked_on'].dt.day_name()
data_df['day_of_date'] = data_df['date'].dt.day_name()

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
chart = px.bar(comparisson, title='Antecedência média das reservas por dia da semana')
chart.show()

#a. Esse número é maior ou menor para finais de semana?

#dado a ser trabalhado
new_data = data_df[['days_to_book','day_of_booking']]
new_data = pd.DataFrame(new_data)

#função para separar as semanas do final de semana
def status(data):
    if data['day_of_booking'] == 'Saturday' or data['day_of_booking'] == 'Sunday':
        return 'weekend'
    return 'week'  

#inclusão do status 'week' ou 'weekend'
new_data['status'] = new_data.apply(status, axis=1)

#comparar se a antecedencia média é maior ou menos para finais de semana
print('------Verificação da antecedencia média durante semana-----')
verificacao = new_data[['status','days_to_book']].groupby(['status']).mean()
verificacao = verificacao['days_to_book'].apply(lambda x: x / np.timedelta64(1,'D'))
verificacao = pd.DataFrame(verificacao)
print(verificacao)
print('-------------------------------------------------------')

#grafico mostrando a Verificação da antecedencia média durante semana
chart = px.bar(verificacao, title='Verificação da antecedencia média durante semana')
chart.show()

print('É de costume os usuários reservarem as datas entre quarta, quinta e sextas-feiras com uma antecedencia média de 32 dias.\n'
    'Durante a semana, a média sobe para 35 dias, enquanto aos finais de semana temos uma média de 22 dias.')
