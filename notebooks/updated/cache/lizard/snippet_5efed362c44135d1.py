def get(self, key, range_end=None, count_only=None, keys_only=None, limit=
    None, max_create_revision=None, min_create_revision=None,
    min_mod_revision=None, revision=None, serializable=None, sort_order=
    None, sort_target=None, timeout=None):

    def run(pg_txn):
        pg_txn.execute('SELECT pgetcd.get(%s,%s)', (Binary(key), 10))
        rows = pg_txn.fetchall()
        res = '{0}'.format(rows[0][0])
        return res
    return self._pool.runInteraction(run)