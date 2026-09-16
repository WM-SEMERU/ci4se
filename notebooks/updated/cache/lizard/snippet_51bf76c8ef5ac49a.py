def fail_to(future):
    assert is_future(future), 'you forgot to pass a future'

    def decorator(f):

        @wraps(f)
        def new_f(*args, **kwargs):
            try:
                return f(*args, **kwargs)
            except Exception:
                future.set_exc_info(sys.exc_info())
        return new_f
    return decorator