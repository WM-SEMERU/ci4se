def p_save_data(p):
    if p[2].type_ != TYPE.string:
        api.errmsg.syntax_error_expected_string(p.lineno(1), p[2].type_)
    if len(p) != 4:
        entry = SYMBOL_TABLE.access_id(p[4], p.lineno(4))
        if entry is None:
            p[0] = None
            return
        entry.accessed = True
        access = entry
        start = make_unary(p.lineno(4), 'ADDRESS', access, type_=TYPE.uinteger)
        if entry.class_ == CLASS.array:
            length = make_number(entry.memsize, lineno=p.lineno(4))
        else:
            length = make_number(entry.type_.size, lineno=p.lineno(4))
    else:
        access = SYMBOL_TABLE.access_id('.ZXBASIC_USER_DATA', p.lineno(3))
        start = make_unary(p.lineno(3), 'ADDRESS', access, type_=TYPE.uinteger)
        access = SYMBOL_TABLE.access_id('.ZXBASIC_USER_DATA_LEN', p.lineno(3))
        length = make_unary(p.lineno(3), 'ADDRESS', access, type_=TYPE.uinteger
            )
    p[0] = make_sentence(p[1], p[2], start, length)