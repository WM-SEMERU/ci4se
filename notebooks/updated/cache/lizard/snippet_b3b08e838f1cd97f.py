def execute(self, query, args=None):
    self._ensure_conn()
    cur = self._conn.cursor()
    yield cur.execute(query, args)
    raise Return(cur)