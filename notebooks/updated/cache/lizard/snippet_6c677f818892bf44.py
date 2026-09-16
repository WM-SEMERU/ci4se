def get_min_row_num(mention):
    span = _to_span(mention)
    if span.sentence.is_tabular():
        return span.sentence.cell.row_start
    else:
        return None