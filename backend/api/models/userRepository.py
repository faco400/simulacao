from typing import List
from sqlalchemy.orm import Session
from backend.api.models.user import User

class UserRepository:

  @staticmethod
  def create(user: User, database: Session) -> User:
    '''Função para criar um usuario'''
    try:
        database.add(user)
        database.commit()
    except:
        database.rollback()
    return user
