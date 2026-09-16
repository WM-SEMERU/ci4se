def _connect(self, servers):
    self._do_connect(servers.split(' '))
    self._verify_connection(verbose=True)