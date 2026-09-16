def _fix_insert(self, sql, params):
    meta = self.query.get_meta()
    if meta.has_auto_field:
        if hasattr(self.query, 'fields'):
            fields = self.query.fields
            auto_field = meta.auto_field
        else:
            fields = self.query.columns
            auto_field = meta.auto_field.db_column or meta.auto_field.column
        auto_in_fields = auto_field in fields
        quoted_table = self.connection.ops.quote_name(meta.db_table)
        if not fields or auto_in_fields and len(fields) == 1 and not params:
            sql = 'INSERT INTO {0} DEFAULT VALUES'.format(quoted_table)
            params = []
        elif auto_in_fields:
            sql = (
                'SET IDENTITY_INSERT {table} ON;{sql};SET IDENTITY_INSERT {table} OFF'
                .format(table=quoted_table, sql=sql))
    if self.return_id and self.connection.features.can_return_id_from_insert:
        col = self.connection.ops.quote_name(meta.pk.db_column or meta.pk.
            get_attname())
        pk_db_type = _re_data_type_terminator.split(meta.pk.db_type(self.
            connection))[0]
        sql = ('SET NOCOUNT ON;{declare_table_var};{sql};{select_return_id}'
            .format(sql=sql, declare_table_var=
            'DECLARE @sqlserver_ado_return_id table ({col_name} {pk_type})'
            .format(col_name=col, pk_type=pk_db_type), select_return_id=
            'SELECT * FROM @sqlserver_ado_return_id'))
        output = self._values_repl.format(col=col)
        sql = self._re_values_sub.sub(output, sql)
    return sql, params