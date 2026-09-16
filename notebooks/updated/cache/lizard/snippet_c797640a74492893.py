def _read_mode_donone(self, size, kind):
    data = dict(kind=kind, length=size, data=self._read_fileng(size))
    return data