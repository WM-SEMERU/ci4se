def _peek(self, size=-1):
    with self._seek_lock:
        seek = self._seek
    with handle_os_exceptions():
        return self._read_range(seek, seek + size)