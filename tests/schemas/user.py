from string import ascii_lowercase

from d42 import schema

NewUserSchema = schema.dict({
    "username": schema.str.alphabet(ascii_lowercase).len(3, 12),
    "password": schema.str.len(6, ...),
})
