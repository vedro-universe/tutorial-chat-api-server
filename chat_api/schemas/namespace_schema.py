from d42 import schema

__all__ = ("NamespaceSchema",)

NamespaceSchema = schema.str.len(10)
