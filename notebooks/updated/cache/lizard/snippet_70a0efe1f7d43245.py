def remove(self, header):
    key = header.lower()
    if key not in self._set:
        raise KeyError(header)
    self._set.remove(key)
    for idx, key in enumerate(self._headers):
        if key.lower() == header:
            del self._headers[idx]
            break
    if self.on_update is not None:
        self.on_update(self)