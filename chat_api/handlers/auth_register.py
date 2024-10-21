from http import HTTPStatus

from aiohttp.web import Request, Response, json_response
from aiohttp_d42_validator import validate
from d42 import schema

from ..repositories import AuthRepository
from ..schemas import CredsSchema, NamespaceSchema

__all__ = ("auth_register",)

SegmentsSchema = schema.dict({
    "namespace": NamespaceSchema,
})


@validate(segments=SegmentsSchema, json=CredsSchema)
async def auth_register(request: Request) -> Response:
    auth_repo: AuthRepository = request.app["auth_repo"]
    namespace = request.match_info.get("namespace")

    payload = await request.json()
    username = payload.get("username")
    password = payload.get("password")

    user_info, error = await auth_repo.register(namespace, username, password)
    if error:
        return json_response({"errors": [error]}, status=HTTPStatus.BAD_REQUEST)

    return json_response(user_info, status=HTTPStatus.OK)
