def acquire_lock(self):
    if self.options.for_global_scope().lock:
        if not self._lock.acquired:
            self._lock.acquire()