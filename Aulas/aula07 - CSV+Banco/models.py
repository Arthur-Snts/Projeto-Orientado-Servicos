from sqlmodel import SQLModel, Field

class Pedido(SQLModel, table=True):
    IdPedido:int = Field(primary_key=True)
    protocolo:str = Field(index=False)
    esfera:str = Field(index=False)
    uf:str = Field(index=False)

    