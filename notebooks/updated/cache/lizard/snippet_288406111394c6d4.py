def clear(self):
    self._wlock.acquire()
    try:
        self._mapping.clear()
        self._queue.clear()
    finally:
        self._wlock.release()