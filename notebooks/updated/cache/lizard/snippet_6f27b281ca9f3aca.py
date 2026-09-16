def set_bool_param(params, name, value):
    if value is None:
        return
    if value is True:
        params[name] = 'true'
    elif value is False:
        params[name] = 'false'
    else:
        raise ValueError("Parameter '%s' must be boolean or None, got %r." %
            (name, value))