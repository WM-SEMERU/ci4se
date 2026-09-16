def get_resolver(order=None, options=None, modules=None):
    if not known_resolvers:
        from . import resolvers as carmen_resolvers
        modules = [carmen_resolvers] + (modules or [])
        for module in modules:
            for loader, name, _ in pkgutil.iter_modules(module.__path__):
                full_name = module.__name__ + '.' + name
                loader.find_module(full_name).load_module(full_name)
    if order is None:
        order = 'place', 'geocode', 'profile'
    else:
        order = tuple(order)
    if options is None:
        options = {}
    resolvers = []
    for resolver_name in order:
        if resolver_name not in known_resolvers:
            raise ValueError('unknown resolver name "%s"' % resolver_name)
        resolvers.append((resolver_name, known_resolvers[resolver_name](**
            options.get(resolver_name, {}))))
    return ResolverCollection(resolvers)