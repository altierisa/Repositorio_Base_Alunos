import requests 

print("Menu")
print("1- GET")
print("2-POST")
print("3-PATCH")
print("4-DELETE")

opcao = input("Escolha a ação(1-4): ")

if opcao == "1":
    post_id= input("Digite o ID do post: ")
    url= f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    r= requests.get(url)
    print("Resposta:", r.json())

elif opcao == "2":
   url= f"https://jsonplaceholder.typicode.com/posts"
   novo_post = { 
       "Title":input("Título:"),
       "body": input("Conteúdo: "),
       "userId":1
    }
   r = requests.post(url, json=novo_post)
   print("Post criado:", r.json())

elif opcao == "3":
    post_id = input("Digite o Id do post a ser atualizado:")
    novo_titulo = input("Novo Título: ")
    url= f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    r = requests.patch(url, json={"title":novo_titulo})
    print("Post atualizado: ", r.json())

elif opcao == "4":
    post_id= input("Digite o ID do post: ")
    url= f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    r = requests.delete(url)
    print("Status code:", r.status_code)

else:
    print("Opção inválida")