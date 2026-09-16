def write(self, data):
    assert isinstance(data, unicode)
    if self.closed:
        raise IOError('Write on closed I/O object')
    if data:
        self.buf.append(data)