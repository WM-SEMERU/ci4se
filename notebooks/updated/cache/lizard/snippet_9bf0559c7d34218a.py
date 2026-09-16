def maximum(self):
    value = self._schema.get('maximum', None)
    if value is None:
        return
    if not isinstance(value, NUMERIC_TYPES):
        raise SchemaError('maximum value {0!r} is not a numeric type'.
            format(value))
    return value