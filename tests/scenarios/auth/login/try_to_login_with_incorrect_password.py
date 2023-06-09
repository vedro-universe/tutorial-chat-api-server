from http import HTTPStatus

import vedro
from contexts import registered_user
from d42 import fake
from interfaces import ChatApi
from schemas import ErrorSchema, NewUserSchema


class Scenario(vedro.Scenario):
    subject = "try to login with incorrect password"

    def given_user(self):
        self.user = registered_user()
        self.user["password"] = fake(NewUserSchema["password"])

    def when_user_logs_in(self):
        self.response = ChatApi().login(self.user)

    def then_it_should_return_failure_response(self):
        assert self.response.status_code == HTTPStatus.BAD_REQUEST

    def and_then_it_should_return_error(self):
        assert self.response.json() == ErrorSchema
