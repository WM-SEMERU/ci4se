def p_expr_OR_expr(p):
    p[0] = make_binary(p.lineno(2), 'OR', p[1], p[3], lambda x, y: x or y)