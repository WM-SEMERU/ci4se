def close(self):
    if self.filename != ':memory:':
        if self._conn is not None:
            self._conn.commit()
            self._conn.close()
            self._conn = None