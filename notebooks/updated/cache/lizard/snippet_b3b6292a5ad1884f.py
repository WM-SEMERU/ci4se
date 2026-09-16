def user_remove(name, user=None, password=None, host=None, port=None,
    database='admin', authdb=None):
    conn = _connect(user, password, host, port)
    if not conn:
        return 'Failed to connect to mongo database'
    try:
        log.info('Removing user %s', name)
        mdb = pymongo.database.Database(conn, database)
        mdb.remove_user(name)
    except pymongo.errors.PyMongoError as err:
        log.error('Creating database %s failed with error: %s', name, err)
        return six.text_type(err)
    return True