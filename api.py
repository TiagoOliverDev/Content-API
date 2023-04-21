from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel

app = FastAPI() #Só com esse comando a api já está criada

dados = {
    1: {"Nome": "Tiago", "Email": "teste", "Senha": "teste", "Confirmar-senha": "teste"},
    2: {"Nome": "Tiago1", "Email": "teste", "Senha": "teste", "Confirmar-senha": "teste"},
    3: {"Nome": "Tiago2", "Email": "teste", "Senha": "teste", "Confirmar-senha": "teste"},
    4: {"Nome": "Tiago3", "Email": "teste", "Senha": "teste", "Confirmar-senha": "teste"},
}

class ItemForSale(BaseModel):
    name_item: str
    preco_unitario: float
    quantidade: int

@app.get("/") #@ = decorator
async def home():
    return {"cadastro": len(dados)}

@app.get("/cadastrados/{id_user}")
async def get_sale(id_user: int): # recebendo parâmetro e passando sua tipagem
    if id_user in dados:
         return dados[id_user]
    else:
        return {"Erro": "ID de user inexistente!"}

  
if __name__ == '__main__':
    uvicorn.run(app, host="localhost", port=8000)
