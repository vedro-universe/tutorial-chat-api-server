from http import HTTPStatus

from aiohttp.web import Request, Response, json_response

__all__ = ("healthcheck",)


async def healthcheck(request: Request) -> Response:
    return json_response({"message": "OK"}, status=HTTPStatus.OK)
