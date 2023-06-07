import httpx
import vedro
from config import Config
from httpx import Response


class ChatApi(vedro.Interface):
    def __init__(self, api_url: str = Config.Api.URL) -> None:
        self.api_url = api_url

    def register(self, user: dict[str, str]) -> Response:
        response = httpx.post(f"{self.api_url}/auth/register", json={
            "username": user["username"],
            "password": user["password"]
        })
        response.body = response.json()
        return response

    def login(self, user: dict[str, str]) -> Response:
        response = httpx.post(f"{self.api_url}/auth/login", json={
            "username": user["username"],
            "password": user["password"]
        })
        response.body = response.json()
        return response

    def send(self, message: dict[str, str], token: str) -> Response:
        headers = {"Authorization": token}
        payload = {
            "text": message["text"],
            "chat_id": message["chat_id"]
        }
        response = httpx.post(f"{self.api_url}/chats/{message['chat_id']}/messages", json=payload, headers=headers)
        response.body = response.json()
        return response

    def retrieve_messages(self, chat_id: str, token: str) -> Response:
        headers = {"Authorization": token}
        response = httpx.get(f"{self.api_url}/chats/{chat_id}/messages", headers=headers)
        response.body = response.json()
        return response
