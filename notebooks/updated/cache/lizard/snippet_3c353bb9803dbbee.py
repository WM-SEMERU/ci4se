def close(self):
    self._lock.acquire()
    try:
        self._closed = True
        self._cv.notifyAll()
        if self._event is not None:
            self._event.set()
    finally:
        self._lock.release()