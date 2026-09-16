def seek(self, offset, whence=0):
    self.flush()
    if whence == self.SEEK_SET:
        self._realpos = self._pos = offset
    elif whence == self.SEEK_CUR:
        self._pos += offset
        self._realpos = self._pos
    else:
        self._realpos = self._pos = self._get_size() + offset
    self._rbuffer = bytes()