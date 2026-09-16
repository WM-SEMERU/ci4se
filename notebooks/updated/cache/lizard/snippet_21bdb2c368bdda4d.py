def load_data(self, path, overwrite=False, partition=None):
    if partition is not None:
        partition_schema = self.partition_schema()
    else:
        partition_schema = None
    stmt = ddl.LoadData(self._qualified_name, path, partition=partition,
        partition_schema=partition_schema)
    return self._execute(stmt)