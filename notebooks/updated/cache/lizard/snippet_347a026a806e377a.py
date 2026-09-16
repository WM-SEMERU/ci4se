def reset(self, total_size=None):
    self.root = FakeDirectory(self.path_separator, filesystem=self)
    self.cwd = self.root.name
    self.open_files = []
    self._free_fd_heap = []
    self._last_ino = 0
    self._last_dev = 0
    self.mount_points = {}
    self.add_mount_point(self.root.name, total_size)
    self._add_standard_streams()