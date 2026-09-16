def incrby(self, key, increment):
    return self._execute([b'INCRBY', key, ascii(increment)])