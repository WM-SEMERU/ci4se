def p_print_list_expr(p):
    if p[1] in ('BOLD', 'ITALIC'):
        p[0] = make_sentence(p[1] + '_TMP', make_typecast(TYPE.ubyte, p[2],
            p.lineno(1)))
    else:
        p[0] = p[1]