from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse

from app.api.v1.schema.schema import ResponseSchema
from app.service.register_service import RegisterService
from app.model.register import RegisterDTO
from app.model.email import Email
from app.api.v1.docs.summary import RegisterApiSummaryDocs
from app.service.register_service import register_service
from app.api.v1.schema.enum import ResponseStatus

register_router = APIRouter(prefix="/register", tags=["Register"])

@register_router.post(
    "",
    summary=RegisterApiSummaryDocs.POST_REGISTER,
    response_model=ResponseSchema,
    response_model_exclude_none=True
)
async def register(credentials: RegisterDTO, request: Request):
    await register_service.register(credentials, request)
    return ResponseSchema(detail=ResponseStatus.SUCCESS.name)


@register_router.get(
    "/verify/{token}",
    summary=RegisterApiSummaryDocs.GET_VERIFY,
    response_model=ResponseSchema,
    response_model_exclude_none=True
)
async def verify_user(token: str):
    await register_service.verify_account(token)
    return RedirectResponse("http://localhost:4200/") # login page
