from d42 import schema

from .user import NewUserSchema

NewMessageSchema = schema.dict({
    "text": schema.str.len(1, 140),
    "chat_id": schema.str.len(1, 32),
})

MessageSchema = NewMessageSchema + schema.dict({
    "username": NewUserSchema["username"],
    "sent_at": schema.int.min(1)
})
