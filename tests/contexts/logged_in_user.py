import vedro
from interfaces.chat_api import ChatApi

from .registered_user import registered_user


@vedro.context
def logged_in_user(user: dict[str, str] | None = None) -> dict[str, str | int]:
    if user is None:
        user = registered_user()
    response = ChatApi().login(user)
    response.raise_for_status()
    return response.json()
