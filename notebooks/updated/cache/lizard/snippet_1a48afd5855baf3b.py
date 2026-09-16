def lrem(self, key, count, value):
    if not isinstance(count, int):
        raise TypeError('count argument must be int')
    return self.execute(b'LREM', key, count, value)