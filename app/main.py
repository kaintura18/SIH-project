from fastapi import FastAPI, Response, status , HTTPException, Depends
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from . import schemas
from .database import engine, Sessionlocal,get_db
from sqlalchemy.orm import Session
from .schemas import User
#from .models import FeasibilityRequest, CostRequest
from .routers import  users,auth,oauth2,posts
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

schemas.Base.metadata.create_all(bind=engine)

app.include_router(users.router)
app.include_router(auth.router)
#app.include_router(oauth2.router)
# CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],  # Change to your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(posts.router)
