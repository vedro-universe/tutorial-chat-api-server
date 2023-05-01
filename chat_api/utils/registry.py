from time import monotonic
from typing import Any, Dict, Tuple

from niltype import Nil, Nilable

__all__ = ("Registry",)


class Registry:
    def __init__(self, expire_after: int) -> None:
        self._expire_after = expire_after
        self._store: Dict[str, Tuple[Any, float]] = {}

    async def add(self, key: str, value: Any) -> None:
        expire_at = monotonic() + self._expire_after
        self._store[key] = (value, expire_at)
        await self._invalidate_expired()

    async def get(self, key: str) -> Nilable[Any]:
        maybe_value = self._store.get(key, Nil)
        if maybe_value is Nil:
            return Nil

        value, expire_at = maybe_value
        if monotonic() > expire_at:
            await self.remove(key)
            return Nil

        return value

    async def remove(self, key: str) -> None:
        try:
            del self._store[key]
        except KeyError:
            pass

    async def _invalidate_expired(self) -> None:
        keys = list(self._store.keys())
        for key in keys:
            await self.get(key)
