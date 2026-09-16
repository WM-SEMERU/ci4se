def selectfalse(table, field, complement=False):
    return select(table, field, lambda v: not bool(v), complement=complement)