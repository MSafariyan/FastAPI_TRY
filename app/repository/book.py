from sqlalchemy.orm import Session
from ..schemes import book as bookSchemes
from ..models import book as bookModels
from .. import database

def get_all_books(db:Session):
    books = db.query(bookModels.Book).all()
    return books

def add_book(request, db):
    new_book = bookModels.Book(title=request.title, current_price=request.current_price, special_price=request.special_price, img=request.img, status=request.status)
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return {"message":f"Book {new_book.title} added to db"}

def get_book_by_id(id,db):
    book = db.query(bookModels.Book).filter(bookModels.Book.id == id).first()
    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"blog with the id {id} not found")
    return book

def delete_book_by_id(id, db):
    book = db.query(bookModels.Book).filter(bookModels.Book.id == id)
    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"blog with the id {id} not found")
    book.delete(synchronize_session=False)
    db.commit()
    return f"The delete operation was successfull"

def update_book_by_id(id, db):
    book = db.query(bookModels.Book).filter(bookModels.Book.id == id)
    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"blog with the id {id} not found")
    book.update({"title":request.title, "current_price":request.current_price, "special_price":request.special_price, "status":request.status, "img":request.img})
    db.commit()
    return "The updated operation was successfull"