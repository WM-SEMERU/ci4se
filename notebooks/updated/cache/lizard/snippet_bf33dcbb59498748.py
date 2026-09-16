def as_treemap(self):
    if self._treemap_cache:
        return self._treemap_cache
    self._treemap_cache = treemap = TreeMap(self)
    return treemap