from pydantic import BaseModel
from datetime import date
from typing import List

class Livro (BaseModel):
    uuid: str
    titulo: str
    ano: str
    disponivel: bool

class Leitor (BaseModel):
    uuid: str
    nome: str
    livros: List[Livro]


class Emprestimo (BaseModel):
    data_emp: date 
    data_dev: date
    livro: Livro
    leitor: Leitor

