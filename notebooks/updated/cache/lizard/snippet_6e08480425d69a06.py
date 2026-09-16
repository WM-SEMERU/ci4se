def join(self, timeout=None):
    t0 = time.time()
    self._ioloop_manager.join(timeout=timeout)
    if timeout:
        self._stopped.wait(timeout - (time.time() - t0))