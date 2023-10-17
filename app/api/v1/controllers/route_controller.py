from fastapi import APIRouter, status, Depends

from app.api.v1.schema.schema import ResponseSchema
from app.model.route import RouteRequestDTO
from app.model.token import Token
from app.api.v1.docs.summary import RouteApiSummaryDocs
from app.security.jwt_provider import decodeJWT
from app.api.v1.schema.enum import ResponseStatus
from app.service.route_service import route_service

route_router = APIRouter(prefix="/routes", tags=["Routes"])


@route_router.get(
    "",
    summary=RouteApiSummaryDocs.GET_ALL_ROUTES,
    response_model=ResponseSchema,
    response_model_exclude_none=True
)
async def get_all_routes(token = Depends(decodeJWT)):
    result = await route_service.get_all_routes()
    return ResponseSchema(detail=ResponseStatus.SUCCESS.name, result=result)


@route_router.get(
    "/{routeId}",
    summary=RouteApiSummaryDocs.GET_ROUTE_DETAIL,
    response_model=ResponseSchema,
    response_model_exclude_none=True
)
async def get_route_by_id(routeId: int, token = Depends(decodeJWT)):
    result = await route_service.get_route_by_id(routeId)
    return ResponseSchema(detail=ResponseStatus.SUCCESS.name, result=result)


@route_router.post(
    "",
    summary=RouteApiSummaryDocs.POST_NEW_ROUTE,
    response_model=ResponseSchema,
    response_model_exclude_none=True,
    status_code=status.HTTP_201_CREATED
)
async def create_route(route_data: RouteRequestDTO, token = Depends(decodeJWT)):
    await route_service.create_route(route_data)
    return ResponseSchema(detail=ResponseStatus.SUCCESS.name)


@route_router.post(
    "/{routeId}/select",
    summary=RouteApiSummaryDocs.POST_SELECT_ROUTE,
    response_model=ResponseSchema,
    response_model_exclude_none=True
)
async def select_route(routeId: int, token: Token = Depends(decodeJWT)):
    await route_service.select_route(routeId, token.email)
    return ResponseSchema(detail=ResponseStatus.SUCCESS.name, result="Email has been sent to user.")


@route_router.delete(
    "/{routeId}",
    summary=RouteApiSummaryDocs.DELETE_ROUTE,
    response_model=ResponseSchema,
    response_model_exclude_none=True
)
async def delete_route(routeId: int, token = Depends(decodeJWT)):
    await route_service.delete_route(routeId)
    return ResponseSchema(detail=ResponseStatus.SUCCESS.name)


@route_router.patch(
    "/{routeId}",
    summary=RouteApiSummaryDocs.UPDATE_ROUTE,
    response_model=ResponseSchema,
    response_model_exclude_none=True
)
async def update_route(route_data: RouteRequestDTO, routeId: int, token = Depends(decodeJWT)):
    await route_service.update_route(routeId, route_data)
    return ResponseSchema(detail=ResponseStatus.SUCCESS.name)