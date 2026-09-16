def hide(*keys):

    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            g.hide_request_fields = keys
            g.hide_response_fields = keys
            return func(*args, **kwargs)
        return wrapper
    return decorator