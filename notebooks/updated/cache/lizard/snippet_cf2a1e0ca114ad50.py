def fetch(self, buf=None, traceno=None):
    if buf is None:
        buf = self.buf
    if traceno is None:
        traceno = self.traceno
    try:
        if self.kind == TraceField:
            if traceno is None:
                return buf
            return self.filehandle.getth(traceno, buf)
        else:
            return self.filehandle.getbin()
    except IOError:
        if not self.readonly:
            return bytearray(len(self.buf))
        else:
            raise