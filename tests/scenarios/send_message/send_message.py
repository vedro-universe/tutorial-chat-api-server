import vedro
from contexts import logged_in_user
from d42 import fake
from interfaces import ChatApi
from schemas import MessageSchema, NewMessageSchema


class Scenario(vedro.Scenario):
    subject = "send message"

    def given_user_token(self):
        self.token = logged_in_user()

    def given_message(self):
        self.message = fake(NewMessageSchema)

    def when_user_sends_message(self):
        self.response = ChatApi().send(self.message, self.token["token"])

    def then_it_should_return_success_response(self):
        assert self.response.status_code == 200

    def and_it_should_return_sent_message(self):
        assert self.response.json() == MessageSchema % {
            "username": self.token["username"],
            "text": self.message["text"],
        }
