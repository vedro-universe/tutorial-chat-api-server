from http import HTTPStatus

import vedro
from contexts import logined_user, sent_message
from d42 import fake, schema
from interfaces import ChatApi
from schemas import MessageSchema, NewMessageSchema


class Scenario(vedro.Scenario):
    subject = "get messages"

    def given_user_message(self):
        self.user1_token = logined_user()
        self.user1_message = sent_message(self.user1_token["token"])

    def given_another_user_message(self):
        self.user2_token = logined_user()
        message = fake(NewMessageSchema % {
            "chat_id": self.user1_message["chat_id"]
        })
        self.user2_message = sent_message(self.user2_token["token"], message)

    def when_user_retrieves_messages(self):
        self.response = ChatApi().get_messages(self.user1_message["chat_id"], self.user1_token["token"])

    def then_it_should_return_success_response(self):
        assert self.response.status_code == HTTPStatus.OK

    def and_it_should_return_messages(self):
        assert self.response.json() == schema.list([
            MessageSchema % {
                "username": self.user2_token["username"],
                "text": self.user2_message["text"],
                "chat_id": self.user2_message["chat_id"]
            },
            MessageSchema % {
                "username": self.user1_token["username"],
                "text": self.user1_message["text"],
                "chat_id": self.user1_message["chat_id"]
            }
        ])
