async def create(cls, host, *args, **kwargs):
    loop = kwargs.pop('loop', None)
    resolver = kwargs.pop('resolver', Resolver(loop=loop))
    try:
        _host = await resolver.resolve(host)
        self = cls(_host, *args, **kwargs)
    except (ResolveError, ValueError) as e:
        log.error('%s:%s: Error at creating: %s' % (host, args[0], e))
        raise
    return self