#instala a biblioteca requests
#importa a biblioteca 

import requests 

#solicita dados de entrada
cep = input('Digite o cep (Somente números):')

url = f'https://viacep.com.br/ws/{cep}/json/'

resposta = requests.get(url) #fazendo a requisicao

if resposta.status_code == 200: 
    dados = resposta.json()
    if 'erro'not in dados:
        print(f'CEP: {dados['cep']}')
        print(f'Logradouro:{dados['logradouro']}')
        print(f'Cidade:{dados['localidade']}')
        print(f'Estado:{dados['uf']}')
    else:
        print('CEP não localizado')
else:
    print(f'Erro na requisição: {resposta.status_code}')
    print(resposta.content)