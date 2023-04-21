from fastapi import FastAPI
from app.routes import router

app = FastAPI()


@app.get('/')
def health_check():
    return "ok, endpoint /"

app.include_router(router)

#rodando api: uvicorn app.main:app