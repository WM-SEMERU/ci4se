def bulk_query(self, query, *multiparams):
    self._conn.execute(text(query), *multiparams)