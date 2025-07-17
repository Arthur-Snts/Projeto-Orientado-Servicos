from fastapi import FastAPI, Depends
from sqlmodel import SQLModel, Session, create_engine, select
from typing import Annotated, List
from contextlib import asynccontextmanager
from models import Pedido

url = "sqlite:///banco.db"
engine = create_engine(url)

def get_session():
    with Session(engine) as session:
        yield session


def create_db():
    SQLModel.metadata.create_all(engine)

SessionDep = Annotated[Session, Depends(get_session)]
@asynccontextmanager
async def lifespan(app:FastAPI):
    create_db()
    yield

app = FastAPI(lifespan=lifespan)

@app.get("/pedidos")
def pedidos(session:SessionDep)-> list[Pedido]:
    pedidos = session.exec(select(Pedido).limit(100)).all()
    return pedidos

@app.get('/pedidos/{id}')
def pedido_id(session:SessionDep, id:int)-> Pedido:
    pedido = session.exec(select(Pedido).where(Pedido.IdPedido==id)).one()
    return pedido
