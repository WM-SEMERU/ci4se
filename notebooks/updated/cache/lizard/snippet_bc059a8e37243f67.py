def address(self):
    port = ''
    if self._port:
        port = ':{}'.format(self._port)
    return Address('{}/{}{}'.format(self.interface.ip.compressed, self.
        interface.exploded.split('/')[-1], port))