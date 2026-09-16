def connection_made(self, address):
    self._proxy = PickleProxy(self.loop, self)
    for d in self._proxy_deferreds:
        d.callback(self._proxy)