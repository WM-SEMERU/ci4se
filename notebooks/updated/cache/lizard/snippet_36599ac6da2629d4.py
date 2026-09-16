def tell(self):
    self._check_open_file()
    if self._flushes_after_tell():
        self.flush()
    if not self._append:
        return self._io.tell()
    if self._read_whence:
        write_seek = self._io.tell()
        self._io.seek(self._read_seek, self._read_whence)
        self._read_seek = self._io.tell()
        self._read_whence = 0
        self._io.seek(write_seek)
    return self._read_seek