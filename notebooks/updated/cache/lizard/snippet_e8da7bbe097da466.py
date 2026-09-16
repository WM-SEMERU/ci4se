def to_python(self, value):
    if value is None:
        return value
    if not isinstance(value, str):
        return value
    try:
        return json_decode(value)
    except Exception as err:
        raise ValidationError(repr(err))