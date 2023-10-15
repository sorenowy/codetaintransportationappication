from fastapi import APIRouter

from app.api.v1.schema.schema import ResponseSchema
from app.model.login import LoginDTO
from app.api.v1.docs.summary import LoginApiSummaryDocs
from app.api.v1.schema.enum import ResponseStatus
from app.service.login_service import login_service

login_router = APIRouter(prefix="/login", tags=["Login"])

@login_router.post(
    "",
    summary=LoginApiSummaryDocs.POST_LOGIN,
    response_model=ResponseSchema,
    response_model_exclude_none=True
)
async def login(credentials: LoginDTO):
    result = await login_service.login(credentials)
    return ResponseSchema(detail=ResponseStatus.SUCCESS.name, result=result)
