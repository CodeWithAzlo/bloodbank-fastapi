from pydantic import BaseModel


class BloodRequestCreate(BaseModel):
    name: str
    email: str
    contact: str
    blood_group: str
    type: str  # donate or need


class BloodRequestOut(BloodRequestCreate):
    id: int

    class Config:
        from_attributes = True


class AdminLogin(BaseModel):
    email: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str
