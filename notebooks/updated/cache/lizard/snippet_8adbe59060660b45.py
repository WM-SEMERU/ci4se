def _wrap_method(name):
    method = getattr(datetime.datetime, name)

    @functools.wraps(method, ('__name__', '__doc__'), ())
    def wrapper(self, *args, **kw):
        r = method(self, *args, **kw)
        if isinstance(r, datetime.datetime) and not isinstance(r, type(self)):
            r = type(self)(r)
        return r
    setattr(datetime_tz, name, wrapper)