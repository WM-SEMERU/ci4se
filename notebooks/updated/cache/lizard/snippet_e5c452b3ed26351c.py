def schema(cls):
    root = '/'.join([API_ROOT, 'schemas', cls.__name__])
    schema = cls.GET(root)
    return schema