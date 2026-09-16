def sqlupdate(table, rowupdate, where):
    validate_name(table)
    fields = sorted(rowupdate.keys())
    validate_names(fields)
    values = [rowupdate[field] for field in fields]
    setparts = [(field + '=%s') for field in fields]
    setclause = ', '.join(setparts)
    sql = 'update {} set '.format(table) + setclause
    whereclause, wherevalues = sqlwhere(where)
    if whereclause:
        sql = sql + ' where ' + whereclause
    return sql, values + wherevalues