from http import HTTPStatus

import vedro
from d42 import fake
from interfaces import ChatApi
from schemas import NewUserSchema


class Scenario(vedro.Scenario):
    subject = "register new user"

    def given_new_user(self):
        self.user = fake(NewUserSchema)

    def when_guest_registers(self):
        self.response = ChatApi().register(self.user)

    def then_it_should_return_success_response(self):
        assert self.response.status_code == HTTPStatus.OK

    def and_then_it_should_return_created_user(self):
        assert self.response.json() == NewUserSchema % self.user
