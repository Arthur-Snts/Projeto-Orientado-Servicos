from models import Leitor, Livro, Emprestimo, Operacao
from fastapi import FastAPI, HTTPException
from typing import List
from datetime import date,timedelta

app = FastAPI()

livros:List[Livro] = []
leitores:List[Leitor] = []
emprestimos:List[Emprestimo] = []
operacoes:List[Operacao] = []



@app.post('/livro')
def cadastra_livro(livro_cadastra:Livro):
    
    for livro in livros:
        if livro.id == livro_cadastra.id:
            raise HTTPException(status_code=404, detail="ID do Livro já existe")
    livros.append(livro_cadastra)
    

@app.get('/livros', response_model=List[Livro])
def lista_livros():
    livros_mostrar = livros
    for livro in livros:
        if livro.disponivel == False:
            livros_mostrar.pop(livro)
    return livros

@app.get('/livro', response_model=Livro)
def lista_livro(titulo:str):
    for livro in livros:
        if livro.titulo == titulo and livro.disponivel == True:
            return livro
    raise HTTPException(status_code=404, detail="Livro não Existe ou não disponível")


@app.post('/leitor')
def cadastra_leitor(leitor_cadastra:Leitor):
    for leitor in leitores:
        if leitor.id == leitor_cadastra.id:
            raise HTTPException(status_code=404, detail="ID do Leitor já existe")
    leitores.append(leitor_cadastra)

@app.post('/emprestimo')
def cadastra_emprestimo(livro_id:int, leitor_id:int):
    livro = None
    for livro_corrido in livros:
        if livro_corrido.id == livro_id and livro_corrido.disponivel == True:
            livro = livro_corrido
    if livro == None:
       raise HTTPException(status_code=404, detail="Livro não Existe")    
    
    leitor = None
    for leitor_corrido in leitores:
        if leitor_corrido.id == leitor_id:
            leitor = leitor_corrido
    if leitor == None:
       raise HTTPException(status_code=404, detail="Usuário não Existe")     
    setedias = timedelta(days=7)
    data_emp = date.today()
    data_dev = date.today() + setedias
    id = len(emprestimos)+1
    emprestimo = Emprestimo(livro=livro, leitor=leitor,data_dev=data_dev, data_emp=data_emp, id=id)
    emprestimos.append(emprestimo)
    livro.disponivel = False
    leitor.livros.append(livro)

@app.put('/livro')
def atualiza_livro(livro_id:int, leitor_id:int):
    livro = None
    for livro_corrido in livros:
        if livro_corrido.id == livro_id:
            livro = livro_corrido
    if livro == None:
       raise HTTPException(status_code=404, detail="Livro não Existe")    
    
    leitor = None
    for leitor_corrido in leitores:
        if leitor_corrido.id == leitor_id:
            leitor = leitor_corrido
    if leitor == None:
       raise HTTPException(status_code=404, detail="Usuário não Existe")
    
    for livro_alteracao in livros:
        if livro_alteracao.id == livro:
            livro_alteracao.disponivel = True

@app.get('/leitor', response_model=List[Livro])
def lista_livro_usuario(leitor_id:int):
    for leitor in leitores:
        if leitor.id == leitor_id:
            return leitor.livros
    raise HTTPException(status_code=404, detail="Leitor não Existe")
    







    

