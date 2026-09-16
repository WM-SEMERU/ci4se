def maxLength(self):
    value = self._schema.get('maxLength', None)
    if value is None:
        return
    if not isinstance(value, int):
        raise SchemaError('maxLength value {0!r} is not an integer'.format(
            value))
    return value