from pydantic import BaseModel
from datetime import date, datetime
from typing import List

class Livro (BaseModel):
    id: int
    titulo: str
    ano: int
    disponivel: bool

class Leitor (BaseModel):
    id: int
    nome: str
    livros: List[Livro]

class Operacao (BaseModel):
    id: int
    tipo: str
    datatempo: datetime

class Emprestimo (BaseModel):
    id: int
    data_emp: date 
    data_dev: date
    livro: Livro
    leitor: Leitor

