def delimited_file(self, hdfs_dir, schema, name=None, database=None,
    delimiter=',', na_rep=None, escapechar=None, lineterminator=None,
    external=True, persist=False):
    name, database = self._get_concrete_table_path(name, database, persist=
        persist)
    stmt = ddl.CreateTableDelimited(name, hdfs_dir, schema, database=
        database, delimiter=delimiter, external=external, na_rep=na_rep,
        lineterminator=lineterminator, escapechar=escapechar)
    self._execute(stmt)
    return self._wrap_new_table(name, database, persist)