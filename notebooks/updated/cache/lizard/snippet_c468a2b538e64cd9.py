def _close_last(self):
    if self._rs:
        self._rs.close()
    self._rs = None
    if self._prep:
        self._prep.close()
    self._prep = None
    self._meta = None
    self._description = None