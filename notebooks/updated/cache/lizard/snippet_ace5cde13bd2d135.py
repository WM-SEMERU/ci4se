def _agate_to_schema(self, agate_table, column_override):
    bq_schema = []
    for idx, col_name in enumerate(agate_table.column_names):
        inferred_type = self.convert_agate_type(agate_table, idx)
        type_ = column_override.get(col_name, inferred_type)
        bq_schema.append(google.cloud.bigquery.SchemaField(col_name, type_))
    return bq_schema