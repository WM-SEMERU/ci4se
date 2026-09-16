def evaluate_rpn(rpn):
    vals_stack = []
    for item in rpn:
        if item in _ALL_OPS:
            v2 = vals_stack.pop()
            if item in _UNARY_OPS:
                res = _UNARY_OPS[item](v2)
            elif item in _BIN_OPS:
                v1 = vals_stack.pop()
                res = _BIN_OPS[item](v1, v2)
            else:
                raise ValueError('%s not in unary_ops or bin_ops' % str(item))
            vals_stack.append(res)
        else:
            vals_stack.append(item)
    assert len(vals_stack) == 1
    assert isinstance(vals_stack[0], bool)
    return vals_stack[0]