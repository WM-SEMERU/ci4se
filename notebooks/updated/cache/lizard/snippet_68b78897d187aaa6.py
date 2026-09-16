def open(self):
    try:
        self.graph.open(self.cache_uri, create=False)
        self._add_namespaces(self.graph)
        self.is_open = True
    except Exception:
        raise InvalidCacheException('The cache is invalid or not created')