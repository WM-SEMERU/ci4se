def pattern(self):
    value = self._schema.get('pattern', None)
    if value is None:
        return
    try:
        return re.compile(value)
    except re.error as ex:
        raise SchemaError(
            'pattern value {0!r} is not a valid regular expression: {1}'.
            format(value, str(ex)))