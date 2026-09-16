def create_space(self):
    cur = self._conn.cursor()
    cur.executescript(SQL_MODEL)
    self._conn.commit()
    cur.close()
    return