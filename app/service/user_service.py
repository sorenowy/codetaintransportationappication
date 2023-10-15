from fastapi import HTTPException, status

from app.repository.user_repository import UserRepository
from app.model.user import User, UserRequestDTO, UserResponseDTO
from app.model.email import Email
from app.utils.validator import validate_email, validate_password_policy
from app.security.password_hasher import hash_password
from app.utils.mail_sender import mail_sender

class UserService:
    def __init__(self) -> None:
        pass
    
    async def get_all_users(self):
        return await UserRepository.get_all_users()


    async def get_user_by_id(self, id: int):
        result = await UserRepository.get_user_by_id(id)
        if result is not None:
            return UserResponseDTO(**{
                'id':result.id,
                'name':result.name,
                'surname':result.surname,
                'email':result.email,
                'address':result.address,
                'is_admin':result.is_admin,
                'is_verified':result.is_verified
            })   
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No such user in database")
            


    async def create_user(self, data: UserRequestDTO):
        await UserService.__validate_data(data)
        hashed_password = hash_password(data.password)
        data.password = hashed_password
        return await UserRepository.create_user(data)


    async def delete_user(self, id: int):
        user_to_delete = await UserRepository.get_user_by_id(id)
        if user_to_delete is not None:
            await UserRepository.delete_user(id)
            delete_email = UserService.__create_delete_confirmation_email(user_to_delete, user_to_delete.email)
            await mail_sender.send_delete_confirmation_email(delete_email)
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    

    async def update_user(self, id: int, data: UserRequestDTO):
        return await UserRepository.update_user(id, data)


    async def __validate_data(self, data: UserRequestDTO):
        print(f"Entered validation! {data.email}, {data.password}")
        if not data.email or not data.password:
            print("Entered no email or password!")
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
        if validate_email(data.email) is False:
            print("Entered faulty email")
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid email format. It should look like this name@example.domain")
        if await UserRepository.get_user_by_email(data.email) is not None:
            print("Entered duplicate email")
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="User with such email already exists.")
        if validate_password_policy(data.password) is False:
            print("password is no no")
            raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="Password does not confirms to security policy.")
        

    def __create_delete_confirmation_email(self, data: User, user_email: str) -> Email:
        email = Email(
            email=[user_email],
            body={
                "name": data.name
            }
        )
        return email
    
    
user_service = UserService()
