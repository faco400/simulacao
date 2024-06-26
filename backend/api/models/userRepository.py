from typing import List
from sqlalchemy.orm import Session
from api.models.user import User
from fastapi import HTTPException, status

class UserRepository:

  @staticmethod
  def create(user: User, database: Session) -> User:
    '''Função para criar um usuario'''
    try:
        existing = database.query(User).filter(User.email == user.email).first()
        if existing:
          raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail='Usuario ja existe')

        database.add(user)
        database.commit()
    except:
        database.rollback()
        raise
    return user

  @staticmethod
  def get(email: str, database: Session) -> User:
    '''Função para criar um usuario'''
    try:
        existing = database.query(User).filter(User.email == email).first()
        if not existing:
          raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Usuario nao existe')

    except:
        raise
    return existing