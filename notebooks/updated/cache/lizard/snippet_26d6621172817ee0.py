def iterativeFetch(query, batchSize=default_batch_size):
    while True:
        rows = query.fetchmany(batchSize)
        if not rows:
            break
        rowDicts = sqliteRowsToDicts(rows)
        for rowDict in rowDicts:
            yield rowDict