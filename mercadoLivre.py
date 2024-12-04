import requests
from bs4 import BeautifulSoup

# obtendo produtos do Mercado livre

url_base = 'https://lista.mercadolivre.com.br/'
produto_Nome = input('Qual produto vc deseja: ')


response = requests.get(url_base + produto_Nome)
site = BeautifulSoup(response.text, 'html.parser')

produtos = site.findAll('div', attrs={
    'class': 'andes-card ui-search-result ui-search-result--mot andes-card--flat andes-card--padding-16 andes-card--animated'})


for produto in produtos:
    # TITULO
    titulo = produto.find('h2', attrs={'class': 'ui-search-item__title'})
    # Link
    link = produto.find('a', attrs={
        'class': 'ui-search-item__group__element ui-search-link__title-card ui-search-link'})
    # Preço
    preco = produto.find(
        'span', attrs={'class': 'andes-money-amount__fraction'})

    # print(produto.prettify())

    print('Titulo do produto: ', titulo.text)
    print('O link do Produto: ', link['href'])
    print('O preço do carro é : R$', preco.text)

    print('-' * 140)
