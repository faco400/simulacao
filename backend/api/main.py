from fastapi import FastAPI
from db.database import initialize_database

from api.controllers.userController import users
from api.helper.authorization import token # testando

from fastapi.middleware.cors import CORSMiddleware

api = FastAPI()

origins = [
 '*'
]

api.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

api.include_router(users)
api.include_router(token) #testando token

@api.on_event("startup")
async def startup():
    initialize_database()

@api.get("/")
async def root():
    return {"message": "Hello World"}

@api.get('/status')
async def index():
    return {"status": "online"}