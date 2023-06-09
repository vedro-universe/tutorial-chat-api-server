from http import HTTPStatus

import vedro
from contexts import logged_in_user, sent_message
from d42 import schema
from interfaces import ChatApi
from schemas import MessageSchema


class Scenario(vedro.Scenario):
    subject = "get message"

    def given_user_token(self):
        self.token = logged_in_user()

    def given_sent_message(self):
        self.message = sent_message(self.token["token"])

    def when_user_retrieves_messages(self):
        self.response = ChatApi().get_messages(self.message["chat_id"], self.token["token"])

    def then_it_should_return_success_response(self):
        assert self.response.status_code == HTTPStatus.OK

    def and_it_should_return_messages(self):
        assert self.response.json() == schema.list([
            MessageSchema % {
                "username": self.token["username"],
                "text": self.message["text"],
                "chat_id": self.message["chat_id"]
            }
        ])
