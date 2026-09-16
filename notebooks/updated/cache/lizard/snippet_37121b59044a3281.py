def create(self, **kwargs):
    dbname = ait.config.get('database.dbname', kwargs.get('database', 'ait'))
    if self._conn is None:
        raise AttributeError(
            'Unable to create database. No connection to database exists.')
    self._conn.create_database(dbname)
    self._conn.switch_database(dbname)