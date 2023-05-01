from typing import TypedDict

__all__ = ("MessageInfo",)


class MessageInfo(TypedDict):
    username: str
    message: str
    sent_at: int
