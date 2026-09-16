def reopen(self):
    self._read()
    self._close()
    try:
        self._open(self._path, skip_to_end=False)
        return True
    except OSError:
        return False