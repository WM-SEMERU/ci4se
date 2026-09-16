def nodes(self, path):
    path = posix_path(path)
    yield from (self.path(path, e) for e in self._handler.find(path))