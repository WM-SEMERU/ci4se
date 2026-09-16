def p_expr_post_incdec(p):
    p[0] = ast.PostIncDecOp(p[2], p[1], lineno=p.lineno(2))