def log_call(call_name):

    def decorator(f):

        @wraps(f)
        def wrapper(*args, **kw):
            instance = args[0]
            instance.logger.info(call_name, {'content': request.get_json()})
            return f(*args, **kw)
        return wrapper
    return decorator