from typing import TypedDict

__all__ = ("UserInfo",)


class UserInfo(TypedDict):
    username: str
    password: str
