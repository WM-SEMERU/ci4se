def _parse_entry(entry, limit=10):
    entry = entry.split(',')
    label = entry[0]
    points = limit
    if len(entry) > 1:
        proc = float(entry[1].strip())
        points = limit * proc
    return label, int(points)