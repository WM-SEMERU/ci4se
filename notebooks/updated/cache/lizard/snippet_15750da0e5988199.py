def hincrby(self, hashkey, attribute, increment=1):
    return self._hincrby(hashkey, attribute, 'HINCRBY', long, increment)