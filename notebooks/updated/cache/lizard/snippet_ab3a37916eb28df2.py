def _findlinestarts(code_object):
    byte_increments = [c for c in code_object.co_lnotab[0::2]]
    line_increments = [c for c in code_object.co_lnotab[1::2]]
    lineno = code_object.co_firstlineno
    addr = 0
    for byte_incr, line_incr in zip(byte_increments, line_increments):
        if byte_incr:
            yield addr, lineno
            addr += byte_incr
        lineno += line_incr
    yield addr, lineno