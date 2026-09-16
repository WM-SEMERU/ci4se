def save(self):
    result = yield gen.Task(RedisSession._redis_client.set, self._key, self
        .dumps())
    LOGGER.debug('Saved session %s (%r)', self.id, result)
    raise gen.Return(result)