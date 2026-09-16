def flush(self):
    if not self._buffer:
        return
    data = ''.join(self._buffer)
    try:
        if self.write_binary:
            if hasattr(self.stdout, 'buffer'):
                out = self.stdout.buffer
            else:
                out = self.stdout
            out.write(data.encode(self.stdout.encoding or 'utf-8', 'replace'))
        else:
            self.stdout.write(data)
        self.stdout.flush()
    except IOError as e:
        if e.args and e.args[0] == errno.EINTR:
            pass
        elif e.args and e.args[0] == 0:
            pass
        else:
            raise
    self._buffer = []