from pydantic import BaseModel,EmailStr
from typing import Optional
from datetime import datetime
from .database import Base, engine, Sessionlocal
from sqlalchemy import Column, Integer,String, Boolean, TIMESTAMP,text
from sqlalchemy.sql.expression import null
from fastapi import Form

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str


class UserOut(BaseModel):
    id: int
    name: str
    email: EmailStr

    class Config:
        from_attributes = True


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token:str
    token_type: str
class Token_Data(BaseModel):
    id:Optional[str]=None


class FeasibilityRequest(BaseModel):
    location: str
    roof_area: float
    open_space: float

class CostRequest(BaseModel):
    harvesting_type: str
    location: str