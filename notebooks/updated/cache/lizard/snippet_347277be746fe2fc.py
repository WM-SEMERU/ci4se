def is_bound(method):

    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        if not self._is_bound:
            raise ValueError('%r must be bound to call %s()' % (self,
                method.__name__))
        return method(self, *args, **kwargs)
    return wrapper