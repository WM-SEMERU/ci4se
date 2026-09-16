def drop_database(self, name, force=False):
    if not force or self.exists_database(name):
        tables = self.list_tables(database=name)
        udfs = self.list_udfs(database=name)
        udas = self.list_udas(database=name)
    else:
        tables = []
        udfs = []
        udas = []
    if force:
        for table in tables:
            self.log('Dropping {0}'.format('{0}.{1}'.format(name, table)))
            self.drop_table_or_view(table, database=name)
        for func in udfs:
            self.log('Dropping function {0}({1})'.format(func.name, func.
                inputs))
            self.drop_udf(func.name, input_types=func.inputs, database=name,
                force=True)
        for func in udas:
            self.log('Dropping aggregate function {0}({1})'.format(func.
                name, func.inputs))
            self.drop_uda(func.name, input_types=func.inputs, database=name,
                force=True)
    elif len(tables) > 0 or len(udfs) > 0 or len(udas) > 0:
        raise com.IntegrityError(
            'Database {0} must be empty before being dropped, or set force=True'
            .format(name))
    statement = ddl.DropDatabase(name, must_exist=not force)
    return self._execute(statement)