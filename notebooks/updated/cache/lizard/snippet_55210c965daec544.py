def limit(self, limit):
    query = self._copy()
    query._limit = limit
    return query