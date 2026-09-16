def read(self, n):
    d = b''
    while n:
        try:
            block = self._process.stdout.read(n)
        except ValueError:
            block = None
        if not block:
            self._process.poll()
            raise EOFError('Process ended')
        d += block
        n -= len(block)
    return d