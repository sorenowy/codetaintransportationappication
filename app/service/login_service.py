from fastapi import HTTPException, status

from app.repository.user_repository import UserRepository
from app.model.login import LoginDTO
from app.model.user import UserResponseDTO
from app.security.password_hasher import read_hashed_password
from app.security.jwt_provider import signJWT


class LoginService:
    
    def __init__(self) -> None:
        pass
    
    async def login(self, credentials: LoginDTO):
        user = await UserRepository.get_user_by_email(credentials.email)
        if user is None or read_hashed_password(credentials.password, user.password) is False:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
        if not user.is_verified:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="User not verified. Please check your inbox.")
        user_dto = UserResponseDTO(**{
                'id':user.id,
                'name':user.name,
                'surname':user.surname,
                'email':user.email,
                'address':user.address,
                'is_admin':user.is_admin,
                'is_verified':user.is_verified
            })
        
        token = signJWT(user_dto)
        return { "token": token }
    
    
login_service = LoginService()