def p_expr_peek(p):
    p[0] = make_builtin(p.lineno(1), 'PEEK', make_typecast(TYPE.uinteger, p
        [2], p.lineno(1)), type_=TYPE.ubyte)