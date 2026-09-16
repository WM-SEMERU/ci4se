def make_break(lineno, p):
    global last_brk_linenum
    if not OPTIONS.enableBreak.value or lineno == last_brk_linenum or is_null(p
        ):
        return None
    last_brk_linenum = lineno
    return make_sentence('CHKBREAK', make_number(lineno, lineno, TYPE.uinteger)
        )