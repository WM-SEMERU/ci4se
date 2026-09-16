def read(self):
    with self._path.open(mode='r') as fh:
        version = fh.read().strip()
    return Version(version)