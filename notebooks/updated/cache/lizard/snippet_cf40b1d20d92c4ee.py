def result_invoke(action):
    r

    def wrap(func):

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            action(result)
            return result
        return wrapper
    return wrap