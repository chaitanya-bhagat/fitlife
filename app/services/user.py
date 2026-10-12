from app.schemas.user import UserRegister, GetUser, UserLogin
from app.core.security import hash_password, verify_password, create_access_token
from app.database.models.user import User
from app.repositories.user import UserRepository

class UserAlreadyExistsError(Exception):
    pass

class InvalidCredentialsError(Exception):
    pass

class UserService:
    def __init__(self, repository: UserRepository) -> None:
        self.repository =repository

    async def register_user(self, data: UserRegister) -> User:
        existing_user = await self.repository.get_by_email(str(data.email))
        if existing_user:
            raise UserAlreadyExistsError(f"User with email {data.email} already exists.")

        password_hash = hash_password(data.password)
        user = await self.repository.create(email=str(data.email), passoword_hash=password_hash)
        return user

    async def login(self, data: UserLogin) -> str:
        user = await self.repository.get_by_email(str(data.email))
        if user is None:
            raise InvalidCredentialsError("Invalid email or password.")

        if not verify_password(data.password, user.password_hash):
            raise InvalidCredentialsError("Invalid email or password.")

        access_token = create_access_token(user.id)
        return access_token