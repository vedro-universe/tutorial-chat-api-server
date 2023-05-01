from http import HTTPStatus

from aiohttp.web import Request, Response, json_response

from ..repositories import AuthRepository

__all__ = ("auth_register",)


async def auth_register(request: Request) -> Response:
    auth_repo: AuthRepository = request.app["auth_repo"]
    namespace = request.match_info.get("namespace")

    payload = await request.json()
    username = payload.get("username")
    password = payload.get("password")

    user_info, error = await auth_repo.register(namespace, username, password)
    if error:
        return json_response({"error": error}, status=HTTPStatus.BAD_REQUEST)

    return json_response(user_info, status=HTTPStatus.OK)
