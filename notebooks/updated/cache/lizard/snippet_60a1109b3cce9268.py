def hstrlen(self, name, key):
    with self.pipe as pipe:
        return pipe.hstrlen(self.redis_key(name), key)