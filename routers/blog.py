from fastapi import APIRouter, Depends, status, HTTPException, Response
from typing import List
from sqlalchemy.orm import Session
from db import get_db
from schemas import BlogSchema, Show, UserSchema, UserShow
import models
from .oauth2 import get_current_user

router = APIRouter(
    tags=['blogzz'],  # for document taging
    prefix="/blog", )  # for naming common


@router.get('/', status_code=status.HTTP_200_OK, response_model=List[Show])
def all(db: Session = Depends(get_db), current_user: UserShow = Depends(get_current_user)):
    blogs = db.query(models.Blog).all()
    return blogs


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: BlogSchema, db: Session = Depends(get_db)):

    new_blog = models.Blog(title=request.title,
                           body=request.body, no=request.no)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog
    #


@router.get('/{id}', response_model=Show)
def one(id: int, response: Response, db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blogs:
        # one line error handling
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'details not found for this id {id}')

        # response.status_code=status.HTTP_404_NOT_FOUND
        # return {'detail':'not found this id details'}
    return blogs


@router.delete('/{id}')
def destroy(id, db: Session = Depends(get_db)):
    db.query(models.Blog).filter(models.Blog.id ==
                                 id).delete(synchronize_session=False)
    db.commit()
    return {'success'}


@router.put('/{id}')
def update(id, request: BlogSchema, db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).filter(models.Blog.id == id).update(
        {'title': request.title, 'no': request.no, 'body': request.body})
    db.commit()
    # db.refresh(blogs)
    return blogs
