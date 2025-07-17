from sqlmodel import SQLModel, Session, create_engine
from models import Pedido
import csv

url = "sqlite:///banco.db"

engine = create_engine(url)

def create_banco():
    SQLModel.metadata.create_all(engine)

def load_data():
    with open("pedidos.csv", "r", encoding="utf-8") as file:
        cfile = csv.DictReader(file, delimiter=";")
        for row in cfile:
            with Session(engine) as session:
                p = Pedido(
                    IdPedido= row["IdPedido"],
                    protocolo= row["ProtocoloPedido"],
                    esfera=row["Esfera"],
                    uf=row["UF"]
                )
                session.add(p)
                session.commit()

create_banco()
load_data()