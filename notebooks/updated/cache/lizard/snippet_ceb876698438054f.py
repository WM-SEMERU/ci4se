def str_to_bytes(value):
    if not isinstance(value, six.binary_type) and isinstance(value, six.
        string_types):
        return value.encode()
    return value