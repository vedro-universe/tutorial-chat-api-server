from http import HTTPStatus

import vedro
from d42 import fake
from interfaces import ChatApi
from schemas import ErrorSchema, NewUserSchema
from vedro import params


class Scenario(vedro.Scenario):
    subject = "try to register user with invalid {creds}"

    @params({"username": "x" * 2})
    @params({"username": "x" * 13})
    @params({"password": "x" * 5})
    def __init__(self, creds):
        self.creds = creds

    def given_new_user(self):
        self.user = fake(NewUserSchema) | self.creds

    def when_guest_registers(self):
        self.response = ChatApi().register(self.user)

    def then_it_should_return_failure_response(self):
        assert self.response.status_code == HTTPStatus.BAD_REQUEST

    def and_then_it_should_return_error(self):
        assert self.response.json() == ErrorSchema
