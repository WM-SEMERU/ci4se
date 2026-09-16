def encode(self, value):
    if isinstance(value, bytes):
        return value
    elif isinstance(value, int):
        value = b(str(value))
    elif isinstance(value, float):
        value = b(repr(value))
    elif not isinstance(value, str):
        value = str(value)
    if isinstance(value, str):
        value = value.encode()
    return value