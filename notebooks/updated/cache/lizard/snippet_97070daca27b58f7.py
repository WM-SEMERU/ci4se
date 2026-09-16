def get_metadata(ident_hash):
    id, version = get_id_n_version(ident_hash)
    stmt = _get_sql('get-metadata.sql')
    args = dict(id=id, version=version)
    with db_connect() as db_conn:
        with db_conn.cursor() as cursor:
            cursor.execute(stmt, args)
            try:
                metadata = cursor.fetchone()[0]
            except TypeError:
                raise NotFound(ident_hash)
    return metadata