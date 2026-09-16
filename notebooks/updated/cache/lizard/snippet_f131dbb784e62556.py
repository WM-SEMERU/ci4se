def lock(self, block=True):
    self._locked = True
    return self._lock.acquire(block)