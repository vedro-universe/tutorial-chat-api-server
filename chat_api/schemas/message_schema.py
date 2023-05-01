from d42 import schema

__all__ = ("NewMessageSchema",)

NewMessageSchema = schema.dict({
    "message": schema.str.len(1, 140),
})
