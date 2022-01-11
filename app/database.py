from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL= 'sqlite:///./book.db'

engin = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
Base = declarative_base()
SessionLocal = sessionmaker(bind=engin,autocommit=False,autoflush=False)

def conn():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()