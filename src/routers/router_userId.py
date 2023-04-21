from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel, validator

app = FastAPI() #Só com esse comando a api já está criada

dados = {
    1: {"Username": "Tiago", "Email": "teste", "Password": "teste", "ConfirmPassword": "teste"},
    2: {"Username": "Tiago1", "Email": "teste", "Password": "teste", "ConfirmPassword": "teste"},
    3: {"Username": "Tiago2", "Email": "teste", "Password": "teste", "ConfirmPassword": "teste"},
    4: {"Username": "Tiago3", "Email": "teste", "Password": "teste", "ConfirmPassword": "teste"},
}


@app.get("/cadastrados/{id_user}")
async def get_sale(id_user: int): # recebendo parâmetro e passando sua tipagem
    if id_user in dados:
         return dados[id_user]
    else:
        return {"Erro": "ID de user inexistente!"}



if __name__ == '__main__':
    uvicorn.run(app, host="localhost", port=8000)