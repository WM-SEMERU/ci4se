def isbn(self):
    isbns = listify(chained_get(self._head, ['source', 'isbn'], []))
    if len(isbns) == 0:
        return None
    else:
        return tuple(i['$'] for i in isbns)