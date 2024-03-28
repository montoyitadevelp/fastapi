from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models, schema, utils, oauth2

router = APIRouter(tags=["Authentication"])


@router.post("/api/login")
def login(
    user_credientials: schema.UserLogin,
    db: Session = Depends(get_db),
):
    user = (
        db.query(models.User)
        .filter(models.User.email == user_credientials.email)
        .first()
    )
    if not user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials"
        )
    if not utils.verifypassword(user_credientials.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials"
        )
    print(user)
    access_token = oauth2.create_access_token(data={"user_id": user.id})
    return {"access_token": access_token, "info_user": user}
