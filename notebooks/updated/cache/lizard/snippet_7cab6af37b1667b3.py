def close(self, destroy=False, sync=False, timeout=None):
    _SharedPV.close(self, destroy)
    if sync:
        _sync()
        self._disconnected.Wait(timeout=timeout)