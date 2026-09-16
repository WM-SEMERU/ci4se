def tupleize(rows, alphabetize_columns=getattr(settings,
    'ALPHABETIZE_COLUMNS', False)):
    l = []
    for r in rows:
        row = []
        row = list(r.values())
        l.append(row)
    if alphabetize_columns:
        col = sorted(zip(*l))
        result = zip(*col)
        return result
    else:
        return l