import requests

url = 'https://jsonplaceholder.typicode.com/posts/7'

atualizacao = {
    "title":"Título atualizado no exercício"
}

#criando a requisicao
response = requests.patch(url, json=atualizacao)

print("Status Code:", response.status_code)
print("resposta da API:", response.json())