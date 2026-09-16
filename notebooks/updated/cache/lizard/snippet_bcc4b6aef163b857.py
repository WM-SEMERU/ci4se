def search(self, value, createIndex=None):
    if createIndex:
        self._createIndex = createIndex
    self._search = True
    self.filter(QueryExpression({'$text': {'$search': value}}))
    return self