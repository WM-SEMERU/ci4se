def set(self, start, stop, length=None, units='bytes'):
    assert is_byte_range_valid(start, stop, length), 'Bad range provided'
    self._units = units
    self._start = start
    self._stop = stop
    self._length = length
    if self.on_update is not None:
        self.on_update(self)