def get_known_subqueues(self):
    if not self.has_subqueues:
        return set()
    return set(context.connections.redis.smembers(self.
        redis_key_known_subqueues))