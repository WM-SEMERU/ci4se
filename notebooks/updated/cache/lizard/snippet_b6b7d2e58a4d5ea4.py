def write(self, data):
    self._process.poll()
    if self._process.returncode is not None:
        raise EOFError('Process ended')
    self._process.stdin.write(data)