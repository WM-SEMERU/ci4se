def _do_connect(self):
    _, self._protocol = yield from self._loop.create_connection(lambda :
        SnapcastProtocol(self._callbacks), self._host, self._port)