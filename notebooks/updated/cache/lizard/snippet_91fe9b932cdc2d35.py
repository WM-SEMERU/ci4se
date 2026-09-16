def python_2_format_compatible(method):
    if six.PY3:
        return method

    def wrapper(self, format_spec):
        formatted = method(self, format_spec)
        if isinstance(format_spec, str):
            return formatted.encode('utf-8')
        return formatted
    return wrapper