def call(self, func, *args, **kwargs):
    for timer in self:
        with timer:
            func(*args, **kwargs)
    return self