def setup(hosts, default_keyspace, consistency=ConsistencyLevel.ONE,
    lazy_connect=False, retry_connect=False, **kwargs):
    global cluster, session, default_consistency_level, lazy_connect_args
    if 'username' in kwargs or 'password' in kwargs:
        raise CQLEngineException(
            "Username & Password are now handled by using the native driver's auth_provider"
            )
    if not default_keyspace:
        raise UndefinedKeyspaceException()
    from cqlengine import models
    models.DEFAULT_KEYSPACE = default_keyspace
    default_consistency_level = consistency
    if lazy_connect:
        kwargs['default_keyspace'] = default_keyspace
        kwargs['consistency'] = consistency
        kwargs['lazy_connect'] = False
        kwargs['retry_connect'] = retry_connect
        lazy_connect_args = hosts, kwargs
        return
    cluster = Cluster(hosts, **kwargs)
    try:
        session = cluster.connect()
    except NoHostAvailable:
        if retry_connect:
            kwargs['default_keyspace'] = default_keyspace
            kwargs['consistency'] = consistency
            kwargs['lazy_connect'] = False
            kwargs['retry_connect'] = retry_connect
            lazy_connect_args = hosts, kwargs
        raise
    session.row_factory = dict_factory