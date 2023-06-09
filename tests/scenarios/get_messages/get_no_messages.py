from http import HTTPStatus

import vedro
from contexts import logined_user
from d42 import fake, schema
from interfaces import ChatApi
from schemas import NewMessageSchema


class Scenario(vedro.Scenario):
    subject = "get no messages"

    def given_user_token(self):
        self.token = logined_user()

    def given_chat_id(self):
        self.chat_id = fake(NewMessageSchema["chat_id"])

    def when_user_retrieves_messages(self):
        self.response = ChatApi().get_messages(self.chat_id, self.token["token"])

    def then_it_should_return_success_response(self):
        assert self.response.status_code == HTTPStatus.OK

    def and_it_should_return_messages(self):
        assert self.response.json() == schema.list([])
