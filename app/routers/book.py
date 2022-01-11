from fastapi import APIRouter, Depends, status, Response, HTTPException
from sqlalchemy.orm import Session
from .. import database
from ..schemes import book as bookSchemes
from ..schemes import user as userSchemes
from ..models import book as bookModels
from typing import List
from ..repository import book as bookRepo
from .. import oauth2

router = APIRouter()

@router.post('/', status_code=201)
def addBook(request:bookSchemes.BookBase, db:Session=Depends(database.conn), get_current_user: userSchemes.UserBase = Depends(oauth2.get_current_user)):
    return bookRepo.add_book(request, db)

@router.get('/', status_code=200, response_model=List[bookSchemes.BookBase])
def allBooks(db:Session=Depends(database.conn)):
    return bookRepo.get_all_books(db)[:10]

@router.get('/{id}', status_code=200, response_model=bookSchemes.BookBase)
def getBook(id:int, db:Session=Depends(database.conn)):
    return bookRepo.get_book_by_id(id, db)

@router.delete('/{id}', status_code=200)
def deleteBook(id:int, db:Session = Depends(database.conn), get_current_user: userSchemes.UserBase = Depends(oauth2.get_current_user)):
    return bookRepo.delete_book_by_id(id, db)

@router.put('/{id}', status_code=202)
def updateBook(id:int, request: bookSchemes.BookBase, db:Session=Depends(database.conn), get_current_user: userSchemes.UserBase = Depends(oauth2.get_current_user)):
    return bookRepo.update_book_by_id(id, db)