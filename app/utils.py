from passlib.context import CryptContext
pwd_context= CryptContext(schemes=["sha256_crypt"],deprecated="auto")

def hash(password:str):
    return pwd_context.hash(password)

def verify(plain_pass,hashed_pass):
    return pwd_context.verify(plain_pass, hashed_pass)