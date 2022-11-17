from pydantic import BaseModel
from typing import Optional


class BlogSchema(BaseModel):
    title:str
    body:str
    no:int
    
class Show(BaseModel):
    no:int
    class Config():
        orm_mode=True
        
class UserSchema(BaseModel):
    name:str
    email:str
    password:str
    
class UserShow(BaseModel):
    name:str
    email:str
    class Config():
        orm_mode=True
        
class Login(BaseModel):
    email:str
    password:str
    
    
    
    

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None