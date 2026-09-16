def set(self, index, value=None, dir=False, ttl=None, expiration=None):
    if bool(dir) is (value is not None):
        raise TypeError('Choose one of value or directory')
    if (ttl is not None) is (expiration is None):
        raise TypeError('Both of ttl and expiration required')
    self.value = value
    if self.dir != dir:
        self.dir = dir
        self.nodes = {} if dir else None
    self.ttl = ttl
    self.expiration = expiration
    self.modified_index = index