from pwdlib import PasswordHash
from datetime import datetime, timedelta, timezone
import jwt
from app.core.config import setiings

password_hash = PasswordHash.recommended()

def hash_password(password: str) -> str:
    return password_hash.hash(password)

def verify_password(password: str, hashed_password: str) -> bool:
    return password_hash.verify(password, hashed_password)

def create_access_token(user_id: int) -> str:
    expire_at = datetime.now(timezone.utc) + timedelta(minutes=setiings.access_token_expire_minutes)
    payload = {
        "sub": str(user_id),
        "exp": expire_at,
        "type": "access"
    }
    return jwt.encode(payload, setiings.jwt_secret_key, algorithm=setiings.jwt_algorithm)