from sqlalchemy import Column, Integer, String, DateTime, LargeBinary

import datetime

from db.database import Base


class User(Base):
    __tablename__ = 'usuarios'
    
    email: str = Column(String(60), nullable=False, primary_key=True)
    nome: str = Column(String(100), nullable=False)
    senha: str = Column(String(256), nullable=False)
    data_criacao = Column(DateTime, default=datetime.datetime.now)
    tipo: str = Column(String(8), nullable=False)

        