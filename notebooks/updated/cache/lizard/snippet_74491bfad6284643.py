def _make_cell_set_template_code():

    def inner(value):
        lambda : cell
        cell = value
    co = inner.__code__
    if not PY3:
        return types.CodeType(co.co_argcount, co.co_nlocals, co.
            co_stacksize, co.co_flags, co.co_code, co.co_consts, co.
            co_names, co.co_varnames, co.co_filename, co.co_name, co.
            co_firstlineno, co.co_lnotab, co.co_cellvars, ())
    else:
        return types.CodeType(co.co_argcount, co.co_kwonlyargcount, co.
            co_nlocals, co.co_stacksize, co.co_flags, co.co_code, co.
            co_consts, co.co_names, co.co_varnames, co.co_filename, co.
            co_name, co.co_firstlineno, co.co_lnotab, co.co_cellvars, ())