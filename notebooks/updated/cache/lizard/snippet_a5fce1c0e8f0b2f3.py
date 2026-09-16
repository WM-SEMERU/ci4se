def global_get(self, key):
    key = self.pack(key)
    r = self.sql('global_get', key).fetchone()
    if r is None:
        raise KeyError('Not set')
    return self.unpack(r[0])