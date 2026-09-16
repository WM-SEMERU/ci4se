def activate(self, prefix=None, backend=None):
    if isinstance(prefix, compat.string_types):
        self.prefix = prefix
    if isinstance(backend, RmoqStorageBackend):
        self.backend = backend

    def activate(func):
        if isinstance(func, type):
            return self._decorate_class(func)

        def wrapper(*args, **kwargs):
            with self:
                return func(*args, **kwargs)
        return wrapper
    return activate