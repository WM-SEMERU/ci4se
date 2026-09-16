def namedb_read_version(path):
    con = sqlite3.connect(path, isolation_level=None, timeout=2 ** 30)
    con.row_factory = namedb_row_factory
    sql = 'SELECT version FROM db_version;'
    args = ()
    try:
        rowdata = namedb_query_execute(con, sql, args, abort=False)
        row = rowdata.fetchone()
        return row['version']
    except:
        return '0.0.0.0'
    finally:
        con.close()