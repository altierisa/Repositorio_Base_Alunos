#criar um codigo que consuma uma api de clima e informe a temperatuva e descricao do clima em lugar X

import requests
#definir chave api e o link da requisicao
cidade = input("Digite a Cidade: ").strip()
api_key = '2a1ac38a32354cb7b19133643251408'
url = f'https://api.weatherapi.com/v1/current.json'

#parametros da requisicao
parametros = {
    'key':api_key,
    'q':cidade,
    'lang':'pt'
}
#fazer a requisicao
resposta = requests.get(url, params=parametros)
#verificar se a req foi bem sucedida

if resposta.status_code == 200:
    dados = resposta.json()
    temperatura = dados['current']['temp_c']
    descricao = dados['current']['condition']['text']
    print(f'Temperatura Em {cidade} é {temperatura}')
    print(f'Descrição: {descricao}')
else:
    print(f'Erro na requisição: {resposta.status_code}')
    print(resposta.content)