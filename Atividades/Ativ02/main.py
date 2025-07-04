from fastapi import FastAPI, HTTPException
import pandas as pd

app = FastAPI()

@app.get("/pedidos/{id}")
def lista_pedido(id: str):
    df = pd.read_csv("20250702_Pedidos_csv_2025.csv", encoding="utf-8", sep=";")

    df["IdPedido"] = df["IdPedido"].astype(str).str.strip()
    id = id.strip()

    dados = df[df["IdPedido"] == id]

    if not dados.empty:
        return dados.to_dict(orient="records")[0]
    else:
        raise HTTPException(status_code=404, detail="Pedido não localizado")