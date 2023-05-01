from typing import TypedDict

__all__ = ("TokenInfo",)


class TokenInfo(TypedDict):
    username: str
    token: str
    created_at: int
