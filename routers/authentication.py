from fastapi import APIRouter, Depends, HTTPException, status
from schemas import Login
from db import get_db
from sqlalchemy.orm import Session
import models
from hashing import Hashing
from datetime import timedelta
from .token import create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES
from fastapi.security import OAuth2PasswordRequestForm
router = APIRouter(
    tags=['authentication'],
)


@router.post('/login')
def login(form_data: OAuth2PasswordRequestForm=Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(
        models.User.email == form_data.username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='invalid credential')
    print(user)
    if not Hashing.verify_password(form_data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='password missmatch')

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
