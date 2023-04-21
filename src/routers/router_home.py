from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Home():

    @staticmethod
    def get_data():
        dados = {
            1: {"Username": "Tiago", "Email": "teste", "Password": "teste", "ConfirmPassword": "teste"},
            2: {"Username": "Tiago1", "Email": "teste", "Password": "teste", "ConfirmPassword": "teste"},
            3: {"Username": "Tiago2", "Email": "teste", "Password": "teste", "ConfirmPassword": "teste"},
            4: {"Username": "Tiago3", "Email": "teste", "Password": "teste", "ConfirmPassword": "teste"},
        }

        return dados


    class Api(BaseModel):
        Username: str
        Email: str
        Password: str
        ConfirmPassword: str


    @app.get("/") 
    async def home():
        return {"cadastro": len(dados)}