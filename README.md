# desafio-data-science
 
 ## Seazone Code Challenge - Data Science
 O desafio consiste em analisar os dados de ocupação e preço de anúncios no
 Airbnb, a fim de responder uma série de perguntas.

 ## Dados:
  ### desafio_priceav.csv - Contém dados de ocupação e preço de anúncios
  * listing_id: Identificador de um anúncio
  * price_string: Preço ofertado
  * available: Booleano de ocupação. 1 significa livre e 0 ocupado.
  * date: Data a ser alugada
  * booked_on: Data quando “date” foi alugado. Null caso ainda esteja available.
  ### desafio_details.csv - Contém características de cada anúncio
  * listing_id: Identificador de um anúncio
  * location: Bairro do listing
  * Star rating: Nota 1-5 do anúncio
  * Superhost: Booleano que indica se é superhost ou não
  * quartos: Quantidade de quartos do anúncio
  * comentários:Quantidade de comentários do anúncio
  * Título: Título do anúncio
  * banheiros: Número de banheiros do anúncio

 ## Com base nessas informações:
 1. Ordene os bairros em ordem crescente de número de listings
 2. Ordene os bairros em ordem crescente de faturamento médio dos listings
 3. Existem correlações entre as características de um anúncio e seu faturamento?
 a. Quais? Explique
 4. Qual a antecedência média das reservas?
 a. Esse número é maior ou menor para finais de semana?
 Onde possível, embase sua análise com gráficos.

# Início do projeto

### Linguagem
* Python versão 3.10.0

### IDE
* VsCode
### Bibliotecas utilizadas 
* matplotlib==3.5.1
* numpy==1.21.4
* pandas==1.3.5
* plotly==5.5.0
* seaborn==0.11.2
- Obs: Ao final do projeto, foi criado um arquivo 'requirements.txt' para instalação de todos os pacotes

# Soluções

### 1- Ordene os bairros em ordem crescente de número de listings

![analise1](https://user-images.githubusercontent.com/95966908/149409704-20130a99-5b0b-4339-97fa-70eada84a568.PNG)

* O bairro com o maior Listing é o **Ingleses** com **176.864 listings**.

### 2. Ordene os bairros em ordem crescente de faturamento médio dos listings
 
![analise2](https://user-images.githubusercontent.com/95966908/149410367-11ea9c12-398a-4fdc-a3fb-c4f1499977b7.PNG)
 
 * O bairro com o maior faturamento médio é **Jurerê** com a média de **R$414.32** por listing.
 
### 3. Existem correlações entre as características de um anúncio e seu faturamento? Quais? Explique

![analise3](https://user-images.githubusercontent.com/95966908/149410427-e32d7afe-edc4-42c6-8a41-c521923153d5.png)

 * No grafico de correlação, podemos ver que o faturamento está correlacionado ao **número de quartos e número de banheiros**, e podemos dizer que a **nota do anuncio** também tem uma certa relevância na análise.  
 
 
### 4. Qual a antecedência média das reservas? Esse número é maior ou menor para finais de semana?

![analise4](https://user-images.githubusercontent.com/95966908/149410489-85cf506d-e45a-4ee3-ac6a-a7fcb92a5076.PNG)

 * É recorrente os usuários reservarem entre quarta, quinta e sexta-feira com uma **antecedencia média de 32 dias** para a data da locação. Durante a semana, a média sobe para **35 dias**, enquanto aos finais de semana temos uma **média de 22 dias** para a data da locação.
