from os import terminal_size
from typing import List, Optional, Text

from pydantic import BaseModel
from sqlalchemy.sql.sqltypes import TEXT,INTEGER



class UserData(BaseModel):
    name: str
    class Config:
        orm_mode = True
class ProjectData(UserData):
    class Config:
        orm_mode = True
class UserId(BaseModel):
    user_id: int 
    class Config:
        orm_mode = True

# class ShowProject(ProjectData):
#     owner : List[UserData] = []
#     class Config:
#         orm_mode = True



# class UserBase(BaseModel):
#     email: str

# class Data(BaseModel):
#     user_name: str
#     password: str

#     class Config:
#         orm_mode = True


# class User(BaseModel):
#     user_name: str
#     email: str
#     password: str
    
#     class Config:
#         orm_mode = True