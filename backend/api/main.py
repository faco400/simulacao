from fastapi import FastAPI
from backend.db.database import initialize_database

from backend.api.controllers.userController import users

from fastapi.middleware.cors import CORSMiddleware

api = FastAPI()

origins = [
    "http://localhost:3000",
]

api.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

api.include_router(users)

@api.on_event("startup")
async def startup():
    initialize_database()

@api.get("/")
async def root():
    return {"message": "Hello World"}

@api.get('/status')
async def index():
    return {"status": "online"}