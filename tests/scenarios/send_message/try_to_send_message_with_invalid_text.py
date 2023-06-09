from http import HTTPStatus

import vedro
from contexts import logined_user
from d42 import fake
from interfaces import ChatApi
from schemas import ErrorSchema, NewMessageSchema
from vedro import params


class Scenario(vedro.Scenario):
    subject = "try to send message with invalid text (len={text_len})"

    @params(0)
    @params(141)
    def __init__(self, text_len):
        self.text = "x" * text_len

    def given_user_token(self):
        self.token = logined_user()

    def given_message(self):
        self.message = fake(NewMessageSchema) | {"text": self.text}

    def when_user_sends_message(self):
        self.response = ChatApi().send(self.message, self.token["token"])

    def then_it_should_return_failure_response(self):
        assert self.response.status_code == HTTPStatus.BAD_REQUEST

    def and_then_it_should_return_error(self):
        assert self.response.json() == ErrorSchema
