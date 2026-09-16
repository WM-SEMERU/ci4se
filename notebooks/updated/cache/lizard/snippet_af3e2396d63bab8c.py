def read(self):
    val = self._fd.read()
    self._fd.seek(0)
    return int(val)