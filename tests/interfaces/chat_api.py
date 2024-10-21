from config import Config
from vedro_httpx import Response, SyncHTTPInterface


class ChatApi(SyncHTTPInterface):
    def __init__(self, base_url: str = Config.Api.URL) -> None:
        super().__init__(base_url)

    def register(self, user: dict[str, str]) -> Response:
        return self._request("POST", "/auth/register", json={
            "username": user["username"],
            "password": user["password"]
        })

    def login(self, user: dict[str, str]) -> Response:
        return self._request("POST", "/auth/login", json={
            "username": user["username"],
            "password": user["password"]
        })

    def send(self, message: dict[str, str], token: str) -> Response:
        headers = {"X-Auth-Token": token}
        segments = {"chat_id": message['chat_id']}
        payload = {
            "text": message["text"],
            "chat_id": message["chat_id"]
        }
        return self._request("POST", "/chats/{chat_id}/messages",
                             json=payload, headers=headers, segments=segments)

    def get_messages(self, chat_id: str, token: str) -> Response:
        headers = {"X-Auth-Token": token}
        segments = {"chat_id": chat_id}
        return self._request("GET", "/chats/{chat_id}/messages",
                             headers=headers, segments=segments)
