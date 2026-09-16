def make_router(self, rule, method=None, handler=None, cls=None, name=None,
    **params):
    cls = cls or Router
    router = cls(rule, name=name, **params)
    for r in self.routes:
        if r._route == router._route:
            if isinstance(r, cls):
                router = r
                router._set_params(params)
                break
    if method and handler:
        if isinstance(method, tuple):
            for m in method:
                setattr(router, m, handler)
        else:
            setattr(router, method, handler)
    return router