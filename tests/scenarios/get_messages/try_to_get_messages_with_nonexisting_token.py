from http import HTTPStatus

import vedro
from d42 import fake
from interfaces import ChatApi
from schemas import AuthTokenSchema, ErrorSchema, NewMessageSchema


class Scenario(vedro.Scenario):
    subject = "try to get messages with non-existing token"

    def given_user_token(self):
        self.token = fake(AuthTokenSchema["token"])

    def given_chat_id(self):
        self.chat_id = fake(NewMessageSchema["chat_id"])

    def when_user_retrieves_messages(self):
        self.response = ChatApi().get_messages(self.chat_id, self.token)

    def then_it_should_return_failure_response(self):
        assert self.response.status_code == HTTPStatus.UNAUTHORIZED

    def and_then_it_should_return_error(self):
        assert self.response.json() == ErrorSchema
