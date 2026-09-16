def truncate(self, timeout=None):
    client = self._instance._client
    table_admin_client = client.table_admin_client
    if timeout:
        table_admin_client.drop_row_range(self.name,
            delete_all_data_from_table=True, timeout=timeout)
    else:
        table_admin_client.drop_row_range(self.name,
            delete_all_data_from_table=True)