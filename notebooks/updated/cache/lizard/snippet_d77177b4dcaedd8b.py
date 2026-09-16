def solve_each(expr, vars):
    lhs_values, _ = __solve_for_repeated(expr.lhs, vars)
    for lhs_value in repeated.getvalues(lhs_values):
        result = solve(expr.rhs, __nest_scope(expr.lhs, vars, lhs_value))
        if not result.value:
            return result._replace(value=False)
    return Result(True, ())