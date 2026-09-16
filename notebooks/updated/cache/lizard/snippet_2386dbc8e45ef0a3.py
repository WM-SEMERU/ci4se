def load_csv_stream(ctx, model, data, header=None, header_exclude=None, **
    fmtparams):
    _header, _rows = read_csv(data, **fmtparams)
    header = header if header else _header
    if _rows:
        if header != _header and not header_exclude:
            header_exclude = [x for x in _header if x not in header]
        if header_exclude:
            header = [x for x in header if x not in header_exclude]
            pop_idxs = [_header.index(x) for x in header_exclude]
            rows = []
            for i, row in enumerate(_rows):
                rows.append([x for j, x in enumerate(row) if j not in pop_idxs]
                    )
        else:
            rows = list(_rows)
        if rows:
            load_rows(ctx, model, header, rows)