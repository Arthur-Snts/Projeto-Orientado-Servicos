from typing import List, Annotated
from sqlmodel import Session, create_engine, SQLModel, select
from fastapi import FastAPI, Depends
from models import Aluno
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware

urlsqlite = "sqlite:///banco.db"

#Mysql - pymysql
urlmysql = "mysql+pymysql://usuario:senha@localhost/banco"

connect_args = {"check_same_thread": False}
engine = create_engine(urlsqlite, connect_args=connect_args)

def get_session():
    with Session(engine) as session:
        yield session # Yield é usado para ficar retornando session igual a anterior, porém se não exitir, é criada outras

SessionDep = Annotated[Session, Depends(get_session)] #Variável usada para criar uma anotação de Alias e ficar recuperando o valor aberto


def get_create_db():
    SQLModel.metadata.create_all(engine) #Criação das tabelas baseados na Classe

@asynccontextmanager 
async def lifespan(app:FastAPI): #Async usado para não ser executado antes da criação da Aplicação, somente no meio dela
    get_create_db()
    yield


app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # ou ["*"] para liberar geral (menos seguro)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/alunos')
def alunos(session:SessionDep) -> List[Aluno]:
    alunos = session.exec(select(Aluno)).all()
    return alunos

@app.post('/alunos')
def cadastrar(session:SessionDep, aluno:Aluno)-> Aluno:
    session.add(aluno)
    session.commit()
    session.refresh(aluno)
    return aluno

@app.delete("/alunos/{id}")
def deletar(session:SessionDep, id:int)->str:
    consulta = select(Aluno).where(Aluno.id==id)
    aluno = session.exec(consulta).one()
    session.delete(aluno)
    session.commit()
    return "Aluno foi de babau"

@app.put("/alunos/{id}")
def atualizar(session:SessionDep, id:int, nome:str) -> Aluno:
    consulta = select(Aluno).where(Aluno.id==id)
    aluno = session.exec(consulta).one()
    aluno.nome = nome
    session.add(aluno)
    session.commit()
    session.refresh(aluno)
    return aluno