def upsert(self, row, keys, ensure=None, types=None):
    row = self._sync_columns(row, ensure, types=types)
    if self._check_ensure(ensure):
        self.create_index(keys)
    row_count = self.update(row, keys, ensure=False, return_count=True)
    if row_count == 0:
        return self.insert(row, ensure=False)
    return True