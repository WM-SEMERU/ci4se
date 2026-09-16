def schema_list(dbname, user=None, db_user=None, db_password=None, db_host=
    None, db_port=None):
    ret = {}
    query = ''.join([
        'SELECT pg_namespace.nspname as "name",pg_namespace.nspacl as "acl", pg_roles.rolname as "owner" FROM pg_namespace LEFT JOIN pg_roles ON pg_roles.oid = pg_namespace.nspowner '
        ])
    rows = psql_query(query, runas=user, host=db_host, user=db_user, port=
        db_port, maintenance_db=dbname, password=db_password)
    for row in rows:
        retrow = {}
        for key in ('owner', 'acl'):
            retrow[key] = row[key]
        ret[row['name']] = retrow
    return ret