def maybe_parse_user_type(t):
    is_type = isinstance(t, type)
    is_preserved = isinstance(t, type) and issubclass(t,
        _preserved_iterable_types)
    is_string = isinstance(t, string_types)
    is_iterable = isinstance(t, Iterable)
    if is_preserved:
        return [t]
    elif is_string:
        return [t]
    elif is_type and not is_iterable:
        return [t]
    elif is_iterable:
        ts = t
        return tuple(e for t in ts for e in maybe_parse_user_type(t))
    else:
        raise TypeError(
            'Type specifications must be types or strings. Input: {}'.format(t)
            )