import vedro
from d42 import fake
from interfaces.chat_api import ChatApi
from schemas import NewUserSchema


@vedro.context
def registered_user(user: dict[str, str] | None = None) -> dict[str, str]:
    if user is None:
        user = fake(NewUserSchema)
    response = ChatApi().register(user)
    response.raise_for_status()
    return user
