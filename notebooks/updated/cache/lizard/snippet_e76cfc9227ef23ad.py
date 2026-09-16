def persist(self, name):
    with self.pipe as pipe:
        return pipe.persist(self.redis_key(name))