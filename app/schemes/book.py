from pydantic import BaseModel

class BookBase(BaseModel):
    title: str
    current_price: int
    special_price: int
    img: str
    status: bool
    
    class Config:
        orm_mode = True
                