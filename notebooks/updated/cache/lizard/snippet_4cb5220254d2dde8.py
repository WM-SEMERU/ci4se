def sismember(self, name, value):
    with self.pipe as pipe:
        return pipe.sismember(self.redis_key(name), self.valueparse.encode(
            value))