from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from .. import schemas, models, utils, database
from ..database import get_db

router = APIRouter(
    prefix="/users",
    tags=["users"]
)


# ----------------------------
# Create user (signup)
# ----------------------------
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=models.UserOut)
def create_user(user: models.UserCreate, db: Session = Depends(get_db)):
    # hash the password
    hashed_password = utils.hash(user.password)

    new_user = schemas.User(
        name= user.name,
        email=user.email,
        password_hashed=hashed_password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


# ----------------------------
# Get user by ID
# ----------------------------
@router.get("/{id}", response_model=models.UserOut)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(schemas.User).filter(schemas.User.id == id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"user with id {id} does not exist"
        )
    return user