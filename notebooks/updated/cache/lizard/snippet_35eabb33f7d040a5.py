def ast_to_sympy(expr):
    from dolang import to_source
    s = to_source(expr)
    not_to_be_treated_as_functions = ['alpha', 'beta', 'gamma', 'zeta', 'Chi']
    d = {v: sympy.Symbol(v) for v in not_to_be_treated_as_functions}
    return sympy.sympify(s, locals=d)