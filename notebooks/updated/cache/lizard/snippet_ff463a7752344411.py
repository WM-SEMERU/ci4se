def p_statement_draw3(p):
    p[0] = make_sentence('DRAW3', make_typecast(TYPE.integer, p[2], p.
        lineno(3)), make_typecast(TYPE.integer, p[4], p.lineno(5)),
        make_typecast(TYPE.float_, p[6], p.lineno(5)))