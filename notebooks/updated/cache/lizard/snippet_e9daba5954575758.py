def clear_table(dbconn, table_name):
    cur = dbconn.cursor()
    cur.execute("DELETE FROM '{name}'".format(name=table_name))
    dbconn.commit()