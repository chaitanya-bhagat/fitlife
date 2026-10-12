from pydantic import BaseModel, ConfigDict, Field, EmailStr

class UserRegister(BaseModel):
    email: EmailStr 
    password: str = Field(min_length=8, max_length=128)

class GetUser(BaseModel):
    id: int
    email: EmailStr

    model_config = ConfigDict(from_attributes=True)

class UserLogin(BaseModel):
    email: EmailStr
    password: str 

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"