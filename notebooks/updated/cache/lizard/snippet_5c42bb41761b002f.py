def _write_to_file(self, filename, bytesvalue):
    fh, tmp = tempfile.mkstemp()
    with os.fdopen(fh, self._flag) as f:
        f.write(self._dumps(bytesvalue))
    rename(tmp, filename)
    os.chmod(filename, self._mode)