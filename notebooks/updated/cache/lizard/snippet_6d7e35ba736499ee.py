def _set_initial_contents(self, contents):
    contents = self._encode_contents(contents)
    changed = self._byte_contents != contents
    st_size = len(contents)
    if self._byte_contents:
        self.size = 0
    current_size = self.st_size or 0
    self.filesystem.change_disk_usage(st_size - current_size, self.name,
        self.st_dev)
    self._byte_contents = contents
    self.st_size = st_size
    self.epoch += 1
    return changed