def sympy_expressions_equal(expr1, expr2):
    try:
        difference = sympy.simplify(sympy.expand(expr1 - expr2))
    except SympifyError:
        if isinstance(expr1, sympy.Matrix) or isinstance(expr2, sympy.Matrix):
            return _sympy_matrices_equal(expr1, expr2)
        else:
            raise
    try:
        difference = sum(difference)
    except TypeError:
        pass
    return difference == 0