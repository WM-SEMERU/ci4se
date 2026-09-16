def eager_partial(self, fn, *a, **kw):
    args, kwargs = self.prepare_callable(fn, partial=True)
    args += a
    kwargs.update(kw)
    return functools.partial(fn, *args, **kwargs)