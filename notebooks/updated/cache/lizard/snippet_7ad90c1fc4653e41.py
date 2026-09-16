def get_table_columns(dbconn, tablename):
    cur = dbconn.cursor()
    cur.execute("PRAGMA table_info('%s');" % tablename)
    info = cur.fetchall()
    cols = [(i[1], i[2]) for i in info]
    return cols