def schema_exists(dbname, name, user=None, db_user=None, db_password=None,
    db_host=None, db_port=None):
    return bool(schema_get(dbname, name, user=user, db_user=db_user,
        db_host=db_host, db_port=db_port, db_password=db_password))