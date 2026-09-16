def _apply(self, func, name, window=None, center=None, check_minp=None, **
    kwargs):

    def f(x, name=name, *args):
        x = self._shallow_copy(x)
        if isinstance(name, str):
            return getattr(x, name)(*args, **kwargs)
        return x.apply(name, *args, **kwargs)
    return self._groupby.apply(f)