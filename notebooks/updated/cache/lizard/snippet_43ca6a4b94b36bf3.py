def __sync(self):
    pad_length = _BLOCK_SIZE - self.__reader.tell() % _BLOCK_SIZE
    if pad_length and pad_length != _BLOCK_SIZE:
        data = self.__reader.read(pad_length)
        if len(data) != pad_length:
            raise EOFError('Read %d bytes instead of %d' % (len(data),
                pad_length))