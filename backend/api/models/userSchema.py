from pydantic import BaseModel

from enum import Enum

class typeUser(str, Enum):
    IDOSO = 'idoso'
    CUIDADOR = 'cuidador'

class UserBase(BaseModel):
    '''Classe para definir os modelos recebidos na API'''
    nome: str
    email: str
    senha: str
    # data_criacao 
    tipo: typeUser


class UserRequest(UserBase):
    '''...'''

class UserResponse(UserBase):
    '''Classe para definir o Usuário devolvido pela API'''
    id: int
    class Config:
        orm_mode = True