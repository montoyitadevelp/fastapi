from fastapi import status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List
from .. import models, schema, utils
from ..database import get_db
from .. import oauth2

router = APIRouter(prefix="/api/users", tags=["Users"])

@router.get(
    "/", status_code=status.HTTP_200_OK, response_model=List[schema.UserResponse]
)
def get_users(
    db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)
):
    users = db.query(models.User).all()
    return users


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=schema.UserResponse)
def get_user(
    id: int,
    db: Session = Depends(get_db),
    current_user: int = Depends(oauth2.get_current_user),
):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id: {id} was not found",
        )
    return user


@router.post(
    "/", status_code=status.HTTP_201_CREATED, response_model=schema.UserResponse
)
def create_user(
    user: schema.UserCreate,
    db: Session = Depends(get_db),
    current_user: int = Depends(oauth2.get_current_user),
):
    hashed_password = utils.hash(user.password)
    user.password = hashed_password
    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
