def parse(self, ddl=None, source_database=None):
    if ddl is not None:
        self._ddl = ddl
    if source_database is not None:
        self.source_database = source_database
    if self._ddl is None:
        raise ValueError('DDL is not specified')
    ret = self._DDL_PARSE_EXPR.parseString(self._ddl)
    if 'schema' in ret:
        self._table.schema = ret['schema']
    self._table.name = ret['table']
    self._table.is_temp = True if 'temp' in ret else False
    for ret_col in ret['columns']:
        if ret_col.getName() == 'column':
            col = self._table.columns.append(column_name=ret_col['name'],
                data_type_array=ret_col['type'], array_brackets=ret_col[
                'array_brackets'] if 'array_brackets' in ret_col else None)
            if 'constraint' in ret_col:
                col.constraint = ret_col['constraint']
        elif ret_col.getName() == 'constraint':
            for col_name in ret_col['constraint_columns']:
                col = self._table.columns[col_name]
                if ret_col['type'] == 'PRIMARY KEY':
                    col.not_null = True
                    col.primary_key = True
                elif ret_col['type'] in ['UNIQUE', 'UNIQUE KEY']:
                    col.unique = True
                elif ret_col['type'] == 'NOT NULL':
                    col.not_null = True
    return self._table