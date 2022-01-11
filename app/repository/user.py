from sqlalchemy.orm import Session
from ..schemes import user as userSchemes
from ..models import user as userModels
from .. import database
from passlib.context import CryptContext
from ..hashing import Hash

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_all_users(db):
    users = db.query(userModels.User).all()
    return users

def add_user(request, db):
    hashedpassword = pwd_context.hash(request.password)
    new_user = userModels.User(username=request.username, email=request.email, password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message":f"The user {new_user.username} registerd successfully"}