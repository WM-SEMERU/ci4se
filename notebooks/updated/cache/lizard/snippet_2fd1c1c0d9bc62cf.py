def GetRowCache(self, query):
    query_hash = hash(query)
    if query_hash not in self._row_caches:
        self._row_caches[query_hash] = set()
    return self._row_caches[query_hash]