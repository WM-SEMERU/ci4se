def rst_table(data, header=None, fmt=None):
    if header is None and hasattr(data, '_fields'):
        header = data._fields
    try:
        data.dtype.fields
    except AttributeError:
        header = header or ()
    else:
        if not header:
            header = [col.split(':')[0] for col in build_header(data.dtype)]
    if header:
        col_sizes = [len(col) for col in header]
    else:
        col_sizes = [len(str(col)) for col in data[0]]
    body = []
    fmt = functools.partial(scientificformat, fmt=fmt) if fmt else form
    for row in data:
        tup = tuple(fmt(c) for c in row)
        for i, col in enumerate(tup):
            col_sizes[i] = max(col_sizes[i], len(col))
        if len(tup) != len(col_sizes):
            raise ValueError(
                'The header has %d fields but the row %d fields!' % (len(
                col_sizes), len(tup)))
        body.append(tup)
    sepline = ' '.join('=' * size for size in col_sizes)
    templ = ' '.join('%-{}s'.format(size) for size in col_sizes)
    if header:
        lines = [sepline, templ % tuple(header), sepline]
    else:
        lines = [sepline]
    for row in body:
        lines.append(templ % row)
    lines.append(sepline)
    return '\n'.join(lines)