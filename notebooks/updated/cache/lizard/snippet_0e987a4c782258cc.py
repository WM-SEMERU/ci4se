def get_mountpoint(self, path):
    path_chunks = self._normalize_path(path)
    for i in range(len(path_chunks) - 1, -1, -1):
        partial_path = self._join_chunks(path_chunks[:-i])
        if partial_path in self._mountpoints:
            mountpoint = self._mountpoints[partial_path]
            if mountpoint is None:
                break
            return mountpoint, path_chunks[-i:]
    return None, path_chunks