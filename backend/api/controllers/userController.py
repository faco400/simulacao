from typing import List
from fastapi import APIRouter, HTTPException, status, Depends

from backend.api.models.userSchema import UserRequest, UserResponse
from backend.api.models.user import User
from backend.api.models.userRepository import UserRepository
from backend.db.database import get_database

from sqlalchemy.orm import Session

users = APIRouter(
    prefix = '/users',
    tags = ['users'],
    responses = {404: {"description": "Not found"}},
)

@users.post("/register",
    status_code = status.HTTP_201_CREATED,
    response_model=UserResponse
)
def create(
    request: UserRequest, 
    database: Session = Depends(get_database)
    ):

    req = request.dict()

    # user = {key: req[key] for key in req.keys()
    #           & {'name', 'surname', 'email','cpf', 'is_admin',
    #             'telefone', 'status'}}
    
    # wallet = {key: req[key] for key in req.keys()
    #           & {'qtdCreditos', 'qtdCreditosSolicitados'}}

    '''Cria e salva um usuário e carteira'''
    user = UserRepository.create(User(**req), database=database)

    print(user)
    return user
