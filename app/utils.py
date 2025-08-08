# from datetime import datetime, timedelta
# from jose import JWTError, jwt
# from fastapi import Depends, HTTPException, status
# from fastapi.security import OAuth2PasswordBearer

# # Secret for JWT
# SECRET_KEY = "your_secret_key"
# ALGORITHM = "HS256"
# ACCESS_TOKEN_EXPIRE_MINUTES = 60

# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/admin/login")

# # Admin users
# ADMIN_USERS = {
#     "codewithazlo@gmail.com": "adminpass",
#     "syednaved@gmail.com": "adminpass2",
# }


# def create_access_token(data: dict, expires_delta: timedelta = None):
#     to_encode = data.copy()
#     expire = datetime.now() + (
#         expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
#     )
#     to_encode.update({"exp": expire})
#     return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


# def get_current_admin(token: str = Depends(oauth2_scheme)) -> str:
#     credentials_exception = HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         detail="Invalid authentication credentials",
#         headers={"WWW-Authenticate": "Bearer"},
#     )
#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         email: str = payload.get("sub")
#         if email is None or email not in ADMIN_USERS:
#             raise credentials_exception
#         return email
#     except JWTError:
#         raise credentials_exception


# utils.py

from datetime import datetime, timedelta
from jose import JWTError, jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from app.config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES, ADMIN_USERS

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/admin/login")


def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    expire = datetime.now() + (
        expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def get_current_admin(token: str = Depends(oauth2_scheme)) -> str:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid authentication credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None or email not in ADMIN_USERS:
            raise credentials_exception
        return email
    except JWTError:
        raise credentials_exception
