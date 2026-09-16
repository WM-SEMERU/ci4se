def read(self, size):
    if self._update_buffer and not self._updated_buffer and self.duration:
        self.update_buffer(self.duration * 1000 + 5000)
        self._updated_buffer = True
    if not self._buf or len(self._buf) != size:
        self._buf = ffi.new('char[]', size)
        self._view = ffi.buffer(self._buf, size)
    res = librtmp.RTMP_Read(self.client.rtmp, self._buf, size)
    if res < 0:
        raise IOError('Failed to read data')
    return self._view[:res]