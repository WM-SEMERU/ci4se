def execute(self, conn, origin_site_name='', dataset='', block_name='',
    transaction=False):
    if not conn:
        dbsExceptionHandler('dbsException-db-conn-failed',
            'Oracle/Block/List.  Expects db connection from upper layer.',
            self.logger.exception)
    binds = {}
    if origin_site_name:
        wheresql = 'WHERE B.ORIGIN_SITE_NAME = :origin_site_name'
        binds.update(origin_site_name=origin_site_name)
    if dataset:
        if 'wheresql' in locals():
            wheresql += ' AND DS.DATASET = :dataset'
        else:
            wheresql = 'WHERE DS.DATASET = :dataset'
        binds.update(dataset=dataset)
    if block_name:
        if 'wheresql' in locals():
            wheresql += ' AND B.BLOCK_NAME = :block_name'
        else:
            wheresql = 'WHERE B.BLOCK_NAME = :block_name'
        binds.update(block_name=block_name)
    sql = '{sql} {wheresql}'.format(sql=self.sql, wheresql=wheresql)
    cursors = self.dbi.processData(sql, binds, conn, transaction,
        returnCursor=True)
    result = []
    for cursor in cursors:
        result.extend(self.formatCursor(cursor, size=100))
    return result