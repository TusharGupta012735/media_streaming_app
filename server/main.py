from fastapi import FastAPI
from models.base import Base
from routes import auth
from database import engine

app = FastAPI()
app.include_router(auth.router, prefix='/auth')

#TODO : accepts data from user from body
#check if user exists in database
#if user doesnt exist add new user

Base.metadata.create_all(engine)