def async_func(self, function):

    @wraps(function)
    def wrapped(*args, **kwargs):
        return self.submit(function, *args, **kwargs)
    return wrapped