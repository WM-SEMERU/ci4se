def data(self, value):
    if not value:
        value = b''
    if len(value) > self.SIZE:
        raise ValueError('The maximum tag size is {0}'.format(self.SIZE))
    self._data = value
    while len(self._data) < self.SIZE:
        self._data += b'\x00'