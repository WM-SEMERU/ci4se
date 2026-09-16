def migrate(pool, from_connection, to_connection):
    f = connect_database(from_connection)
    t = connect_database(to_connection)
    if isinstance(f, ProjectDB):
        for each in f.get_all():
            each = unicode_obj(each)
            logging.info('projectdb: %s', each['name'])
            t.drop(each['name'])
            t.insert(each['name'], each)
    elif isinstance(f, TaskDB):
        pool = Pool(pool)
        pool.map(lambda x, f=from_connection, t=to_connection:
            taskdb_migrating(x, f, t), f.projects)
    elif isinstance(f, ResultDB):
        pool = Pool(pool)
        pool.map(lambda x, f=from_connection, t=to_connection:
            resultdb_migrating(x, f, t), f.projects)