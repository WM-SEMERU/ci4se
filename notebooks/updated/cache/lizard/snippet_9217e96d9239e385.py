def get_queue_system_lock(self, queue):
    key = self._key(LOCK_REDIS_KEY, queue)
    return Semaphore.get_system_lock(self.connection, key)