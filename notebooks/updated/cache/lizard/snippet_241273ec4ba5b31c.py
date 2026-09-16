def absorb_args(self, func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        return func()
    return wrapper