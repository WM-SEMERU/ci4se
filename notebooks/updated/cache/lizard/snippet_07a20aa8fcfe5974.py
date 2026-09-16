def fields(self):
    result = self._get_key_values('fields')
    for key, value in result.items():
        if not isinstance(value, list):
            result[key] = [value]
    for key, value in result.items():
        schema = get_schema_from_type(key)
        for obj in value:
            if obj not in schema._declared_fields:
                raise InvalidField('{} has no attribute {}'.format(schema.
                    __name__, obj))
    return result