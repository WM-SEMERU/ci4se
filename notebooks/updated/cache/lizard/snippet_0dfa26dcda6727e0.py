def _connect(self):
    if not statsd:
        return
    if hasattr(statsd, 'StatsClient'):
        self.connection = statsd.StatsClient(host=self.host, port=self.port
            ).pipeline()
    else:
        self.connection = statsd.Connection(host=self.host, port=self.port,
            sample_rate=1.0)