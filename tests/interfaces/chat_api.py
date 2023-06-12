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
        payload = {
            "text": message["text"],
            "chat_id": message["chat_id"]
        }
        return self._request("POST", f"/chats/{message['chat_id']}/messages", json=payload, headers=headers)

    def get_messages(self, chat_id: str, token: str) -> Response:
        return self._request("GET", f"/chats/{chat_id}/messages", headers={"X-Auth-Token": token})
