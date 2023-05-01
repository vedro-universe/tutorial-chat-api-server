from typing import TypedDict

__all__ = ("UserInfo",)


class UserInfo(TypedDict):
    id: int
    username: str
    password: str
