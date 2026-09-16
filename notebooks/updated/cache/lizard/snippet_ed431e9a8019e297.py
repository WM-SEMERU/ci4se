def reindex_like(self, other, method=None, tolerance=None, copy=True):
    indexers = alignment.reindex_like_indexers(self, other)
    return self.reindex(indexers=indexers, method=method, copy=copy,
        tolerance=tolerance)