def _handle_stderr(self, ioloop, f, count=-1):
    output = non_blocking_read(self._popen.stderr, count)
    if not output:
        self._popen.stderr.close()
        self._popen.stderr = None
    else:
        self._error.write(output)
        self._register_stderr(ioloop)