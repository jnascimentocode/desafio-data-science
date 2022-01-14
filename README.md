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

![analise1](https://user-images.githubusercontent.com/95966908/149427680-38aa0f1b-c0fe-4b93-9da5-0027ba2bcf49.PNG)

![suburb x listings](https://user-images.githubusercontent.com/95966908/149561809-f9eb7858-cf5c-48f3-8571-1707d88e03f1.png)

* O bairro com o maior Listing é o **Ingleses** com **176.864 listings**.

### 2. Ordene os bairros em ordem crescente de faturamento médio dos listings
 
![analise2](https://user-images.githubusercontent.com/95966908/149428619-7f832d46-e57f-40ad-9685-db0098cc0ac4.PNG)

![suburb x billings](https://user-images.githubusercontent.com/95966908/149561888-fd3c4009-d695-4d4b-8e6f-a68ed4d0d2cc.png)
 
 * O bairro com o maior faturamento médio é **Jurerê** com a média de **R$414.32** por listing.
 
### 3. Existem correlações entre as características de um anúncio e seu faturamento? Quais? Explique

![analise3](https://user-images.githubusercontent.com/95966908/149410427-e32d7afe-edc4-42c6-8a41-c521923153d5.png)

 * No grafico de correlação, podemos ver que o faturamento está correlacionado ao **número de quartos e número de banheiros**, e podemos dizer que a **nota do anuncio** também tem uma certa relevância na análise.   
 
### 4. Qual a antecedência média das reservas? Esse número é maior ou menor para finais de semana?

![analise41](https://user-images.githubusercontent.com/95966908/149565314-823a7a79-56d6-4372-8cf5-098190f358a1.PNG)

![mean week book per days](https://user-images.githubusercontent.com/95966908/149561949-010a0c85-b528-473d-9f75-f1ed3a1963be.png)

![analise4a](https://user-images.githubusercontent.com/95966908/149565335-a4f942dc-d00f-432b-aab0-6cd040bc7706.PNG)

![mean week and weekend](https://user-images.githubusercontent.com/95966908/149565962-d2657c18-a0dd-4377-a471-021526e7c3d3.png)

 * É recorrente os usuários reservarem os quartos entre quarta, quinta e sexta-feira com uma **antecedencia média total de 32 dias** (61,2% de reservas antecedentes durante a semana, 38,8% de reservas antecedentes aos finais de semana) para a data da locação. Durante a semana, a média sobe para **35 dias**, enquanto aos finais de semana temos uma **média de 22 dias** para a data da locação.
