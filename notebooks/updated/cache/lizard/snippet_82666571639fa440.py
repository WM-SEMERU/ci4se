def query(self, query):
    if str(query.key) in self._items:
        return query(self._items[str(query.key)].values())
    else:
        return query([])