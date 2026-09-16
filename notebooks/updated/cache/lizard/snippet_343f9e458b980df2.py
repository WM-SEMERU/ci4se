def visit(d, op):
    op(d)
    if isinstance(d, list):
        for i in d:
            visit(i, op)
    elif isinstance(d, dict):
        for i in itervalues(d):
            visit(i, op)