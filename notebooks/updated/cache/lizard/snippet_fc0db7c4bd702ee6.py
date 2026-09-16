def queuedb_create(path):
    global QUEUE_SQL, ERROR_SQL
    lines = [(l + ';') for l in QUEUE_SQL.split(';')]
    con = sqlite3.connect(path, isolation_level=None)
    db_query_execute(con, 'pragma mmap_size=536870912', ())
    for line in lines:
        db_query_execute(con, line, ())
    con.commit()
    con.row_factory = queuedb_row_factory
    return con