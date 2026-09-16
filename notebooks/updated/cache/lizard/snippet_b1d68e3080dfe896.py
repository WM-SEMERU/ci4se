def acquire(self):
    if not self._locked and all(w.cancelled() for w in self._waiters):
        self._locked = True
        return True
    fut = self._loop.create_future()
    self._waiters.append(fut)
    try:
        yield from fut
        self._locked = True
        return True
    except asyncio.CancelledError:
        if not self._locked:
            self._wake_up_first()
        raise
    finally:
        self._waiters.remove(fut)