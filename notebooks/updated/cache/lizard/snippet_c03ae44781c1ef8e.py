def zremrangebyscore(self, name, min, max):
    with self.pipe as pipe:
        return pipe.zremrangebyscore(self.redis_key(name), min, max)