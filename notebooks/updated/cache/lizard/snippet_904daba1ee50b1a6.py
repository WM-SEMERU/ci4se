def get_existing_keys(self, events):
    data = [e[self.key] for e in events]
    ss = ','.join(['%s' for _ in data])
    query = 'SELECT %s FROM %s WHERE %s IN (%s)' % (self.key, self.table,
        self.key, ss)
    cursor = self.conn.conn.cursor()
    cursor.execute(query, data)
    LOG.info('%s (data: %s)', query, data)
    existing = [r[0] for r in cursor.fetchall()]
    LOG.info('Existing IDs: %s' % existing)
    return set(existing)