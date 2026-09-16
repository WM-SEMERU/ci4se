def query_row(stmt, args=(), factory=None):
    for row in query(stmt, args, factory):
        return row
    return None