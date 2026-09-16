def _rows_differ(row, _row):
    row_copy = copy.deepcopy(row)
    _row_copy = copy.deepcopy(_row)
    for panel in row_copy['panels']:
        if 'id' in panel:
            del panel['id']
    for _panel in _row_copy['panels']:
        if 'id' in _panel:
            del _panel['id']
    diff = DictDiffer(row_copy, _row_copy)
    return diff.changed() or diff.added() or diff.removed()