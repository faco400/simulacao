from sqlalchemy import Boolean, Column, Integer, String, DateTime, Enum
import enum
import datetime

from backend.db.database import Base

class typeUsers(enum.Enum):
  idoso = 1
  cuidador = 2


class User(Base):
    __tablename__ = 'usuarios'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome: str = Column(String(100), nullable=False)
    email: str = Column(String(100), nullable=False)
    senha: str = Column(String(100), nullable=False)
    data_criacao = Column(DateTime, default=datetime.datetime.now)
    tipo: str = Column(Enum(typeUsers))