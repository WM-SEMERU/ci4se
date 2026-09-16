def _handle_stdout(self, ioloop, f, count=-1):
    output = non_blocking_read(self._popen.stdout, count)
    if not output:
        self._popen.stdout.close()
        self._popen.stdout = None
    else:
        self._output.write(output)
        self._register_stdout(ioloop)