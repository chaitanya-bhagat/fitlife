import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jwt import InvalidTokenError
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import setiings
from app.database.models.user import User
from app.database.session import get_db
from app.repositories.user import UserRepository

bearer_scheme = HTTPBearer(auto_error=False)

async def get_current_user(
        credentials: HTTPAuthorizationCredentials | None = Depends(bearer_scheme),
        db: AsyncSession = Depends(get_db)
) -> User:
    unauthorized = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid or missing authentication credentials.",
        headers={"WWW-Authenticate": "Bearer"},
    )
    if credentials is None:
        raise unauthorized

    token = credentials.credentials

    try:
        payload = jwt.decode(token, setiings.jwt_secret_key, algorithms=[setiings.jwt_algorithm], options={"require": ["exp", "sub"]})
        if payload.get("type") != "access":
            raise unauthorized
        sub = payload.get("sub")
        if (not isinstance(sub, str)) or (not sub.isdigit()):
            raise unauthorized
        user_id = int(sub)
    except InvalidTokenError:
        raise unauthorized

    repository = UserRepository(db)
    user = await repository.get_by_id(user_id)
    if user is None:
        raise unauthorized
    return user
