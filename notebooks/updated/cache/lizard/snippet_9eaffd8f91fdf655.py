def cache(self):
    if not self._cache:
        self._cache = self.graph.get('%s' % self.id)
    return self._cache