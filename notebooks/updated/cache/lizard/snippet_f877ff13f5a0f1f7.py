def p_expression(self, p):
    if len(p) == 2:
        left, op, right = p[1], None, None
    else:
        __, left, op, right = p
    p[0] = _filter.Expression(left, op, right)