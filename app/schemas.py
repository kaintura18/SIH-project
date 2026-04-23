from .database import Base, engine, Sessionlocal
from sqlalchemy import Column, Integer,String, Boolean, TIMESTAMP,text
from sqlalchemy.sql.expression import null
from typing import Optional

class User(Base):
    __tablename__="user_details"
    id= Column (Integer, primary_key=True, nullable=False)
    name=Column (String,nullable=False)
    email=Column (String,unique=True, nullable=False,index=True)
    password_hashed=Column(String, nullable=False)
    created_at=Column(TIMESTAMP(timezone=True), nullable= False, server_default=text('now()'))
    
class contractor(Base):
    __tablename__="contractor_details"
    id= Column (Integer, primary_key=True, nullable=False)
    contractor_name=Column (String,nullable=False)
    contractor_email=Column (String,unique=True, nullable=False,index=True)
    contractor_password_hashed=Column(String, nullable=False)

class project(Base):
    __tablename__="project_details"
    id= Column (Integer, primary_key=True, nullable=False)
    project_name=Column (String,nullable=False)
    project_description=Column(String, nullable=False)
    project_location=Column(String, nullable=False)
    project_budget=Column(Integer, nullable=False)
    project_deadline=Column(TIMESTAMP(timezone=True), nullable= False)