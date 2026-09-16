def expireat(self, key, timestamp):
    return self._execute([b'EXPIREAT', key, ascii(timestamp).encode('ascii'
        )], 1)