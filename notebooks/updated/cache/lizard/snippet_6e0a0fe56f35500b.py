def transform_op(self, op, value):
    if value is None:
        if _EQ_RE.match(op):
            return 'is'
        elif _NEQ_RE.match(op):
            return 'is not'
    return op