from http import HTTPStatus

from aiohttp.web import Request, Response, json_response
from aiohttp_valera_validator import validate
from d42 import schema

from ..repositories import AuthRepository, ChatRepository
from ..schemas import AuthTokenSchema, NamespaceSchema, NewMessageSchema

__all__ = ("get_messages",)

SegmentsSchema = schema.dict({
    "namespace": NamespaceSchema,
    "chat_id": NewMessageSchema["chat_id"],
})

HeadersSchema = schema.dict({
    "Authorization": AuthTokenSchema,
    ...: ...
})


@validate(segments=SegmentsSchema, headers=HeadersSchema)
async def get_messages(request: Request) -> Response:
    auth_repo: AuthRepository = request.app["auth_repo"]
    chat_repo: ChatRepository = request.app["chat_repo"]

    namespace = request.match_info.get("namespace")
    chat_id = request.match_info.get("chat_id")

    token = request.headers.get("Authorization")
    _, error = await auth_repo.get_user_info(namespace, token)
    if error:
        return json_response({"errors": [error]}, status=HTTPStatus.UNAUTHORIZED)

    messages, error = await chat_repo.get_messages(namespace, chat_id)
    if error:
        return json_response({"errors": [error]}, status=HTTPStatus.BAD_REQUEST)

    return json_response(messages, status=HTTPStatus.OK)
