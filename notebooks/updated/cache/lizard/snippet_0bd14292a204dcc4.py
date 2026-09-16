def wrap_name_to_id(func_, *args, **kwargs):
    assert isinstance(args[0], dict)
    args[0][PRIMARY_KEY] = args[0].get(PRIMARY_FIELD, '')
    return func_(*args, **kwargs)