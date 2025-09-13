# métood get

import requests

url = 'https://jsonplaceholder.typicode.com/posts/5'
response = requests.get(url)

print("Status:", response.status_code)
print("Título do post:" ,response.json()['title'])
