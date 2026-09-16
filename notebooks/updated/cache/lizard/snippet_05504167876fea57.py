def p_let_arr_substr_in_args3(p):
    i = 2 if p[1].upper() == 'LET' else 1
    id_ = p[i]
    arg_list = p[i + 2]
    substr = make_number(0, lineno=p.lineno(i + 4)), make_number(gl.
        MAX_STRSLICE_IDX, lineno=p.lineno(i + 3))
    expr_ = p[i + 7]
    p[0] = make_array_substr_assign(p.lineno(i), id_, arg_list, substr, expr_)