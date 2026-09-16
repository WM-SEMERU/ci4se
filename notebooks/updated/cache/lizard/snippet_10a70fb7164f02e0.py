def p_else_part_endif(p):
    if p[2] == '\n':
        if len(p) == 4:
            p[0] = [make_nop(), p[3]]
        elif len(p) == 6:
            p[0] = [make_label(p[3], p.lineno(3)), p[4], p[5]]
        else:
            p[0] = [p[3], p[4]]
    else:
        p[0] = [p[2], p[3]]