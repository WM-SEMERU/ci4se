def invalidate_metadata(self, name=None, database=None):
    stmt = 'INVALIDATE METADATA'
    if name is not None:
        stmt = self._table_command(stmt, name, database=database)
    self._execute(stmt)