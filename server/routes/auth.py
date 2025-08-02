import uuid
import bcrypt
from fastapi import APIRouter, Depends, HTTPException
from database import get_db
from models.user import User
from pydantic_schemas.user_create import UserCreate
from sqlalchemy.orm import Session

router = APIRouter() #this doesnt create a new fastapi instance for every route

@router.post("/signup")
def signup(user: UserCreate, db: Session = Depends(get_db)): #step-1 data input is done
    #step-2 check if user alreaedy exists
    user_db = db.query(User).filter(User.email == user.email).first()
    if user_db:
        raise HTTPException(400,"User with the email already exists")
    #step-3 add the user 
    hashed_pw = bcrypt.hashpw(user.password.encode(), bcrypt.gensalt())
    user_db = User(
        id = str(uuid.uuid4()),
        email = user.email,
        password = hashed_pw,
        name = user.name,
    )
    db.add(user_db)
    db.commit()
    db.refresh(user_db)
    return user_db
    
