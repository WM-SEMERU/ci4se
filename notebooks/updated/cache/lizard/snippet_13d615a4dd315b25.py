def validate_bool_kwarg(value, arg_name):
    if not (is_bool(value) or value is None):
        raise ValueError(
            'For argument "{arg}" expected type bool, received type {typ}.'
            .format(arg=arg_name, typ=type(value).__name__))
    return value