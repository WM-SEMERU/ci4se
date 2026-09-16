def invalidate(self):
    super(RedisTransport, self).invalidate()
    for server in self._servers:
        server['redis'].connection_pool.disconnect()
    return False