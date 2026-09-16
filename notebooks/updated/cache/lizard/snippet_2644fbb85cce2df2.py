def get(self, path):
    mountpoint, chunks = self.get_mountpoint(path)
    if mountpoint is None:
        return self._files.get(self._join_chunks(chunks))
    else:
        return mountpoint.get(chunks)