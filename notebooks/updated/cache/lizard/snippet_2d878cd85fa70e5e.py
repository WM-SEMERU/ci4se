def _read_runtime_vars(variable_file, sep=','):
    rows = [x for x in read_file(variable_file).split('\n') if x.strip()]
    valid_rows = []
    if len(rows) > 0:
        header = rows.pop(0).split(sep)
        validate_header(header)
        for row in rows:
            row = _validate_row(row, sep=sep, required_length=4)
            if row:
                valid_rows.append(row)
    return valid_rows