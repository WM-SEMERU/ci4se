def size(self):
    if self._size is None:
        self._size = 0
        for csv_file in self.files:
            self._size += sum(1 if line else 0 for line in _util.
                open_local_or_gcs(csv_file, 'r'))
    return self._size