def pluggable(method):

    def wrapped(self, *args, **kwargs):
        if hasattr(self, '_plugins'):
            return getattr(self._plugins[-1], method.__name__)(*args, **kwargs)
        else:
            return method(self, *args, **kwargs)
    wrapped.original = method
    return wrapped