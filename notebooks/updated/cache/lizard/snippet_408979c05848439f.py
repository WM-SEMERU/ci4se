def native(self):
    if self.contents is None:
        return None
    if self._native is None:
        self._native = int_from_bytes(self._merge_chunks())
    return self._native