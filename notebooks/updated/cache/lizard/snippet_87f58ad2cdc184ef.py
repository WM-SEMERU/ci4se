def create_postgresql_psycopg2cffi(username, password, host, port, database,
    **kwargs):
    return create_engine(_create_postgresql_psycopg2cffi(username, password,
        host, port, database), **kwargs)