from http import HTTPStatus

import vedro
from d42 import fake
from interfaces import ChatApi
from schemas import ErrorSchema, NewUserSchema


class Scenario(vedro.Scenario):
    subject = "try to login as non-existing user"

    def given_user(self):
        self.user = fake(NewUserSchema)

    def when_user_logs_in(self):
        self.response = ChatApi().login(self.user)

    def then_it_should_return_failure_response(self):
        assert self.response.status_code == HTTPStatus.BAD_REQUEST

    def and_then_it_should_return_error(self):
        assert self.response.json() == ErrorSchema
