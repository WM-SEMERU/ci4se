def _write(self, s):
    while s:
        n = self.sslobj.write(s)
        if not n:
            raise IOError('Socket closed')
        s = s[n:]