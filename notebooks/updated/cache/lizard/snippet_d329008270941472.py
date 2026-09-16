def _inject_closure_values_fix_code(c, injected, **kwargs):
    c.freevars += injected
    for i, (opcode, value) in enumerate(c.code):
        if opcode == byteplay.LOAD_GLOBAL and value in kwargs:
            c.code[i] = byteplay.LOAD_DEREF, value
    _inject_closure_values_fix_closures(c, injected, **kwargs)
    return c