def insert(self, row):
    self._check_dropped()
    res = self.engine.execute(self.table.insert(row))
    if len(res.inserted_primary_key) > 0:
        return res.inserted_primary_key[0]