from models import Leitor, Livro, Emprestimo
from fastapi import FastAPI, HTTPException
from typing import List
from datetime import date,timedelta
import uuid

app = FastAPI()

livros:List[Livro] = []
leitores:List[Leitor] = []
emprestimos:List[Emprestimo] = []



@app.post('/livro', response_model=Livro)
def cadastra_livro(livro_cadastra:Livro):

    livro_cadastra.uuid = str(uuid.uuid4())
    livros.append(livro_cadastra)
    livros.append(livro_cadastra)

    return livro_cadastra
    
@app.get('/livros', response_model=List[Livro])
def lista_livros():
    return livros

@app.get('/livros/{titulo}', response_model=List[Livro])
def lista_livros(titulo:str):
    for livro in livros:
        if livro.titulo == titulo:
            return livro
    return HTTPException(404, "Livro não Encontrado")

@app.post('/leitores', response_model = Leitor)
def cadastrar_leitor(leitor:Leitor):
    leitor.uuid = str(uuid.uuid4())
    leitores.append(leitor)
    return leitor

@app.get('/emprestimo', response_model=Emprestimo)
def emprestimo(leitor:str,livro:str, data_emprestimo:date, data_devolucao:date):
    user = None
    book = None
    for u in leitores:
        if u.uuid == leitor:
            user = u
    for l in livros:
        if l.uuid == livro:
            if l.disponivel:
                book = l

    if book and user:
        book.disponivel == False
        dados = {
            "leitor":user,
            "livro":book,
            "data_emp":data_emprestimo,
            "data_dev":data_devolucao
        }

        emprestimo = Emprestimo(**dados)
        emprestimos.append(emprestimo)

        return emprestimo
    
    raise HTTPException(404, "Empréstimo não Realizado")









    







    

