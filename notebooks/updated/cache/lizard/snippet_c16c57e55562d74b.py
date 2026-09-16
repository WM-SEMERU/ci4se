def HashFile(self, fd, byte_count):
    while byte_count > 0:
        buf_size = min(byte_count, constants.CLIENT_MAX_BUFFER_SIZE)
        buf = fd.read(buf_size)
        if not buf:
            break
        self.HashBuffer(buf)
        byte_count -= buf_size