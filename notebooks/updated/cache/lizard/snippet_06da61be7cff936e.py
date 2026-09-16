def query_value(stmt, args=(), default=None):
    for row in query(stmt, args, TupleFactory):
        return row[0]
    return default