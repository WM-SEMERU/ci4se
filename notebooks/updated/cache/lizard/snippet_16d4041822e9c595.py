def buffer(self):
    return buffer(self._region.buffer(), self._ofs, self._size)