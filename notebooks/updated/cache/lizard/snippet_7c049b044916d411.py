def listFileParents(self, logical_file_name='', block_id=0, block_name=''):
    if not logical_file_name and not block_name and not block_id:
        dbsExceptionHandler('dbsException-invalid-input',
            'Logical_file_name, block_id or block_name is required for fileparents api'
            , self.logger.exception)
    with self.dbi.connection() as conn:
        sqlresult = self.fileparentlist.execute(conn, logical_file_name,
            block_id, block_name)
        d = {}
        for i in sqlresult:
            k = i['this_logical_file_name']
            v = i['parent_logical_file_name']
            d.setdefault(k, []).append(v)
        for k, v in d.iteritems():
            yield {'logical_file_name': k, 'parent_logical_file_name': v}
        del d