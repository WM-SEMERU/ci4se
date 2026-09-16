def create_mysql_mysqldb(username, password, host, port, database, **kwargs):
    return create_engine(_create_mysql_mysqldb(username, password, host,
        port, database), **kwargs)