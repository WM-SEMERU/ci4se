def _resize_to_minimum(worksheet, rows=None, cols=None):
    current_cols, current_rows = worksheet.col_count, worksheet.row_count
    if rows is not None and rows <= current_rows:
        rows = None
    if cols is not None and cols <= current_cols:
        cols = None
    if cols is not None or rows is not None:
        worksheet.resize(rows, cols)