def to_python(self, value):
    if isinstance(value, six.string_types):
        return value
    if value is None:
        return value
    return _unsigned_integer_to_hex_string(value)