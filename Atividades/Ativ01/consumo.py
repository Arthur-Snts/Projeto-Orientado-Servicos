import requests

URL = "http://127.0.0.1:8000"

def listar_livros():
    r = requests.get(f"{URL}/livros")
    if r.status_code == 200:
        print(r.text)

def listar_livro(titulo):
    r = requests.get(f"{URL}/livros/{titulo}")
    if r.status_code == 200:
        print(r.text)
    elif r.status_code == 404:
        print(r.text)

def cadatrar_livro():
    titulo = input("Digite o Título: ")
    ano = int(input("Digite o Ano: "))
    edicao = int(input("Digite a Edição: "))
    livro = {
        "titulo":titulo,
        "ano": ano,
        "edicao":edicao
    }
    r = requests.post(f"{URL}/livros", json=livro)
    if r.status_code == 200:
        print(r.text)
    elif r.status_code == 404:
        print(r.text)

def excluir_livro(titulo):
    r = requests.delete(f"{URL}/livros/{titulo}")
    if r.status_code == 200:
        print("Excluído com Sucesso")
    elif r.status_code == 404:
        print(r.text)

def atualizar_livro(titulo_velho):
    r = requests.get(f"{URL}/livros/{titulo_velho}")
    if r.status_code == 200:
        titulo = input("Digite o Título novo: ")
        ano = int(input("Digite o Ano novo: "))
        edicao = int(input("Digite a Edição nova: "))
        livro = {
            "titulo":titulo,
            "ano": ano,
            "edicao":edicao
        }
        r = requests.put(f"{URL}/livros/{titulo_velho}", json=livro)
        if r.status_code == 200:
            print("Atualizado com Sucesso")
        elif r.status_code == 404:
            print(r.text)
    else:
        print(r.text)

def menu(): 
    print("-=-" *15)
    print("1 - Listar Livros")
    print("2 - Listar Livros pelo Título")
    print("3 - Cadastrar Livro")
    print("4 - Deletar Livros")
    print("5 - Editar Livro")
    print("6 - Sair")
    print("-=-" *15)
    return int(input("Digite sua Ação: "))


opcao = menu()
while opcao !=6:
    print("-=-" *15)
    if opcao == 1:
        listar_livros()
    elif opcao == 2:
        titulo = input("Digite o título: ")
        listar_livro(titulo)
    elif opcao == 3:
        cadatrar_livro()
    elif opcao == 4:
        titulo = input("Digite o título: ")
        excluir_livro(titulo)
    elif opcao == 5:
        titulo = input("Digite o título do livro que queira Editar:")
        atualizar_livro(titulo)
    
    opcao = menu()