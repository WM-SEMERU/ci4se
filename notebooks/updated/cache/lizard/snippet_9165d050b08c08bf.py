def render_as_json(func):
    if inspect.isclass(func):
        setattr(func, '_renderer', json_renderer)
        return func
    else:

        @functools.wraps(func)
        def decorated_view(*args, **kwargs):
            data = func(*args, **kwargs)
            return _build_response(data, jsonify)
        return decorated_view