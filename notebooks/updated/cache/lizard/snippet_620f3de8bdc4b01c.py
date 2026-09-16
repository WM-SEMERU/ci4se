def namedb_select_count_rows(cur, query, args, count_column='COUNT(*)'):
    count_rows = namedb_query_execute(cur, query, args)
    count = 0
    for r in count_rows:
        count = r[count_column]
        break
    return count