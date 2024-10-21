from http import HTTPStatus

from aiohttp.web import Request, Response, json_response
from aiohttp_d42_validator import validate
from d42 import schema

from ..repositories import AuthRepository, ChatRepository
from ..schemas import AuthTokenSchema, NamespaceSchema, NewMessageSchema

__all__ = ("send_message",)

SegmentsSchema = schema.dict({
    "namespace": NamespaceSchema,
    "chat_id": NewMessageSchema["chat_id"],
})

HeadersSchema = schema.dict({
    "X-Auth-Token": AuthTokenSchema,
    ...: ...
})


@validate(segments=SegmentsSchema, headers=HeadersSchema, json=NewMessageSchema)
async def send_message(request: Request) -> Response:
    auth_repo: AuthRepository = request.app["auth_repo"]
    chat_repo: ChatRepository = request.app["chat_repo"]

    namespace = request.match_info.get("namespace")
    chat_id = request.match_info.get("chat_id")

    token = request.headers.get("X-Auth-Token")
    user_info, error = await auth_repo.get_user_info(namespace, token)
    if error:
        return json_response({"errors": [error]}, status=HTTPStatus.UNAUTHORIZED)

    payload = await request.json()
    message = payload.get("text")

    result, error = await chat_repo.send_message(namespace, chat_id, user_info["username"], message)
    if error:
        return json_response({"errors": [error]}, status=HTTPStatus.BAD_REQUEST)

    return json_response(result, status=HTTPStatus.OK)
