def close(self):
    if self._mode in _allowed_write and self._valid is None:
        self._finalize_write()
    result = self._fp.close()
    self._closed = True
    return result