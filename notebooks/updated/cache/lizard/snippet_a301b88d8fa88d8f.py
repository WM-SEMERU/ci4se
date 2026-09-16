def read_bytes(self, num_bytes):
    buffer_size = len(self._buffer)
    if buffer_size > num_bytes:
        data, self._buffer = self._buffer[:num_bytes], self._buffer[num_bytes:]
    elif 0 < buffer_size <= num_bytes:
        data, self._buffer = self._buffer, bytearray()
    else:
        self._buffer += self.__read__(num_bytes)
        return self.read_bytes(num_bytes)
    return data