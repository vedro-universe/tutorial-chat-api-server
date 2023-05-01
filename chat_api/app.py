from aiohttp import web
from aiohttp.web import Application

from .handlers import auth_login, auth_register, get_messages, healthcheck, send_message
from .repositories import AuthRepository, ChatRepository
from .utils import Registry

__all__ = ("create_app",)


async def create_app() -> Application:
    app = Application()

    registry = Registry(expire_after=3600 * 24)  # 1 day
    app["chat_repo"] = ChatRepository(registry)
    app["auth_repo"] = AuthRepository(registry)

    app.add_routes([
        web.post("/{namespace}/auth/register", auth_register),
        web.post("/{namespace}/auth/login", auth_login),
        web.post("/{namespace}/chats/{chat_id}/messages", send_message),
        web.get("/{namespace}/chats/{chat_id}/messages", get_messages),
        web.get("/healthcheck", healthcheck),
    ])

    return app
