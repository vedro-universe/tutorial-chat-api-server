import vedro
from d42 import fake
from interfaces.chat_api import ChatApi
from schemas import NewMessageSchema


@vedro.context
def sent_message(token, message: dict[str, str] = None) -> dict[str, str]:
    if message is None:
        message = fake(NewMessageSchema)
    response = ChatApi().send(message, token)
    response.raise_for_status()
    return response.json()
