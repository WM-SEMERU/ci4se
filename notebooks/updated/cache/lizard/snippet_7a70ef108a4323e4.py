def cursor():
    try:
        cur = conn.cursor()
        yield cur
    except (db.Error, Exception) as e:
        cur.close()
        if conn:
            conn.rollback()
        print(e.message)
        raise
    else:
        conn.commit()
        cur.close()