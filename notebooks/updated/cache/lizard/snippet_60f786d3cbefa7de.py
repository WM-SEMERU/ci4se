def _aggregate(data, norm=True, sort_by='value', keys=None):
    if keys:
        vdict = {k: (0) for k in keys}
        for d in data:
            if d in keys:
                vdict[d] += 1
    else:
        vdict = {}
        for d in data:
            vdict[d] = vdict[d] + 1 if d in vdict else 1
    vals = [(k, v) for k, v in vdict.items()]
    if sort_by == 'value':
        vals.sort(key=lambda x: x[0])
    else:
        vals.sort(key=lambda x: x[1])
    xs = [v[0] for v in vals]
    if norm:
        raw_y = [v[1] for v in vals]
        total_y = sum(raw_y)
        ys = [(100.0 * y / total_y) for y in raw_y]
    else:
        ys = [v[1] for v in vals]
    return xs, ys