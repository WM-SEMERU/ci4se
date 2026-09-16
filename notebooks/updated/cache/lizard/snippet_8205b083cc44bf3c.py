def list_partitions(self, table, retry=DEFAULT_RETRY):
    table = _table_arg_to_table_ref(table, default_project=self.project)
    meta_table = self.get_table(TableReference(self.dataset(table.
        dataset_id, project=table.project), '%s$__PARTITIONS_SUMMARY__' %
        table.table_id))
    subset = [col for col in meta_table.schema if col.name == 'partition_id']
    return [row[0] for row in self.list_rows(meta_table, selected_fields=
        subset, retry=retry)]