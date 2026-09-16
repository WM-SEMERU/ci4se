def flush(self, fsync=False):
    if self._handle is not None:
        self._handle.flush()
        if fsync:
            try:
                os.fsync(self._handle.fileno())
            except OSError:
                pass