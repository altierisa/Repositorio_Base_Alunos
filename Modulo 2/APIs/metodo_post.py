#metodo post cria 

import requests 

url = 'https://jsonplaceholder.typicode.com/posts'

novo_post = { 
    "title":"Meu primeiro POST",
    "body":"Estou aprendendo a enviar dados com Python",
    "userId": 10
}
#criando a requisicao
response = requests.post(url, json=novo_post)
print("Status code: ", response.status_code)
print("Resposta da API:", response.json())
