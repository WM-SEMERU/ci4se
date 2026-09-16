def _work(self):
    server = wsgi.Server(name=self._AGENT_BINARY, num_threads=CONF.AGENT.
        worker_count)
    server.start(application=_MetadataProxyHandler(), port=CONF.bind_port,
        host=CONF.bind_host)
    server.wait()