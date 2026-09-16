def read_moc_ascii(moc, filename=None, file=None):
    if file is not None:
        orders = _read_ascii(file)
    else:
        with open(filename, 'r') as f:
            orders = _read_ascii(f)
    for text in orders:
        if not text:
            continue
        cells = []
        order, ranges = text.split('/')
        for r in ranges.split(','):
            try:
                cells.append(int(r))
            except ValueError as e:
                rmin, rmax = r.split('-')
                cells.extend(range(int(rmin), int(rmax) + 1))
        moc.add(order, cells)