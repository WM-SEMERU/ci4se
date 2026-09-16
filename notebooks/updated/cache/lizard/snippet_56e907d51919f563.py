def selectop(table, field, value, op, complement=False):
    return select(table, field, lambda v: op(v, value), complement=complement)