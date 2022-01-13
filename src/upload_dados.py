import pandas as pd

#lendo o arquivo .csv
table_priceav = pd.read_csv('data/desafio_priceav.csv')
table_details = pd.read_csv('data/desafio_details.csv')

#tratamento da tabela
table_priceav = table_priceav.drop(['Unnamed: 0', 'Unnamed: 0.1'], axis=1)
table_details = table_details.drop('Unnamed: 0', axis=1)

#unificando as tabelas
data_df = table_details.merge(table_priceav)

