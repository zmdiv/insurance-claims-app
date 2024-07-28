from pydantic import BaseModel

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int

    class Config:
        from_attributes = True

class ClaimBase(BaseModel):
    description: str
    amount: float

class ClaimCreate(ClaimBase):
    pass

class Claim(ClaimBase):
    id: int
    user_id: int

    class Config:
        from_attributes = True
