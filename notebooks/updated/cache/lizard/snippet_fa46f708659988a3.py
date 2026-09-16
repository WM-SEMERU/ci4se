def update(self, row, keys, ensure=None, types=None, return_count=False):
    row = self._sync_columns(row, ensure, types=types)
    args, row = self._keys_to_args(row, keys)
    clause = self._args_to_clause(args)
    if not len(row):
        return self.count(clause)
    stmt = self.table.update(whereclause=clause, values=row)
    rp = self.db.executable.execute(stmt)
    if rp.supports_sane_rowcount():
        return rp.rowcount
    if return_count:
        return self.count(clause)