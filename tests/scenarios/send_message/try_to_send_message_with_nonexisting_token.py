from http import HTTPStatus

import vedro
from d42 import fake
from interfaces import ChatApi
from schemas import AuthTokenSchema, ErrorSchema, NewMessageSchema


class Scenario(vedro.Scenario):
    subject = "try to send message with incorrect token"

    def given_user_token(self):
        self.token = fake(AuthTokenSchema["token"])

    def given_message(self):
        self.message = fake(NewMessageSchema)

    def when_user_sends_message(self):
        self.response = ChatApi().send(self.message, self.token)

    def then_it_should_return_failure_response(self):
        assert self.response.status_code == HTTPStatus.UNAUTHORIZED

    def and_then_it_should_return_error(self):
        assert self.response.json() == ErrorSchema
