def _prepend_row_index(rows, index):
    if index is None or index is False:
        return rows
    if len(index) != len(rows):
        print('index=', index)
        print('rows=', rows)
        raise ValueError('index must be as long as the number of data rows')
    rows = [([v] + list(row)) for v, row in zip(index, rows)]
    return rows