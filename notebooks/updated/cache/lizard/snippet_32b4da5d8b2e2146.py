def first(self, columns=None):
    self._query.take(1)
    results = self.get(columns)
    if len(results) > 0:
        return results.first()
    return