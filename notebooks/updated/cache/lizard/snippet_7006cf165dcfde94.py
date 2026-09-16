def _write(self, str_buf):
    self._filehandle.write(str_buf)
    self._buf_size += len(str_buf)