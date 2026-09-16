def isin(arg, values):
    op = ops.Contains(arg, values)
    return op.to_expr()