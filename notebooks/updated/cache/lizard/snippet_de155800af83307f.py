def _handle_io(self, args, file, result, passphrase=False, binary=False):
    p = self._open_subprocess(args, passphrase)
    if not binary:
        stdin = codecs.getwriter(self._encoding)(p.stdin)
    else:
        stdin = p.stdin
    if passphrase:
        _util._write_passphrase(stdin, passphrase, self._encoding)
    writer = _util._threaded_copy_data(file, stdin)
    self._collect_output(p, result, writer, stdin)
    return result