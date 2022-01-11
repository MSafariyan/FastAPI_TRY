from fastapi import APIRouter, Depends, status, Response, HTTPException
from sqlalchemy.orm import Session
from .. import database
from ..schemes import user as userSchemes
from ..models import user as userModels
from typing import List
from ..repository import user as userRepo
from .. import oauth2


router = APIRouter()

@router.get('/', status_code=200, response_model=List[userSchemes.UserBase])
def allUsers(db:Session=Depends(database.conn), get_current_user: userSchemes.UserBase = Depends(oauth2.get_current_user)):
    return userRepo.get_all_users(db)

@router.post('/', status_code=201)
def addUser(request:userSchemes.UserBase, db:Session=Depends(database.conn), get_current_user: userSchemes.UserBase = Depends(oauth2.get_current_user)):
    return userRepo.add_user(request, db)
