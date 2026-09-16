def copy(self, contents=True):
    cp = connection(collection=self._db_coll, baseiri=self._baseiri)
    if contents:
        cp.add_many(self._relationships)
    return cp