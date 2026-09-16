def db(self):
    if not self._db:
        self._db = pgtablestorage.DB(dburl=self.dburl)
    return self._db