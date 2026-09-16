def routes_register(app, handler, *paths, methods=None, router=None, name=None
    ):
    if router is None:
        router = app.router
    handler = to_coroutine(handler)
    resources = []
    for path in paths:
        if isinstance(path, type) and issubclass(path, BaseException):
            app._error_handlers[path] = handler
            continue
        name = str(name or '')
        rname, rnum = name, 2
        while rname in router:
            rname = '%s%d' % (name, rnum)
            rnum += 1
        path = parse(path)
        if isinstance(path, RETYPE):
            resource = RawReResource(path, name=rname)
            router.register_resource(resource)
        else:
            resource = router.add_resource(path, name=rname)
        for method in (methods or [METH_ANY]):
            method = method.upper()
            resource.add_route(method, handler)
        resources.append(resource)
    return resources