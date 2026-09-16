def check_columns(column, line, columns):
    return column <= min(len(line), max(columns))