def grid_to_obj(cls, file_path=None, text='', edges=None, columns=None,
    eval_cells=True, key_on=None):
    edges = edges if edges else cls.FANCY
    lines = cls._get_lines(file_path, text)
    data = []
    for i in range(len(lines) - 1):
        if i % 2 == 1:
            row = lines[i].split(edges['internal vertical edge'])[1:-1]
            data.append([cls._eval_cell(r, _eval=eval_cells) for r in row])
    row_columns = data[0]
    if len(row_columns) != len(set(row_columns)):
        for i, col in enumerate(row_columns):
            count = row_columns[:i].count(col)
            row_columns[i] = '%s_%s' % (col, count) if count else col
    return cls.list_to_obj(data[1:], columns=columns, row_columns=
        row_columns, key_on=key_on)