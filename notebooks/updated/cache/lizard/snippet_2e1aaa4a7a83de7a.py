def execEmbCode(SCOPE, NAME, VAL, TEAL, codeStr):
    PARENT = None
    if TEAL:
        PARENT = TEAL.top
    OUT = None
    ldict = locals()
    exec(codeStr, globals(), ldict)
    return ldict['OUT']