import requests

url = 'https://jsonplaceholder.typicode.com/posts/10'

response = requests.delete(url)

print("Status code:", response.status_code)
print("resposta da api: ", response.text) #retorno deve ser vzio // dicionario vario = {}
