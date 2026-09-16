def merge_table_records(self, table, record_data, match_column_names):
    table = table.get_soap_object(self.client)
    record_data = record_data.get_soap_object(self.client)
    return MergeResult(self.call('mergeTableRecords', table, record_data,
        match_column_names))