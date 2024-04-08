import os #importação para fazer a verificação se o header do arquivo e o proprio arquivo 'dados.csv' existem 
import requests #importação da biblioteca requests para fazer a requesição da URL
from bs4 import BeautifulSoup as bs #importação da biblioteca BeautifulSoup usada para fazer a manipulação HTML
import pandas as pd #importação da biblioteca pandas para manipulaçãi de dados

print("Web Scraping para Coleta de Preços de Produtos KABUM!!!")

while True:
    while True:
        try:
            url = input("Favor cole a URL inteira: ")
            response = requests.get(url)
            response.raise_for_status()  # Verifica se a requisição foi bem sucedida

            # Se chegou até aqui, a URL é válida, então saímos do loop
            break
        except requests.exceptions.RequestException as e:
            print("Erro ao fazer a requisição:", e)

    html = response.text
    soup = bs(html, 'html.parser')
    
    #Print da requisição e todo código html da página, usei só para saber se estava tudo certo com a requisição
    #print(response)
    #print(html)

    #Criação do objeto soup
    soup = bs(html, 'html.parser')

    #Procurando o título do produto
    titulo = soup.find('h1', {'class' : 'sc-58b2114e-6 brTtKt'}).text
    print("Nome do Produto: "+titulo)

    #Procurando o elemento "Preço Normal"
    try:
        preço_normal = soup.find('b', {'class' : 'regularPrice'})
        for valor in preço_normal:
            print("valor normal: "+valor)
                
    except:
        print("Elemento não encontrado")

    #Procurando o elemento "Preço Final"
    try:
            preço_final = soup.find('h4',{'class' : 'sc-5492faee-2 ipHrwP finalPrice'})
            for valor in preço_final:
                print("Valor a vista: "+valor)
    except:
        print("Elemento não encontrado")
            
    #Criação das listas para armazenar os dados
    titulos = []
    preços_normais = []
    preços_finais = []

    # Adicionando os dados as listas
    titulos.append(titulo)
    preços_normais.append(preço_normal)
    preços_finais.append(preço_final)

    # Criando o DataFrame com as listas
    df = pd.DataFrame()
    df['Nome'] = titulos
    df['Valor_normal'] = preços_normais
    df['Valor_a_vista'] = preços_finais

    # Importando o DataFrame para o arquivo 'dados.csv'
    df.to_csv('dados.csv', mode='a', header=not os.path.exists('dados.csv'), index=False)

    continuar = input("Deseja continuar adicionando dados? (S/N): ")
    if continuar.upper() != 'S':
        break