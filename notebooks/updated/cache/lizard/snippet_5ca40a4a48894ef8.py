def _getcols(cur, table):
    query = ' '.join(('SELECT * FROM', table, 'LIMIT 0'))
    cur.execute(query)
    colnames = [desc[0] for desc in cur.description]
    LOG.info('COLS (%s): %s', table, colnames)
    return