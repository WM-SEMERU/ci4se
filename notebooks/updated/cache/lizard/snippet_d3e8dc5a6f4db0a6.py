def poll(self, timeout=None):
    _vv and IOLOG.debug('%r.poll(%r)', self, timeout)
    self._generation += 1
    return self._poll(timeout)