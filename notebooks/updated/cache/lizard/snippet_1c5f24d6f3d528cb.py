def delete(self):
    if not HAS_SQL:
        return
    try:
        conn, c = self.connect()
        c.execute('DELETE FROM {0}'.format(self.table_name))
        conn.commit()
        conn.close()
    except:
        log.traceback(logging.DEBUG)