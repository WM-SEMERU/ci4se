async def create_pool(address, *, db=None, password=None, ssl=None,
    encoding=None, minsize=1, maxsize=10, parser=None, loop=None,
    create_connection_timeout=None, pool_cls=None, connection_cls=None):
    if pool_cls:
        assert issubclass(pool_cls, AbcPool
            ), 'pool_class does not meet the AbcPool contract'
        cls = pool_cls
    else:
        cls = ConnectionsPool
    if isinstance(address, str):
        address, options = parse_url(address)
        db = options.setdefault('db', db)
        password = options.setdefault('password', password)
        encoding = options.setdefault('encoding', encoding)
        create_connection_timeout = options.setdefault('timeout',
            create_connection_timeout)
        if 'ssl' in options:
            assert options['ssl'] or not options['ssl'] and not ssl, (
                'Conflicting ssl options are set', options['ssl'], ssl)
            ssl = ssl or options['ssl']
    pool = cls(address, db, password, encoding, minsize=minsize, maxsize=
        maxsize, ssl=ssl, parser=parser, create_connection_timeout=
        create_connection_timeout, connection_cls=connection_cls, loop=loop)
    try:
        await pool._fill_free(override_min=False)
    except Exception:
        pool.close()
        await pool.wait_closed()
        await pool.wait_closed()
        raise
    return pool