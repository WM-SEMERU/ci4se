def on_receive(self, broker):
    _vv and IOLOG.debug('%r.on_receive()', self)
    self._lock.acquire()
    try:
        self.receive_side.read(1)
        deferred = self._deferred
        self._deferred = []
    finally:
        self._lock.release()
    for func, args, kwargs in deferred:
        try:
            func(*args, **kwargs)
        except Exception:
            LOG.exception('defer() crashed: %r(*%r, **%r)', func, args, kwargs)
            self._broker.shutdown()