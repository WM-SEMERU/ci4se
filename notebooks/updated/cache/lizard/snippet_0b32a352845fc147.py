def to_python(self, value):
    if not value:
        return {}
    elif isinstance(value, six.string_types):
        res = loads(value)
        assert isinstance(res, dict)
        return JSONDict(**res)
    else:
        return value