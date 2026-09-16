def p_print_list_comma(p):
    p[0] = p[1]
    p[0].eol = p[3] is not None
    p[0].appendChild(make_sentence('PRINT_COMMA'))
    if p[3] is not None:
        p[0].appendChild(p[3])