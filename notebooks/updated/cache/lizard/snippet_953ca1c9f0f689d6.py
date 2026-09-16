def p_pause(p):
    p[0] = make_sentence('PAUSE', make_typecast(TYPE.uinteger, p[2], p.
        lineno(1)))