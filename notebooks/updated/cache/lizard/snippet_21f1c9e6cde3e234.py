def tabulate(d, transpose=False, thousands=True, key_fun=None, sep=',',
    align=True):
    pairs = d.keys()
    rows, cols = zip(*pairs)
    if transpose:
        rows, cols = cols, rows
    rows = sorted(set(rows))
    cols = sorted(set(cols))
    header = ['o'] + list(cols)
    table = []
    for r in rows:
        combo = [(r, c) for c in cols]
        if transpose:
            combo = [(c, r) for r, c in combo]
        data = [d.get(x, 'n/a') for x in combo]
        data = [('{0:.1f}'.format(x) if isinstance(x, float) else x) for x in
            data]
        if key_fun:
            data = [key_fun(x) for x in data]
        table.append([str(r)] + data)
    if not align:
        formatted = load_csv(header, table, sep=sep)
        return '\n'.join(formatted)
    return loadtable(header, table, thousands=thousands)