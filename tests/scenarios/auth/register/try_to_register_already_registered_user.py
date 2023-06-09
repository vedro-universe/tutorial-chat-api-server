from http import HTTPStatus

import vedro
from contexts import registered_user
from interfaces import ChatApi
from schemas import ErrorSchema


class Scenario(vedro.Scenario):
    subject = "try to register already registered user"

    def given_registered_user(self):
        self.user = registered_user()

    def when_guest_registers(self):
        self.response = ChatApi().register(self.user)

    def then_it_should_return_failure_response(self):
        assert self.response.status_code == HTTPStatus.BAD_REQUEST

    def and_then_it_should_return_error(self):
        assert self.response.json() == ErrorSchema
