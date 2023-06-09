from http import HTTPStatus

import vedro
from contexts import logined_user
from interfaces import ChatApi
from schemas import ErrorSchema
from vedro import params


class Scenario(vedro.Scenario):
    subject = "try to get messages with invalid chat_id (len={chat_id_len})"

    @params(2)
    @params(33)
    def __init__(self, chat_id_len):
        self.chat_id = "x" * chat_id_len

    def given_user_token(self):
        self.token = logined_user()

    def when_user_retrieves_messages(self):
        self.response = ChatApi().get_messages(self.chat_id, self.token["token"])

    def then_it_should_return_failure_response(self):
        assert self.response.status_code == HTTPStatus.BAD_REQUEST

    def and_then_it_should_return_error(self):
        assert self.response.json() == ErrorSchema
