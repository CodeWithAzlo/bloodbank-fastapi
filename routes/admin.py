from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from app.schemas import Token
from app.utils import create_access_token
from app.config import ADMIN_USERS


router = APIRouter(prefix="/admin", tags=["Admin"])


@router.post("/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    email = form_data.username
    password = form_data.password

    if email not in ADMIN_USERS or ADMIN_USERS[email] != password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token = create_access_token(data={"sub": email})
    return {"access_token": access_token, "token_type": "bearer"}
