def add_partition(self, spec, location=None):
    part_schema = self.partition_schema()
    stmt = ddl.AddPartition(self._qualified_name, spec, part_schema,
        location=location)
    return self._execute(stmt)