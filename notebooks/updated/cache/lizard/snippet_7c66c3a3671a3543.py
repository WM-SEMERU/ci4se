def export(string, template=None, **extra):

    def wrapped(f):
        endpoint = (f.__module__ + '.' + f.__name__)[16:]
        if template is not None:
            old_f = f

            def f(**kwargs):
                rv = old_f(**kwargs)
                if not isinstance(rv, Response):
                    rv = TemplateResponse(template, **rv or {})
                return rv
            f.__name__ = old_f.__name__
            f.__doc__ = old_f.__doc__
        exported_views[endpoint] = f, string, extra
        return f
    return wrapped