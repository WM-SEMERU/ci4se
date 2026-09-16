def db_tables(name, **connection_args):
    if not db_exists(name, **connection_args):
        log.info("Database '%s' does not exist", name)
        return False
    dbc = _connect(**connection_args)
    if dbc is None:
        return []
    cur = dbc.cursor()
    s_name = quote_identifier(name)
    qry = 'SHOW TABLES IN {0}'.format(s_name)
    try:
        _execute(cur, qry)
    except MySQLdb.OperationalError as exc:
        err = 'MySQL Error {0}: {1}'.format(*exc.args)
        __context__['mysql.error'] = err
        log.error(err)
        return []
    ret = []
    results = cur.fetchall()
    for table in results:
        ret.append(table[0])
    log.debug(ret)
    return ret