from d42 import schema

from .user import NewUserSchema

AuthTokenSchema = schema.dict({
    "username": NewUserSchema["username"],
    "token": schema.str.alphabet("0123456789abcdef").len(40),
    "created_at": schema.int.min(0),
})
