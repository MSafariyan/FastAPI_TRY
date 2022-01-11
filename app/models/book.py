import datetime
from ..database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship

class Book(Base):
    __tablename__ = "book"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String)
    current_price = Column(Integer)
    special_price = Column(Integer)
    img = Column(String)
    status = Column(Boolean)
    