from d42 import schema

__all__ = ("ChatIdSchema",)

ChatIdSchema = schema.str.len(1, 32)
