def read(self, size=None):
    data = self.rfile.read(size)
    self.bytes_read += len(data)
    self._check_length()
    return data