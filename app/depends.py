# esse arquivo serve pra gente definir injeção de dependência (passar dependência como parâmetro para função)

from fastapi import Depends
from app.db.connection import Session


def get_db_session():
    try:
        session = Session()
        yield session
    finally:
        session.close()


        


