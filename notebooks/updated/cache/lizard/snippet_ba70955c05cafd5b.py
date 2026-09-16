def connect(self, **kwargs):
    host = ait.config.get('database.host', kwargs.get('host', 'localhost'))
    port = ait.config.get('database.port', kwargs.get('port', 8086))
    un = ait.config.get('database.un', kwargs.get('un', 'root'))
    pw = ait.config.get('database.pw', kwargs.get('pw', 'root'))
    dbname = ait.config.get('database.dbname', kwargs.get('database', 'ait'))
    self._conn = self._backend.InfluxDBClient(host, port, un, pw)
    if dbname not in [v['name'] for v in self._conn.get_list_database()]:
        self.create(database=dbname)
    self._conn.switch_database(dbname)