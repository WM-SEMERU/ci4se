def load_raw(cls, model_fn, schema, *args, **kwargs):
    c = cls(*args, **kwargs)
    c.schema = schema.copy(schema_only=True)
    c._model_data = open(model_fn, 'rb').read()
    return c