def connection_made(self, transport):
    self.transport = transport
    if self._proxy is None:
        peername = transport.get_extra_info('peername')
        self._remote_address = NetAddress(peername[0], peername[1])
    self._task = spawn_sync(self._process_messages(), loop=self.loop)