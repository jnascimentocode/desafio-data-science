import pandas as pd
import os
from upload_dados import *
import seaborn as sns
import matplotlib.pyplot as plt
os.system('cls')

#3. Existem correlações entre as características de um anúncio e seu faturamento?
#   a. Quais? Explique

# filtrando todos os dados somente dos anuncios alugados
data_df = data_df.loc[data_df['booked_on'] != 'blank']

#agrupando todos os dados pela soma do faturamento
billings = data_df[['ad_name','number_of_bedrooms','number_of_bathrooms','star_rating','is_superhost','price_string','number_of_reviews']].groupby('ad_name').sum()
print(billings.sort_values(by='price_string', ascending=False))

# chamar a matriz de correlação para análise
print('----- Correlação dos dados -----')
print(billings.corr())
sns.heatmap(billings.corr(), annot=True, vmin=-1, vmax=1, cmap='coolwarm')
plt.show()
print('--------------------------------')
print('Podemos ver que o faturamento está correlacionado ao número de quartos e número de banheiros, \
        e podemos dizer que a nota do anuncio também tem uma certa relevância na análise.')
print('--------------------------------')

