def remove(src, rel, dst):
    smt = 'DELETE FROM %s' % rel
    queries = []
    params = []
    if src is not None:
        queries.append('src = ?')
        params.append(src)
    if dst is not None:
        queries.append('dst = ?')
        params.append(dst)
    if not queries:
        return smt, params
    smt = '%s WHERE %s' % (smt, ' AND '.join(queries))
    return smt, params