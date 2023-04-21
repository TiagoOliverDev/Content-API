from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel, validator

app = FastAPI() #Só com esse comando a api já está criada

dados = {
    1: {"Name": "Tiago", "Email": "teste", "Password": "teste", "ConfirmPassword": "teste"},
    2: {"Name": "Tiago1", "Email": "teste", "Password": "teste", "ConfirmPassword": "teste"},
    3: {"Name": "Tiago2", "Email": "teste", "Password": "teste", "ConfirmPassword": "teste"},
    4: {"Name": "Tiago3", "Email": "teste", "Password": "teste", "ConfirmPassword": "teste"},
}

@app.put("/update_user/{id_user}")
    
class UserUpdate(BaseModel):
    Username: str
    Email: str
    Password: str
    ConfirmPassword: str

    @validator('ConfirmPassword') # Function para verificar senha e confirmar senha
    def passwords_match(cls, v, values):
        if 'Password' in values and v != values['Password']:
            raise ValueError('ConfirmPassword não confere com o Password')
        return v

async def update_user(user: UserUpdate):
    user_dict = user.dict()
    user_id = max(dados.keys()) + 1
    dados[user_id] = user_dict
    return {"id_user": user_id}




if __name__ == '__main__':
    uvicorn.run(app, host="localhost", port=8000)