def wrap_with_scope(func, scope_name=None):
    if scope_name is None:
        scope_name = get_current_scope().name
    return lambda *args, scope=scope_name, **kwargs: _call_with_scope(func,
        scope, args, kwargs)