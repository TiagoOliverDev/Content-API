from sqlalchemy import Column, String, Integer
from app.db.base import Base


class UserModel(Base):
    __tablename__ = 'users'
    id = Column('id', Integer, primary_key=True, nullable=False, autoincrement=True)
    username = Column('username', String, nullable=False, unique=True)
    password = Column('password', String, nullable=False)
    


# iniciando migrations com: alembic init migrations
# fazendo migrations com: alembic revision --autogenerate -m "add users table"
# comando para aplicar o script em nosso db: alembic upgrade head
# rodar o comando para exportar a variável de ambiente: source .env