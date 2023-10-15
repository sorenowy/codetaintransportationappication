from fastapi import APIRouter, Depends, status

from app.api.v1.schema.schema import ResponseSchema
from app.service.user_service import user_service
from app.model.user import UserRequestDTO
from app.api.v1.docs.summary import UsersApiSummaryDocs
from app.security.jwt_provider import decodeJWT
from app.api.v1.schema.enum import ResponseStatus

users_router = APIRouter(prefix="/users", tags=["Users"])

@users_router.get(
    "",
    summary=UsersApiSummaryDocs.GET_ALL_USERS,
    response_model=ResponseSchema,
    response_model_exclude_none=True
)
async def get_all_users(user=Depends(decodeJWT)):
    result = await user_service.get_all_users()
    return ResponseSchema(detail=ResponseStatus.SUCCESS.name, result=result)


@users_router.get(
    "/{userId}",
    summary=UsersApiSummaryDocs.GET_USER,
    response_model=ResponseSchema,
    response_model_exclude_none=True
)
async def get_user_by_id(userId: int, token = Depends(decodeJWT)):
    print(token)
    result = await user_service.get_user_by_id(userId)
    return ResponseSchema(detail=ResponseStatus.SUCCESS.name, result=result)


@users_router.post(
    "",
    summary=UsersApiSummaryDocs.CREATE_USER,
    response_model=ResponseSchema,
    response_model_exclude_none=True,
    status_code=status.HTTP_201_CREATED
)
async def create_user(user_data: UserRequestDTO, token = Depends(decodeJWT)):
    await user_service.create_user(user_data)
    return ResponseSchema(detail=ResponseStatus.SUCCESS.name)


@users_router.delete(
    "/{userId}",
    summary=UsersApiSummaryDocs.DELETE_USER,
    response_model=ResponseSchema,
    response_model_exclude_none=True
)
async def delete_user(userId: int, token = Depends(decodeJWT)):
    await user_service.delete_user(userId)
    return ResponseSchema(detail=ResponseStatus.SUCCESS.name)


@users_router.patch(
    "/{userId}",
    summary=UsersApiSummaryDocs.UPDATE_USER,
    response_model=ResponseSchema,
    response_model_exclude_none=True
)
async def update_user(user_data: UserRequestDTO, userId: int, token = Depends(decodeJWT)):
    await user_service.update_user(userId, user_data)
    return ResponseSchema(detail=ResponseStatus.SUCCESS.name)
