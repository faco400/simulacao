from typing_extensions import Annotated
from typing import Union
from datetime import datetime, timedelta, timezone

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from api.models.userRepository import UserRepository
from api.models.user import User 

from sqlalchemy.orm import Session
from db.database import get_database

from passlib.context import CryptContext

from pydantic import BaseModel

import jwt
from jwt.exceptions import InvalidTokenError

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# to get a string like this run:
# openssl rand -hex 32
SECRET_KEY = "02cd6d63ddfbef12ede35bbdb3c799bb32905db16cda504417a1f46c0e58a23e"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Union[str, None] = None

token = APIRouter(
    prefix = '/token',
    tags = ['token'],
    responses = {400: {"description": "Not found"}},
)


async def get_current_user(
        token: Annotated[str, Depends(oauth2_scheme)],
        database: Session = Depends(get_database)
        ):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except InvalidTokenError:
        raise credentials_exception
    user = UserRepository.get(token_data.username, database=database)
    if user is None:
        raise credentials_exception
    return user
    

@token.get("/users/me")
async def read_users_me(
    current_user: Annotated[User, Depends(get_current_user)]):
    return current_user


@token.post("")
async def login(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    database: Session = Depends(get_database)
    ): 
    user = authenticate_user(database, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def authenticate_user(database, username: str, password: str):
    user = UserRepository.get(username, database=database)
    if not user:
        return False
    if not verify_password(password, user.senha):
        return False
    return user

def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt