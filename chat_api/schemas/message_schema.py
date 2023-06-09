from d42 import schema

__all__ = ("NewMessageSchema",)

NewMessageSchema = schema.dict({
    "text": schema.str.len(1, 140),
    "chat_id": schema.str.len(3, 32)
})
