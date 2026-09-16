def database(self):
    if self._database:
        return self._database
    if self._recordSet is not None:
        return self._recordSet.database()
    else:
        return Orb.instance().database()