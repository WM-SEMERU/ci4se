def fit_transform(self, tables=None, transformer_dict=None,
    transformer_list=None, missing=None):
    if missing is None:
        missing = self.missing
    else:
        self.missing = missing
        warnings.warn(DEPRECATION_MESSAGE.format('fit_transform'),
            DeprecationWarning)
    transformed = {}
    if tables is None:
        tables = self.table_dict
    if transformer_dict is None and transformer_list is None:
        transformer_dict = self.transformer_dict
    for table_name in tables:
        table, table_meta = tables[table_name]
        transformed_table = self.fit_transform_table(table, table_meta,
            transformer_dict, transformer_list)
        transformed[table_name] = transformed_table
    return transformed