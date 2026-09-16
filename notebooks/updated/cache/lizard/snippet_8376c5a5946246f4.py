def _unquote(self, value):
    if not value:
        raise SyntaxError
    if value[0] == value[-1] and value[0] in ('"', "'"):
        value = value[1:-1]
    return value