def format_table(columns, rows):
    rows = [tuple(str(i) for i in r) for r in rows]
    columns = tuple(str(i).upper() for i in columns)
    if rows:
        widths = tuple(max(max(map(len, x)), len(c)) for x, c in zip(zip(*
            rows), columns))
    else:
        widths = tuple(map(len, columns))
    row_template = '    '.join('%%-%ds' for _ in columns) % widths
    header = (row_template % tuple(columns)).strip()
    if rows:
        data = '\n'.join((row_template % r).strip() for r in rows)
        return '\n'.join([header, data])
    else:
        return header