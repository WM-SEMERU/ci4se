def read(self, n=CHUNK_SIZE):
    if self.closed:
        return b('')
    s, disconnected = io_op(os.read, self.fd, n)
    if disconnected:
        LOG.debug('%r.read(): disconnected: %s', self, disconnected)
        return b('')
    return s