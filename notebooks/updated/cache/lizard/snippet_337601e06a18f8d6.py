def delete_records(keep=20):
    sql = (
        'SELECT * from records where is_deleted<>1 ORDER BY id desc LIMIT -1 offset {}'
        .format(keep))
    assert isinstance(g.db, sqlite3.Connection)
    c = g.db.cursor()
    c.execute(sql)
    rows = c.fetchall()
    for row in rows:
        name = row[1]
        xmind = join(app.config['UPLOAD_FOLDER'], name)
        xml = join(app.config['UPLOAD_FOLDER'], name[:-5] + 'xml')
        for f in [xmind, xml]:
            if exists(f):
                os.remove(f)
        sql = 'UPDATE records SET is_deleted=1 WHERE id = ?'
        c.execute(sql, (row[0],))
        g.db.commit()