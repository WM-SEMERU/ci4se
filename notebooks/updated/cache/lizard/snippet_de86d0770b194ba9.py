def deallocate(self, buf):
    with self._lock:
        buf.truncate(0)
        self._free.append(buf)
        if self._waiters:
            self._waiters[0].notify()