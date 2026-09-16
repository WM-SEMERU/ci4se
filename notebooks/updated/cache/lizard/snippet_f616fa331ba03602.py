def setrange(self, name, offset, value):
    with self.pipe as pipe:
        return pipe.setrange(self.redis_key(name), offset, value)