from http import HTTPStatus

from aiohttp.web import Request, Response, json_response

from ..repositories import AuthRepository, ChatRepository

__all__ = ("send_message",)


async def send_message(request: Request) -> Response:
    auth_repo: AuthRepository = request.app["auth_repo"]
    chat_repo: ChatRepository = request.app["chat_repo"]

    namespace = request.match_info.get("namespace")
    chat_id = request.match_info.get("chat_id")

    token = request.headers.get("Authorization")
    if not token:
        return json_response({"error": "Token is required"}, status=HTTPStatus.UNAUTHORIZED)

    user_info, error = await auth_repo.get_user_info(namespace, token)
    if error:
        return json_response({"error": error}, status=HTTPStatus.UNAUTHORIZED)

    payload = await request.json()
    message = payload.get("message")

    result, error = await chat_repo.send_message(namespace, chat_id, user_info["username"], message)
    if error:
        return json_response({"error": error}, status=HTTPStatus.BAD_REQUEST)

    return json_response(result, status=HTTPStatus.OK)
