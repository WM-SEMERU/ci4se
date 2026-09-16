def alter_add_column(self, table, column_name, field, **kwargs):
    name = field.name
    op = super(SchemaMigrator, self).alter_add_column(table, column_name,
        field, **kwargs)
    if isinstance(field, pw.ForeignKeyField):
        field.name = name
    return op