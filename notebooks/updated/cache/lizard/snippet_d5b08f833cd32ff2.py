def wait(self, num_slaves, timeout=0):
    command = [b'WAIT', ascii(num_slaves).encode('ascii'), ascii(timeout).
        encode('ascii')]
    return self._execute(command)