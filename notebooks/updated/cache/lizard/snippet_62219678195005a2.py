def from_view(cls, view, *methods, name=None):
    docs = getattr(view, '__doc__', None)
    view = to_coroutine(view)
    methods = methods or ['GET']
    if METH_ANY in methods:
        methods = METH_ALL

    def proxy(self, *args, **kwargs):
        return view(*args, **kwargs)
    params = {m.lower(): proxy for m in methods}
    params['methods'] = methods
    if docs:
        params['__doc__'] = docs
    return type(name or view.__name__, (cls,), params)