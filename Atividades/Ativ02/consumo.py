import requests

URL = "http://127.0.0.1:8000"

def listar_livro(id):
    r = requests.get(f"{URL}/livros/{id}")
    if r.status_code == 200:
        print(r.text)
    elif r.status_code == 404:
        print(r.text)



def menu(): 
    print("-=-" *15)
    print("1 - Listar Livro pelo id")
    print("-=-" *15)
    return int(input("Digite sua Ação: "))


opcao = menu()
while opcao !=6:
    print("-=-" *15)
    if opcao == 1:
        id =int(input("Digite o ID do Pedido"))
        listar_livro(id)
    
    
    opcao = menu()