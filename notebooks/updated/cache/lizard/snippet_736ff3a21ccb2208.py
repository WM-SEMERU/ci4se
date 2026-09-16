def get_schemas(cls, schema_types=None, sort=True):
    result = filter(lambda x: not x.is_inline_array, cls._schemas.values())
    if schema_types:
        result = filter(lambda x: x.schema_type in schema_types, result)
    if sort:
        result = sorted(result, key=attrgetter('name'))
    return result