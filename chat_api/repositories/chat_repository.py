from datetime import datetime
from typing import List

from niltype import Nil

from ..entities import MessageInfo
from ..utils import Registry
from .repository import MaybeResult, Repository

__all__ = ("ChatRepository",)


class ChatRepository(Repository):
    def __init__(self, registry: Registry) -> None:
        self._registry = registry

    async def send_message(self, namespace: str, chat_id: str, username: str, text: str) -> MaybeResult[MessageInfo]:
        message = self._create_message(username, text, chat_id)

        messages_key = f"{namespace}::{chat_id}::messages"
        maybe_messages = await self._registry.get(messages_key)
        if maybe_messages is Nil:
            messages = [message]
        else:
            messages = [message] + maybe_messages

        await self._registry.add(messages_key, messages)
        return message, None

    async def get_messages(self, namespace: str, chat_id: str) -> MaybeResult[List[MessageInfo]]:
        messages_key = f"{namespace}::{chat_id}::messages"
        maybe_messages = await self._registry.get(messages_key)
        if maybe_messages is Nil:
            return [], None
        return maybe_messages, None

    def _create_message(self, username: str, text: str, chat_id: str) -> MessageInfo:
        sent_at = int(datetime.utcnow().timestamp())
        return {
            "chat_id": chat_id,
            "username": username,
            "text": text,
            "sent_at": sent_at,
        }
