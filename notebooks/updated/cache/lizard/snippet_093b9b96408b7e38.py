def read(self, size=None):
    if size is not None:
        read_size = min(size, self.__remaining_bytes)
    else:
        read_size = self.__remaining_bytes
    data = self.__stream.read(read_size)
    if read_size > 0 and not data:
        raise exceptions.StreamExhausted(
            'Not enough bytes in stream; expected %d, exhausted after %d' %
            (self.__max_bytes, self.__max_bytes - self.__remaining_bytes))
    self.__remaining_bytes -= len(data)
    return data