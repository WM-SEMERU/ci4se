def _conn_string_adodbapi(self, db_key, instance=None, conn_key=None,
    db_name=None):
    if instance:
        _, host, username, password, database, _ = self._get_access_info(
            instance, db_key, db_name)
    elif conn_key:
        _, host, username, password, database, _ = conn_key.split(':')
    p = self._get_adoprovider(instance)
    conn_str = 'Provider={};Data Source={};Initial Catalog={};'.format(p,
        host, database)
    if username:
        conn_str += 'User ID={};'.format(username)
    if password:
        conn_str += 'Password={};'.format(password)
    if not username and not password:
        conn_str += 'Integrated Security=SSPI;'
    return conn_str