def nbytes_stored(self):
    m = getsize(self._store, self._path)
    if self._chunk_store is None:
        return m
    else:
        n = getsize(self._chunk_store, self._path)
        if m < 0 or n < 0:
            return -1
        else:
            return m + n