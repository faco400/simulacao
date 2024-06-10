from sqlalchemy import Column, Integer, String, DateTime, LargeBinary

import datetime

from db.database import Base


class User(Base):
    __tablename__ = 'usuarios'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome: str = Column(String(100), nullable=False)
    email: str = Column(String(100), nullable=False, unique=True)
    senha: str = Column(LargeBinary, nullable=False)
    data_criacao = Column(DateTime, default=datetime.datetime.now)
    tipo: str = Column(String(100), nullable=False)

        