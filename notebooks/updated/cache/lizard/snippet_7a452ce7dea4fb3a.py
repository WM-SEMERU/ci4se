def client(cls, config):
    if not hasattr(cls, '_client'):
        cls._client = statsd.StatsClient(config.STATSD_HOST, config.
            STATSD_PORT, config.STATSD_PREFIX)
    return cls._client