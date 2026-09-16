def _filehandle(self):
    if self._fh and self._has_file_rolled():
        try:
            self._fh.close()
        except Exception:
            pass
        self._fh = None
    if not self._fh:
        self._open_file(self.filename)
        if not self.opened_before:
            self.opened_before = True
            self._fh.seek(0, os.SEEK_END)
    return self._fh