def select(self, columns=(), by=(), where=(), **kwds):
    return self._seu('select', columns, by, where, kwds)