from d42 import schema

ErrorSchema = schema.dict({
    "errors": schema.list(schema.str.len(1, ...))
})
