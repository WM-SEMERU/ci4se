def update(self, table, sys_id, **kparams):
    result = self.table_api_put(table, sys_id, **kparams)
    return self.to_record(result, table)