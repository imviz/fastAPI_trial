from fastapi import FastAPI,Depends,status,Response,HTTPException
from schemas import BlogSchema,Show,UserSchema,UserShow
import models
from typing import List
from db import engine,get_db
from sqlalchemy.orm import Session
from hashing import Hashing


from routers import blog,authentication
# from passlib.context import CryptContext

app=FastAPI()

# def get_db():
#     dbs=SessionLocal()
#     try:
#         yield dbs
#     finally:
#         dbs.close()

# for migrations

models.Base.metadata.create_all(bind=engine)

app.include_router(authentication.router)
app.include_router(blog.router)





# --------------------------all thinks is changed to router




# @app.post('/blog',status_code=status.HTTP_201_CREATED,tags=['blog'])
# def create(request:BlogSchema,db :Session=Depends(get_db)):
    
#     new_blog=models.Blog(title=request.title,body=request.body,no=request.no)
#     db.add(new_blog)
#     db.commit()
#     db.refresh(new_blog)
#     return new_blog
    
# @app.get('/blog',status_code=status.HTTP_200_OK,response_model=List[Show],tags=['blog'])
# def all( db:Session=Depends(get_db)):
#     blogs=db.query(models.Blog).all()   
#     return blogs

# @app.get('/blog/{id}',response_model=Show,tags=['blog'])
# def one(id:int,response:Response,db:Session=Depends(get_db)):
#     blogs=db.query(models.Blog).filter(models.Blog.id==id).first()
#     if not blogs:
#         # one line error handling
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'details not found for this id {id}')
    
    
#         response.status_code=status.HTTP_404_NOT_FOUND
#         return {'detail':'not found this id details'}
#     return blogs


# @app.delete('/blog/{id}',tags=['blog'])
# def destroy(id,db:Session=Depends(get_db)):
#     db.query(models.Blog).filter(models.Blog.id==id).delete(synchronize_session=False)
#     db.commit()
#     return {'success'}

# @app.put('/blog/{id}',tags=['blog'])
# def update(id,request:BlogSchema,db:Session=Depends(get_db)):
#     blogs=db.query(models.Blog).filter(models.Blog.id==id).update({'title':request.title,'no':request.no,'body':request.body})
#     db.commit()
#     # db.refresh(blogs)
#     return blogs


# for hashing
# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# for user creation




# ---------------------------------------








@app.post('/user',response_model=UserShow,tags=['user'])
def create_user(request:UserSchema,db:Session=Depends(get_db)):
    # hased_pass=pwd_context.hash(request.password)
    new_user=models.User(name=request.name,email=request.email,password=Hashing.bycript(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user




@app.get('/user/{id}',tags=['user'])
def get_user(id,db:Session=Depends(get_db)):
    user=db.query(models.User).filter(models.User.id==id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='no data present')
    return user
