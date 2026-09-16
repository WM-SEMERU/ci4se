def p_elseif_list(p):
    label_, cond_ = p[1]
    then_ = p[2]
    else_ = p[3]
    if isinstance(else_, list):
        else_ = make_block(*else_)
    else:
        then_ = make_block(then_, else_)
        else_ = None
    p[0] = make_block(label_, make_sentence('IF', cond_, then_, else_,
        lineno=p.lineno(1)))