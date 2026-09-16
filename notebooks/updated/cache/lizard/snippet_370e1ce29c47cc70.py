def _redis_connect(cls, settings):
    if 'tornadoredis' not in globals():
        import tornadoredis
    kwargs = {'host': settings.get('host', cls.REDIS_HOST), 'port':
        settings.get('port', cls.REDIS_PORT), 'selected_db': settings.get(
        'db', cls.REDIS_DB)}
    LOGGER.info('Connecting to %(host)s:%(port)s DB %(selected_db)s', kwargs)
    cls._redis_client = tornadoredis.Client(**kwargs)
    cls._redis_client.connect()