def eager_partial_regardless(self, fn, *a, **kw):
    if self.has_annotations(fn):
        return self.eager_partial(fn, *a, **kw)
    return functools.partial(fn, *a, **kw)