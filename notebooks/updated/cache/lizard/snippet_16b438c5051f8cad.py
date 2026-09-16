def write(self, s):
    if not self.isalive():
        raise EOFError('Pty is closed')
    if PY2:
        s = _unicode(s)
    success, nbytes = self.pty.write(s)
    if not success:
        raise IOError('Write failed')
    return nbytes