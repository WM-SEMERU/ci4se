def sametype(func):

    @functools.wraps(func)
    def wrapper(self, other):
        if type(other) is not type(self):
            return NotImplemented
        return func(self, other)
    return wrapper