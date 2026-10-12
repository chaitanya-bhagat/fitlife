from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.session import get_db
from app.schemas.user import UserRegister, GetUser, UserLogin, TokenResponse
from app.services.user import UserService, UserAlreadyExistsError, InvalidCredentialsError
from app.repositories.user import UserRepository

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)

def get_user_service(db: AsyncSession = Depends(get_db)) -> UserService:
    repository = UserRepository(db)
    return UserService(repository)

@router.post("/register", response_model=GetUser, status_code=status.HTTP_201_CREATED)
async def register_user(payload: UserRegister, service: UserService = Depends(get_user_service)):
    try:
        new_user = await service.register_user(payload)
        return new_user
    except UserAlreadyExistsError:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User with this email already exists.",
        )

@router.post("/login", response_model=TokenResponse)
async def login_user(payload: UserLogin, service: UserService = Depends(get_user_service)):
    try:
        access_token = await service.login(payload)
    except InvalidCredentialsError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password.",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return TokenResponse(access_token=access_token)
    