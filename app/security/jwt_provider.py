import jwt
from fastapi import HTTPException, status, Depends
from fastapi.security import APIKeyHeader

from app.config.constants import JWT_ALGORITHM, SECRET_KEY
from app.model.user import UserResponseDTO
from app.model.token import Token


bearer_header = APIKeyHeader(name="Authorization")

def signJWT(user: UserResponseDTO):
    payload = {
        "email": user.email,
        "user_id": user.id,
        "is_admin": user.is_admin,
        "is_verified": user.is_verified
    }
    
    token = jwt.encode(payload, SECRET_KEY, algorithm=JWT_ALGORITHM)
    
    return token


def decodeJWT(token: str = Depends(bearer_header)) -> Token:
    try:
        decoded_token = jwt.decode(
            token, SECRET_KEY, algorithms=[JWT_ALGORITHM]
        )
        
        token = Token(**{
            'email': decoded_token.get('email'),
            'user_id': decoded_token.get('user_id'),
            'is_admin': decoded_token.get('is_admin'),
            'is_verified': decoded_token.get('is_verified')
        })
        
        return token
    
    except:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid access token")
