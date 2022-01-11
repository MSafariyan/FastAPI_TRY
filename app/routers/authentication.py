from fastapi import APIRouter, Depends, HTTPException
from ..schemes import user as userSchemes
from .. import database
from ..models import user as userModels
from sqlalchemy.orm import Session
from ..hashing import Hash
from ..token import create_access_token
from fastapi.security import  OAuth2PasswordRequestForm
router = APIRouter()

@router.post('/login')
def login(request:OAuth2PasswordRequestForm = Depends(), db: Session=Depends(database.conn)):
    existUser = db.query(userModels.User).filter(userModels.User.email == request.username ).first()
    if not existUser:
        raise HTTPException(status_code=200, detail=f"Invalid login")
    
    if not Hash.verify(request.password, existUser.password):
        raise HTTPException(status_code=200, detail=f"password is wrong")

    access_token = create_access_token(
        data={"sub": existUser.username}
    )
    return {"access_token": access_token, "token_type": "bearer"}
