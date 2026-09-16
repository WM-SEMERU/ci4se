def decode(self, node, cache=None, as_map_key=False):
    if not cache:
        cache = RollingCache()
    return self._decode(node, cache, as_map_key)