from datetime import datetime
from hashlib import sha1
from time import time
from uuid import uuid4

from niltype import Nil

from ..entities import TokenInfo, UserInfo
from ..utils import Registry
from .repository import MaybeResult, Repository

__all__ = ("AuthRepository",)


class AuthRepository(Repository):
    def __init__(self, registry: Registry) -> None:
        self._registry = registry

    async def register(self, namespace: str, username: str, password: str) -> MaybeResult[UserInfo]:
        user_key = f"{namespace}::{username}::user"
        maybe_user = await self._registry.get(user_key)
        if maybe_user is not Nil:
            return None, f"User '{username}' already exists"

        new_user = self._create_user(username, password)
        await self._registry.add(user_key, new_user)
        return new_user, None

    async def login(self, namespace: str, username: str, password: str) -> MaybeResult[TokenInfo]:
        user_key = f"{namespace}::{username}::user"
        maybe_user = await self._registry.get(user_key)
        if maybe_user is Nil:
            return None, f"User '{username}' does not exist"

        if maybe_user["password"] != password:
            return None, "Invalid password"

        token = self._create_token(maybe_user["username"])
        token_key = f"{namespace}::{token['token']}::token"
        await self._registry.add(token_key, token)

        return token, None

    async def get_user_info(self, namespace: str, token: str) -> MaybeResult[UserInfo]:
        token_key = f"{namespace}::{token}::token"
        maybe_token = await self._registry.get(token_key)
        if maybe_token is Nil:
            return None, "Invalid token"

        user_key = f"{namespace}::{maybe_token['username']}::user"
        maybe_user = await self._registry.get(user_key)
        if maybe_user is Nil:
            return None, "Invalid token"

        return maybe_user, None

    def _create_user(self, username: str, password: str) -> UserInfo:
        user_id = int(time() * 1000)
        return {
            "id": user_id,
            "username": username,
            "password": password,
        }

    def _create_token(self, username: str) -> TokenInfo:
        uuid = str(uuid4()).encode()
        token = sha1(uuid).hexdigest()
        created_at = int(datetime.utcnow().timestamp())
        return {
            "username": username,
            "token": token,
            "created_at": created_at,
        }
