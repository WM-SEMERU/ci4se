def _rows_from_json(values, schema):
    from google.cloud.bigquery import Row
    field_to_index = _field_to_index_mapping(schema)
    return [Row(_row_tuple_from_json(r, schema), field_to_index) for r in
        values]