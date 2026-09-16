def read(self, size=None):
    if not self._is_open:
        raise IOError('Not opened.')
    if self._fsntfs_data_stream:
        return self._fsntfs_data_stream.read(size=size)
    return self._fsntfs_file_entry.read(size=size)