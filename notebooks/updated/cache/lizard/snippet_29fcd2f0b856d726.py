def resize(self, size):
    count = max(int(size), 0) - len(self)
    if count == 0:
        pass
    elif -count == len(self):
        self._value = bytes()
    elif count > 0:
        self._value += b'\x00' * count
    else:
        self._value = self._value[:count]
    size = len(self)
    self._bit_size = size * 8
    self._align_to_byte_size = size