def query(self, sql, *args, **kwargs):
    with self.locked() as conn:
        for row in conn.query(sql, *args, **kwargs):
            yield row