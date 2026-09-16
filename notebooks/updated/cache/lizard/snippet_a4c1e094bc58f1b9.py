def buttonUp(self, button=mouse.LEFT):
    self._lock.acquire()
    mouse.release(button)
    self._lock.release()