from typing import List
from fastapi import APIRouter, HTTPException, status, Depends

from api.models.userSchema import UserRequest, UserResponse
from api.models.user import User
from api.models.userRepository import UserRepository
from db.database import get_database

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

    '''Cria e salva um usuário e carteira'''
    user = UserRepository.create(User(**req), database=database)

    return user
