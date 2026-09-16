def insert_or_append_blocks(self, blocks):
    start = 0
    bulk_insert = self.bulk_insert
    blocks_len = len(blocks)
    select = 'SELECT ?,?,?,"",0'
    query = (
        'INSERT OR IGNORE INTO gauged_data (namespace, offset, `key`, data, flags) '
        )
    execute = self.cursor.execute
    while start < blocks_len:
        rows = blocks[start:start + bulk_insert]
        params = []
        for namespace, offset, key, _, _ in rows:
            params.extend((namespace, offset, key))
        insert = (select + ' UNION ') * (len(rows) - 1) + select
        execute(query + insert, params)
        start += bulk_insert
    for namespace, offset, key, data, flags in blocks:
        execute(
            'UPDATE gauged_data SET data = CAST(data || ? AS BLOB),flags = ? WHERE namespace = ? AND offset = ? AND `key` = ?'
            , (data, flags, namespace, offset, key))