def maximumCanEqual(self):
    if self.maximum is None:
        raise SchemaError('maximumCanEqual requires presence of maximum')
    value = self._schema.get('maximumCanEqual', True)
    if value is not True and value is not False:
        raise SchemaError('maximumCanEqual value {0!r} is not a boolean'.
            format(value))
    return value