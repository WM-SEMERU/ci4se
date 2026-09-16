def smembers(self, key, *, encoding=_NOTSET):
    return self.execute(b'SMEMBERS', key, encoding=encoding)