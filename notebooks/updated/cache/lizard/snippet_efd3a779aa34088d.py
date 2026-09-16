def p_statement_plot_attr(p):
    p[0] = make_sentence('PLOT', make_typecast(TYPE.ubyte, p[3], p.lineno(4
        )), make_typecast(TYPE.ubyte, p[5], p.lineno(4)), p[2])