from http import HTTPStatus

import vedro
from contexts import registered_user
from interfaces import ChatApi
from schemas import AuthTokenSchema


class Scenario(vedro.Scenario):
    subject = "login as registered user"

    def given_user(self):
        self.user = registered_user()

    def when_user_logs_in(self):
        self.response = ChatApi().login(self.user)

    def then_it_should_return_success_response(self):
        assert self.response.status_code == HTTPStatus.OK, self.response.json()

    def and_it_should_return_created_token(self):
        assert self.response.json() == AuthTokenSchema % {
            "username": self.user["username"]
        }
