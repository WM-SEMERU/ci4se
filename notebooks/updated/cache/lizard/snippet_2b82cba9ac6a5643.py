def boolean(value):
    if isinstance(value, bool):
        return value
    if value == '':
        return False
    return strtobool(value)