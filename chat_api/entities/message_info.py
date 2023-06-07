from typing import TypedDict

__all__ = ("MessageInfo",)


class MessageInfo(TypedDict):
    username: str
    text: str
    sent_at: int
    chat_id: str
