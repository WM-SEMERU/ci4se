def stop(self):
    if not self._dead:
        self._killed = True
        self._cancelled.set()
        self._busy_sem.release()
        self.join()
        if not self._ready_sem.acquire(False):
            warning('ISOTP Timer thread may not have stopped correctly')