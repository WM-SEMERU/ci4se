def indices(db=None):
    cur = _connect(db)
    if not cur:
        return False
    cur.execute(
        "SELECT name FROM sqlite_master WHERE type='index' ORDER BY name;")
    rows = cur.fetchall()
    return rows