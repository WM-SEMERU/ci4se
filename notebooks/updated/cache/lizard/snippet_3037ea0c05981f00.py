def set_str_param(params, name, value):
    if value is None:
        return
    if isinstance(value, str):
        params[name] = value
    elif isinstance(value, unicode):
        params[name] = value.encode('utf-8')
    else:
        raise ValueError("Parameter '%s' must be a string or None, got %r." %
            (name, value))