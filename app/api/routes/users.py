from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.models.user import User
from app.schemas.user import GetUser
from app.api.dependencies.auth import get_current_user

router = APIRouter(
    prefix="/users",
    tags=["users"],
)

@router.get("/me", response_model=GetUser)
async def get_my_profile(current_user: User = Depends(get_current_user)):
    return current_user