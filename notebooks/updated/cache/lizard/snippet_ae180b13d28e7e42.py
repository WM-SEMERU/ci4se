def _release(self):
    if self._in_use is None:
        return
    if not self._in_use.done():
        self._in_use.set_result(None)
    self._in_use = None
    if self._proxy is not None:
        self._proxy._detach()
        self._proxy = None
    self._pool._queue.put_nowait(self)