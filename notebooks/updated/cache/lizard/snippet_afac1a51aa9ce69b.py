def column_map(tables, columns):
    if not columns:
        return {t.name: None for t in tables}
    columns = set(columns)
    colmap = {t.name: list(set(t.columns).intersection(columns)) for t in
        tables}
    foundcols = tz.reduce(lambda x, y: x.union(y), (set(v) for v in colmap.
        values()))
    if foundcols != columns:
        raise RuntimeError('Not all required columns were found. Missing: {}'
            .format(list(columns - foundcols)))
    return colmap