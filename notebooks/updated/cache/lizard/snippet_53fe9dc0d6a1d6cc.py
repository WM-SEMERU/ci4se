def p_if_sentence(p):
    cond_ = p[1]
    if len(p) == 6:
        lbl = make_label(p[3], p.lineno(3))
        stat_ = make_block(lbl, p[4])
        endif_ = p[5]
    elif len(p) == 5:
        stat_ = p[3]
        endif_ = p[4]
    else:
        stat_ = make_nop()
        endif_ = p[3]
    p[0] = make_sentence('IF', cond_, make_block(stat_, endif_), lineno=p.
        lineno(2))