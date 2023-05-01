from d42 import schema

__all__ = ("CredsSchema", "AuthTokenSchema",)

CredsSchema = schema.dict({
    "username": schema.str.len(3, 12),
    "password": schema.str.len(6, ...),
})

AuthTokenSchema = schema.str.alphabet("0123456789abcdef").len(40)
