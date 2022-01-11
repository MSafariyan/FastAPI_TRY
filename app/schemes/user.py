from pydantic import BaseModel

class UserBase(BaseModel):
    username: str
    email: str
    password: str
    
    class Config:
        orm_mode = True
            
    
class Login(BaseModel):
    username: str
    password: str
    
class Token(BaseModel):
    access_token: str
    token_type: str
    

class TokenData(BaseModel):
    email: str | None = None

