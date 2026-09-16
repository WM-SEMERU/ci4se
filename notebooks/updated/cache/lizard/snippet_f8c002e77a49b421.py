def uninstall_pgpm_from_db(self):
    drop_schema_cascade_script = 'DROP SCHEMA {schema_name} CASCADE;'
    if self._conn.closed:
        self._conn = psycopg2.connect(self._connection_string,
            connection_factory=pgpm.lib.utils.db.MegaConnection)
    cur = self._conn.cursor()
    cur.execute(pgpm.lib.utils.db.SqlScriptsHelper.current_user_sql)
    current_user = cur.fetchone()[0]
    cur.execute(pgpm.lib.utils.db.SqlScriptsHelper.is_superuser_sql)
    is_cur_superuser = cur.fetchone()[0]
    if not is_cur_superuser:
        self._logger.debug(
            'User {0} is not a superuser. Only superuser can remove pgpm'.
            format(current_user))
        sys.exit(1)
    self._logger.debug('Removing pgpm from DB by dropping schema {0}'.
        format(self._pgpm_schema_name))
    cur.execute(drop_schema_cascade_script.format(schema_name=self.
        _pgpm_schema_name))
    self._conn.commit()
    self._conn.close()
    return 0