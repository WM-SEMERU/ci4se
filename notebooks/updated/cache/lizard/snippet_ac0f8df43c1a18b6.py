def sql(state, host, sql, database=None, postgresql_user=None,
    postgresql_password=None, postgresql_host=None, postgresql_port=None):
    yield make_execute_psql_command(sql, database=database, user=
        postgresql_user, password=postgresql_password, host=postgresql_host,
        port=postgresql_port)