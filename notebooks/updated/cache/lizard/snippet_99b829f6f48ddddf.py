def reverse_transform(self, tables, table_metas=None, missing=None):
    if missing is None:
        missing = self.missing
    else:
        self.missing = missing
        warnings.warn(DEPRECATION_MESSAGE.format('reverse_transform'),
            DeprecationWarning)
    reverse = {}
    for table_name in tables:
        table = tables[table_name]
        if table_metas is None:
            table_meta = self.table_dict[table_name][1]
        else:
            table_meta = table_metas[table_name]
        reverse[table_name] = self.reverse_transform_table(table, table_meta)
    return reverse