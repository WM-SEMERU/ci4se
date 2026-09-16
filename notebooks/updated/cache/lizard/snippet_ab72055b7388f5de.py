def seek(self, offset, whence=os.SEEK_SET):
    if not self._is_open:
        raise IOError('Not opened.')
    if whence not in [os.SEEK_SET, os.SEEK_CUR, os.SEEK_END]:
        raise IOError('Unsupported whence.')
    self._file_object.seek(offset, whence)