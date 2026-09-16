def p_expr_peektype_(p):
    p[0] = make_builtin(p.lineno(1), 'PEEK', make_typecast(TYPE.uinteger, p
        [5], p.lineno(4)), type_=p[3])