def p_poke2(p):
    i = 2 if isinstance(p[2], Symbol) or p[2] is None else 3
    if p[i + 1] is None or p[i + 3] is None:
        p[0] = None
        return
    p[0] = make_sentence('POKE', make_typecast(TYPE.uinteger, p[i + 1], p.
        lineno(i + 2)), make_typecast(p[i], p[i + 3], p.lineno(i + 3)))