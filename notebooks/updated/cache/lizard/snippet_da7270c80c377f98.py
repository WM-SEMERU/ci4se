def to_binary(s, encoding='utf8'):
    if PY3:
        return s if isinstance(s, binary_type) else binary_type(s, encoding
            =encoding)
    return binary_type(s)