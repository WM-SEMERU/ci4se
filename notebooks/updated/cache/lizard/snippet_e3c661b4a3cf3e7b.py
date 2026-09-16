def _reconnect(self):
    self.close()
    self._db = psycopg2.connect(**self._db_args)
    if self._search_path:
        self.execute('set search_path=%s;' % self._search_path)
    if self._timezone:
        self.execute("set timezone='%s';" % self._timezone)