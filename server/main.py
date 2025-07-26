from fastapi import FastAPI
from pydantic import BaseModel
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

app = FastAPI()

DATABASE_URL = "postgresql://postgres:TusharGupta@2005@localhost:5432/audio_streaming_app"

engine = create_engine(DATABASE_URL) #central source of connection to database
sessionLocal = sessionmaker(
    autoflush=False,
    bind=engine,
) 
#a factory to create session to interact with database

class User(BaseModel):
    name : str
    email : str
    password : str

#TODO : accepts data from user from body
#check if user exists in database
#if user doesnt exist add new user

@app.post("/signup")
def signup(user: User): #step-1 data input is done
    print(user.name)
    print(user.email)
    print(user.password)
    
    pass
    